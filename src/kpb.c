/* Known-plaintext attack on a double columnar transposition, second-key side: finds the second key (width Lb) by simulated annealing. After undoing the second transposition, adjacent letters of the intermediate text are plaintext letters La apart, whatever the first key is. Tolerates a plaintext whose separators are slightly misplaced.
   Build: clang -O2 -o kpb kpb.c -lm    (original comments below are in Japanese) */
// 二重の列転置の既知平文攻撃（後ろの鍵の側）。暗号文 C と平文 P から、後ろの鍵（幅 Lb の列の読み順）を焼きなましで探す。
// 点：後ろの転置を戻した中間の文 I は、平文の列転置（幅 La）なので、I で隣り合う字の組・3字組は、
//     平文で La 字離れた字の組・3字組（櫛の続き）になる（櫛の切れ目 La-1 か所を除く）。前の鍵の順には関係しない。
//     平文の X の位置が1か所ずれても、ずれをまたぐ組（全体の La/n ほど）しか外れない。
// 使い方: kpb P C LaMin LaMax LbMin LbMax 歩数 やり直し 種 [鍵と I を出す下限(0-1)]
// 出力: La Lb 点の割合 当たり2/上限2 当たり3/上限3 [| 後ろの鍵（列ごとの読み順、0始まり） | I]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 512
int n,np; char P[MAXN],C[MAXN]; int cD2[676]; int cD3[17576]; int cV2[676]; int cV3[17576];
static void undo(const char*in,int n,const int*key,int k,char*out){
  int rows=(n+k-1)/k, full=n%k?n%k:k, lens[128], order[128], start[128];
  for(int i=0;i<k;i++){lens[i]=i<full?rows:rows-1; order[key[i]]=i;}
  int p=0; for(int r=0;r<k;r++){int c=order[r]; start[c]=p; p+=lens[c];}
  int o=0; for(int r=0;r<rows;r++) for(int c=0;c<k;c++) if(r<lens[c]) out[o++]=in[start[c]+r];
}
static char Ibuf[MAXN];
static int score(const int*key,int Lb,int*s2,int*s3){
  char*I=Ibuf; undo(C,n,key,Lb,I); int t2=0,t3=0; static int tt[MAXN]; int nt=0;
  for(int m=0;m+1<n;m++){int x=I[m]*26+I[m+1]; if(cV2[x]<cD2[x]) t2++; cV2[x]++;}
  for(int m=0;m+1<n;m++){int x=I[m]*26+I[m+1]; cV2[x]=0;}
  for(int m=0;m+2<n;m++){int x=(I[m]*26+I[m+1])*26+I[m+2]; if(cV3[x]<cD3[x]) t3++; cV3[x]++; tt[nt++]=x;}
  for(int i=0;i<nt;i++) cV3[tt[i]]=0;
  *s2=t2;*s3=t3; return t2+2*t3; }
int main(int argc,char**argv){
  np=strlen(argv[1]); n=strlen(argv[2]);
  for(int i=0;i<np;i++) P[i]=(argv[1][i]|32)-'a'; for(int i=0;i<n;i++) C[i]=(argv[2][i]|32)-'a';
  int a0=atoi(argv[3]),a1=atoi(argv[4]),b0=atoi(argv[5]),b1=atoi(argv[6]); long steps=atol(argv[7]); int rest=atoi(argv[8]); srand(atoi(argv[9]));
  double thr=argc>10?atof(argv[10]):0.8;
  for(int La=a0;La<=a1;La++){
    memset(cD2,0,sizeof cD2); memset(cD3,0,sizeof cD3);
    for(int i=0;i+La<np;i++) cD2[P[i]*26+P[i+La]]++;
    for(int i=0;i+2*La<np;i++) cD3[(P[i]*26+P[i+La])*26+P[i+2*La]]++;
    int max2=np-La>0?np-La:0, max3=np-2*La>0?np-2*La:0, maxs=max2+2*max3; if(maxs<=0) continue;
    for(int Lb=b0;Lb<=b1;Lb++){
      int best=-1,bk[128],b2=0,b3=0;
      for(int r=0;r<rest;r++){ int k[128]; for(int i=0;i<Lb;i++)k[i]=i; for(int i=Lb-1;i>0;i--){int j=rand()%(i+1);int x=k[i];k[i]=k[j];k[j]=x;}
        int s2,s3; int cur=score(k,Lb,&s2,&s3); if(cur>best){best=cur;memcpy(bk,k,sizeof(int)*Lb);b2=s2;b3=s3;}
        for(long it=0;it<steps;it++){ int i=rand()%Lb,j=rand()%Lb; if(i==j) continue; int t=rand()%3; int sv[128]; memcpy(sv,k,sizeof(int)*Lb);
          if(t==0){int x=k[i];k[i]=k[j];k[j]=x;}
          else if(t==1){ // 読み順を1つ抜いて差し込む（順位で操作）
            int ri=k[i], rj=k[j]; for(int q=0;q<Lb;q++){ if(ri<rj){ if(k[q]>ri&&k[q]<=rj) k[q]--; } else { if(k[q]>=rj&&k[q]<ri) k[q]++; } } k[i]=rj; }
          else { if(i>j){int x=i;i=j;j=x;} int len=1+rand()%3; if(j+len>Lb||i+len>j){ memcpy(k,sv,sizeof(int)*Lb); continue;} for(int q=0;q<len;q++){int x=k[i+q];k[i+q]=k[j+q];k[j+q]=x;} }
          int ns=score(k,Lb,&s2,&s3); double T=3.0*(1.0-(double)it/steps)+0.05;
          if(ns>=cur||exp((ns-cur)/T)>(double)rand()/RAND_MAX){cur=ns; if(cur>best){best=cur;memcpy(bk,k,sizeof(int)*Lb);b2=s2;b3=s3;}}
          else memcpy(k,sv,sizeof(int)*Lb); } }
      printf("%d %d %.3f %d/%d %d/%d",La,Lb,(double)best/maxs,b2,max2,b3,max3);
      if((double)best/maxs>=thr){ int s2,s3; score(bk,Lb,&s2,&s3); printf(" |"); for(int i=0;i<Lb;i++)printf(" %d",bk[i]); printf(" | "); for(int i=0;i<n;i++) putchar('a'+Ibuf[i]); }
      printf("\n"); fflush(stdout); } }
  return 0; }
