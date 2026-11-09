/* Known-plaintext attack on a double columnar transposition, first-key side: finds the reading order of the columns of the first key (width La) by simulated annealing. Pairs and triples of letters Lb apart in the intermediate text stand in one column of the second grid, so they must occur as adjacent letters of the ciphertext, whatever the second key is. Needs the plaintext with every letter in its exact position.
   Build: clang -O2 -o kpa kpa.c -lm    (original comments below are in Japanese) */
// 二重の列転置の既知平文攻撃。平文 P と暗号文 C（同じ長さ）から、前の鍵（幅 La の列の読み順）を焼きなましで探す。
// 点：中間の文 I（P の櫛を鍵の順に並べたもの）で Lb 字離れた字の組・3字組は、後ろの格子の同じ列で上下に並ぶので、
//     暗号文の隣り合う字の組・3字組に必ず現れる（後ろの鍵の順には関係しない）。重複込みの共通部分の大きさを点にする。
// 使い方: kpa P C LaMin LaMax LbMin LbMax 歩数 やり直し 種 [詳細を出す下限の割合(0-1)]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 512
int n; char P[MAXN],C[MAXN]; int cA2[676]; int cA3[17576]; int cV2[676]; int cV3[17576];
static int build(const int*ord,int La,char*I){ int o=0; for(int k=0;k<La;k++){int c=ord[k]; for(int i=c;i<n;i+=La) I[o++]=P[i];} return o; }
static int score(const int*ord,int La,int Lb,int*s2,int*s3){
  static char I[MAXN]; build(ord,La,I); int t2=0,t3=0; static int touched3[MAXN]; int nt=0;
  for(int m=0;m+Lb<n;m++){int x=I[m]*26+I[m+Lb]; if(cV2[x]<cA2[x]) t2++; cV2[x]++;}
  for(int m=0;m+Lb<n;m++){int x=I[m]*26+I[m+Lb]; cV2[x]=0;}
  for(int m=0;m+2*Lb<n;m++){int x=(I[m]*26+I[m+Lb])*26+I[m+2*Lb]; if(cV3[x]<cA3[x]) t3++; cV3[x]++; touched3[nt++]=x;}
  for(int i=0;i<nt;i++) cV3[touched3[i]]=0;
  *s2=t2; *s3=t3; return t2+2*t3; }
int main(int argc,char**argv){
  n=strlen(argv[1]); if((int)strlen(argv[2])!=n){fprintf(stderr,"長さが違う %d %d\n",n,(int)strlen(argv[2])); return 1;}
  for(int i=0;i<n;i++){P[i]=(argv[1][i]|32)-'a'; C[i]=(argv[2][i]|32)-'a';}
  for(int i=0;i+1<n;i++) cA2[C[i]*26+C[i+1]]++;
  for(int i=0;i+2<n;i++) cA3[(C[i]*26+C[i+1])*26+C[i+2]]++;
  int a0=atoi(argv[3]),a1=atoi(argv[4]),b0=atoi(argv[5]),b1=atoi(argv[6]); long steps=atol(argv[7]); int rest=atoi(argv[8]); srand(atoi(argv[9]));
  double thr=argc>10?atof(argv[10]):0.9;
  for(int La=a0;La<=a1;La++) for(int Lb=b0;Lb<=b1;Lb++){
    int max2=n-Lb>0?n-Lb:0, max3=n-2*Lb>0?n-2*Lb:0, maxs=max2+2*max3; if(maxs<=0) continue;
    int best=-1,bo[128],b2=0,b3=0;
    for(int r=0;r<rest;r++){ int o[128]; for(int i=0;i<La;i++)o[i]=i; for(int i=La-1;i>0;i--){int j=rand()%(i+1);int x=o[i];o[i]=o[j];o[j]=x;}
      int s2,s3; int cur=score(o,La,Lb,&s2,&s3); if(cur>best){best=cur;memcpy(bo,o,sizeof(int)*La);b2=s2;b3=s3;}
      for(long it=0;it<steps;it++){ int i=rand()%La,j=rand()%La; if(i==j) continue; int t=rand()%3; int sv[128]; memcpy(sv,o,sizeof(int)*La);
        if(t==0){int x=o[i];o[i]=o[j];o[j]=x;}
        else if(t==1){int x=o[i]; if(i<j){for(int q=i;q<j;q++)o[q]=o[q+1];} else {for(int q=i;q>j;q--)o[q]=o[q-1];} o[j]=x;}
        else { if(i>j){int x=i;i=j;j=x;} int len=1+rand()%3; if(j+len>La||i+len>j){ memcpy(o,sv,sizeof(int)*La); continue;} for(int q=0;q<len;q++){int x=o[i+q];o[i+q]=o[j+q];o[j+q]=x;} }
        int ns=score(o,La,Lb,&s2,&s3); double T=3.0*(1.0-(double)it/steps)+0.05;
        if(ns>=cur||exp((ns-cur)/T)>(double)rand()/RAND_MAX){cur=ns; if(cur>best){best=cur;memcpy(bo,o,sizeof(int)*La);b2=s2;b3=s3;}}
        else memcpy(o,sv,sizeof(int)*La);
        if(best==maxs) break; }
      if(best==maxs) break; }
    printf("%d %d %.3f %d/%d %d/%d",La,Lb,(double)best/maxs,b2,max2,b3,max3);
    if((double)best/maxs>=thr){ printf(" |"); for(int i=0;i<La;i++)printf(" %d",bo[i]); }
    printf("\n"); fflush(stdout); }
  return 0; }
