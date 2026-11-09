# 読み

暗号文を鍵で戻した字の並びは `data/plaintext.txt`。ここでは、語に分けたものと、普通の書き方に戻したものを並べる。
X は区切り、Q は CH。太字は平文として崩れている字（暗号文のその字がそうなっている）。

## コマ 0993（Luftgaukommando VII → Flugabwehrkommando Schwarzwald、1940年5月17日、4部）

1. `GKDOS X ERSTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X GIBT AN FLUGABWEHRKOMMANDO X SCHWARZWALD X AB DOPPELPUNKT X EINS X UND X DREI X ZUG DER X DREI X BAT`**`B`**`ERIE X RES X LEI X FLAKABTEILUNG X NEUNDREIZWO X KLAMMER`
2. `X HERBERTINGEN X KLAMMER X DIE BEIDEN ZUEGE WERDEN DURQ FLUGABWEHRKOMMANDO X SCHWARZWALD X TRANSPORTI`**`W`**`RT UND GEM X FERN`**`N`**`UENDLIQER BESPREQUNG EINGESETZT X ZWOTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X`
3. `SETZT X DREI X ZUG FLA X M X G X RES X KOMP X DREINULLVIER X KLAMMER X SIGMARINGEN X KLAMMER BEIM SQUTZOBJEKT X HERBERTINGEN X EIN X TRANSPORT DURQ FLAKGRUPPE X FRIEDRICHSHAFEN X DIE NEUEN STELLUNGEN`
4. `UND FEUERBEREITS`**`X`**`AFT ZU MELDEN X LUFTGAUKOMMANDO X ROEM X SIEBEN X STRIQ ROEM X EINS X ANTON X OP X ZWO X NR X ZWOAQTFUENFEINS X STRIQ X VIERNULL X G X KDOS `**`Q`**

普通の書き方に戻すと：

> G.Kdos. 1.) Flakgruppe Friedrichshafen gibt an Flugabwehrkommando Schwarzwald ab: 1. und 3. Zug der 3. Batterie Res. Lei. Flakabteilung 932 (Herbertingen). Die beiden Züge werden durch Flugabwehrkommando Schwarzwald transportiert und gem. fernmündlicher Besprechung eingesetzt. 2.) Flakgruppe Friedrichshafen setzt 3. Zug Fla. M.G. Res. Komp. 304 (Sigmaringen) beim Schutzobjekt Herbertingen ein. Transport durch Flakgruppe Friedrichshafen. Die neuen Stellungen und Feuerbereitschaft zu melden. Luftgaukommando VII/Ia op 2 Nr. 2851/40 g.Kdos.

これは受け手の清書（コマ 0994・0995）と同じ内容である。

## コマ 1025〜1027（Flugabwehrkommando Schwarzwald Ic 発、1940年5月17日、2部）

1. `GEHEIME KOMMANDOSAQE X AM X EINSSEQS X FUENF X VIERNULL X WURDE DEM X FLGABW X KDO X SCHWARZWALD DER X ROEM X EINS X ZUG X ZWO X STRIQ X NEUNDREIZWO X KLAMMER X ZWO X CENTIMETER KLAMMER VON FLAKGRUPPE X FRIEDRICHSHAFEN X ZUGETEILT X DER ZUG IST SEIT`
2. `ZWOZWODREINULL X UHR IN STELLUNG X DREINULLDREIEINS X WESTL X TUELLINGEN X FEUERBEREIT X ER IST ABT X NEUNVIERZWO X UNTERSTELLT X FLGABWKDO X SCHWARZWALD X ROEM X EINS X CAESAR X NR X FRITZ X EINSSEQSEINS X STRIQ X VIE`**`E`**`NULL X G`**`H`**`DOS`

普通の書き方に戻すと：

> Geheime Kommandosache. Am 16.5.40 wurde dem Flgabw.Kdo. Schwarzwald der I. Zug 2./932 (2 cm) von Flakgruppe Friedrichshafen zugeteilt. Der Zug ist seit 22.30 Uhr in Stellung 3031 westl. Tüllingen feuerbereit. Er ist Abt. 942 unterstellt. Flgabw.Kdo. Schwarzwald Ic Nr. F 161/40 g.Kdos.

これは同じ日の印字の電信（コマ 1024）と同じ内容である。

## 綴りの決まり（この2通で見えたもの）

- 語の区切りは X。名前・数・略語の前後に入り、ふつうの語の並びは続けて書く（`DIEBEIDENZUEGEWERDEN`）。
- CH は Q（`DURQ`、`SQUTZOBJEKT`、`STRIQ`）。名前は CH のまま（`FRIEDRICHSHAFEN`、`SCHWARZWALD`）。
- 数字は1桁ずつ綴り、続けて書く（`NEUNDREIZWO`＝932、`ZWOAQTFUENFEINS`＝2851）。2 は ZWO。
- 「1.)」「2.)」は `ERSTENS KLAMMER`、`ZWOTENS KLAMMER`。括弧は `KLAMMER`、「:」は `DOPPELPUNKT`、「/」は `STRIQ`。
- ローマ数字は `ROEM` を前に置く（`ROEM SIEBEN`＝VII、`ROEM EINS`＝I）。1字だけの字は名前で綴る（`ANTON`＝a、`CAESAR`＝c、`FRITZ`＝F）。
- 各部の最初の5字群は鍵の識別の群で、本文に含まない。部は語の切れ目で切ってある。

## 崩れている字（7字／1,023字）

| 場所 | 平文 | 暗号文の字 | 見立て |
|---|---|---|---|
| 0993 1部 | BAT**B**ERIE | 8字目（TE**B**DA） | 印字は B。T の誤り |
| 0993 2部 | TRANSPORTI**W**RT | 49字目（EXW**W**U） | 印字は W。E の誤り |
| 0993 2部 | FERN**N**UENDLIQER | 18字目（RN**N**RA） | 印字は N。M の誤り |
| 0993 4部 | FEUERBEREITS**X**AFT と末尾の **Q** | 32字目（M**X**NLB）と 30字目（MLEF**Q**） | 2つの字を入れ替えると SQAFT と、末尾の X になる |
| 1027 | VIE**E**NULL | 137字目（R**E**TEZ） | 手書きは e。R の誤り |
| 1027 | G**H**DOS | 194字目（IZN**H**） | 手書きの h と k は形が近い。K かもしれない |

0993 の5字は、印字の暗号文を拡大して確かめてもその字である。発信側が暗号化するとき、または中継のときの誤りとみる（確かめる材料はない）。
