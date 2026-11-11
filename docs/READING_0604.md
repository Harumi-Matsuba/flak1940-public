# 1940年6月4日の無線電報（コマ 0863〜0867）：鍵と読み

2026年11月11日に追加。5月17日と同じ方式（二重の列転置）で、その日の鍵が違う。

## 資料
- 暗号文：NARA RG 242、T405 roll 9、コマ 0863〜0867（Funkspruch、5部 179・190・194・186・204字、手書き。1〜4部と5部は書き手が違う）。書き起こしは `data/ciphertext_0863_0867.txt`。
- 平文の手がかり：同じ綴のコマ 0862（印字の電信、SRO 037、6月4日 11:45、Flugabwehrkommando Schwarzwald Ic → Luftgaukommando VII Ia op 2 ほか）。高射砲の各隊が「陸軍の荷下ろしの援護のため」6月3〜4日に新しい陣地に入り、射撃準備を終えた時刻の報告。

## 鍵
```
前の鍵（19）  9 14 17 1 12 6 18 3 16 10 4 8 19 13 7 2 11 15 5
後ろの鍵（22）19 22 9 17 1 12 7 16 21 13 10 20 4 18 2 15 6 3 8 11 5 14
```
復号：`python3 src/decrypt_0604.py`（平文は `data/plaintext_0604.txt`）。

## 鍵の戻し方
1. 0862 の本文を、5月17日に分かった綴りの決まり（数字は1桁ずつ、斜線は STRIQ、ローマ数字は ROEM、名前・数の前後に X）で無線の平文に直した候補を、復号する前に作った（918字。実物は 928字）。
2. 後ろの鍵の側から探す道具（`src/kpb.c`）を、1〜4部それぞれに、鍵の長さ 8〜35 の全組で当てた。4部とも独立に (19, 22) が首位（0.56〜0.69。2位は 0.50 以下）。
3. 1・2・4部が同じ後ろの鍵を返した。それを固定し、前の鍵（19）をドイツ語の4文字統計の山登りで探すと、4回のやり直しとも同じ鍵になった。
4. 5部（鍵探しに使っていない）は、その鍵でそのまま読めた（下の「5部の字形」）。

## 読み（太字は語として通らない字）
> Geheime Kommandosache. Zum Schutze von Heeresausladungen gehen in Stellung am 3. Juni 40: II./2./942 von Bahnhof Im­me**m**dingen nach Bahnhof Sankt Georgen, seit 19.45 Uhr feuerbereit. II./2./851 von Bodersweier nach Triberg, seit 20.30 Uhr feuerbereit. II./4./251 von Hattingen nach Peterzell, seit 20.45 Uhr feuerbereit. II./10./351 von Ettlingen nach Haslach, seit 20.45 Uhr feuerbereit. I./Leichte Reserve-Flakbatt[r]. 453 von Horb nach Marbach, seit 21.00 Uhr feuerbereit. I./3./851 von Ichenheim nach Bahnhof Hornberg, seit 21.00 Uhr feuerbereit. 4./321 (Eis) von Hüfingen nach Villingen, seit 4. Juni 40 04.35 Uhr feuerbereit. Flugabw.Kdo. Roem. I C[aesar] … Fritz 225/40 g.Kdos.

暗号化された文面そのもの（`GEHEIMEKOMMANDOSAQEXZUMSQUTZEVON…`）は `data/plaintext_0604.txt`。
- 0862 の電信と内容が合う。電信の OCR の「19.85」は 19.45、「Immenddngen」は Immendingen。
- 綴り：日付は DREI X JUNI X VIERNULL（月を語で書く。5月17日は数字だった）、II./10./351 の 10 は ZEHN、「Le.Res.Flakbatt.」は LEIQTE RESERVE FLAKBATT（R は不明）、Sankt は SANKT。
- 2部の「ROEM ZWO」の間に X がない（ほかは ROEM X ZWO）。字の誤りではないので数えない。
- 5部の末尾は `ROEM X EINS X CAESAR X NRO X FRITZ X ZWOZWOFUENF X STRIQ X VIERNULL X GKDOS`。NRO の O が何かは分からない（Nr. の誤りか略記の形か）。

## 数字
| 項目 | 値 |
|---|---|
| 本文の字数 | 928（識別の群 5字×5部を除く） |
| 語として通らない字 | 3（IMMEMDINGEN の M、2部 EIUS の U、NRO の O）。意味の通る字 925/928（99.7%） |
| 対照（でたらめな鍵 1,000 組） | 本物以上 0 組（3字組：本物 45、最高 17。4文字統計：本物 −4.666／字、最高 −7.125） |
| 鍵探しに使っていない部分 | 5部（199字）がそのまま読めた |
| 別の読み手（OpenAI Codex、gpt-6-astra、推論 high）との字の一致 | 1〜4部（こちらの1回目、直す前）：177/179、185/190、189/194、180/186（96.8〜98.9%）。直した後は 178・187・189・181。5部：鍵で字形を直した書き起こしと 173/204（84.8%）、直す前の1回目と 181/204（88.7%）。5部の最初の回（2026-10-31、依頼文が字形を誤って説明していた）はそれぞれ 152/204（74.5%）と 188/204（92.2%）。電報全体（直す前の1〜4部＋直した5部）は 904/953（94.9%）、最初の回を使うと 883/953（92.7%） |
| 復号する前に電信から作った平文の候補との字の一致 | 857/928（92.3%）。違いは主に綴り（JUNI・SANKT・ZEHN など） |

数え方：一致は、こちらの書き起こしと Codex の読みを字の並びで突き合わせた数。Codex が「a/b」と迷った字は最初の候補で数えた。5部では、Codex もこちらの1回目も x を r と読んだ所が多く、2人の読みが合っても正しいとは限らない（直す前の方が Codex との一致が高い）。

## 書き起こしの直し
- **1〜4部**：Codex と食い違った 18字のうち、画像を見直して Codex の読みを採った 4字（1部 8字目 u→n、2部 65字目 n→m、182字目 l→f、4部 131字目 q→g。数え方は識別の群を含む部の頭から 1始まり）。見直したのはこちらの読み手で、2つ目のモデルによる判定はしていない。残りの 14字は1回目のまま。
- **5部の字形**：この書き手は、x を上に小さな旗の付いた r のような形で、r を輪のある h のような形で書く。1回目はこれを r・h と読んでいたため、復号した文で区切りの X の位置に R が並んだ。復号した文の字を暗号文に戻すと、直す字は 47（r→x 26、h→r 10、n→r 5、ほか 6）で、どれもこの字形の型に入る。したがって5部の書き起こしは、**鍵を知ってから字形を決めた**もので、独立の読みではない。Codex の2回目は r と x を 25 か所で迷い、その2番目の候補をとると 196/204 になる。

## 先行
2026-11-11、台帳 dbourdeau/cyphersolver（origin/main c95be258d）の全文検索で Immendingen・Bodersweier・Hornberg・0867・「Juni 1940」・「4 June 1940」は 0件。台帳の flak1940 のページは、6月4日を「別の鍵で、読まれていない」としている。平文は同じ綴の電信 0862 に当時の形で残っているので、知られていなかった文面を読んだのではない。新しいのはこの日の鍵。

## 人の確認
人は画像と書き起こし・読みを照らしていない。
