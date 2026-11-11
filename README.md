# ドイツ空軍 Flugabwehrkommando Schwarzwald の無線電報（1940年5月17日）：その日の鍵と読み

米国国立公文書館（NARA）RG 242、T405 roll 9 にある、Luftgau VII の高射砲部隊の無線電報（5字群、二重の列転置）のうち、1940年5月17日の2通（6部、本文 1,023字）について、その日の鍵を戻し、全部を復号した記録である。資料は Cyphersolver 台帳の未解読の目録 704 に当たる。

**先行との関係。** 2026年11月10日時点で、`docs/PRIOR_CHECK.md` に挙げた先では、この日の鍵と、この2通の解読は見当たらない。ただし次のことを断っておく。
- **平文は同じ綴に当時の形で残っている**（1通目は受け手の清書、2通目は同じ日の印字の電信）。鍵は、1通目の清書から作った平文を使う既知平文の方法で戻した。知られていなかった文面を読んだのではない。
- 台帳の目録 704 のページは、近くのコマの印字の電信を手がかりに二重転置を解く手順（鍵の長さ 15〜25）を案内している。ここで使ったのは同じ型の方法で、後ろの鍵の長さは 28 だった。
- ここで戻したのは、5月17日の鍵（2つ）、暗号文と平文の字ごとの対応（数字・記号・略語の綴りの決まり）、1通目の3部で2つの行が入れ替わって印字されていること、である。

**状態：全文の読み（2通とも）。** 本文 1,023字のうち、語として通らない字は 7字（0.7%）。

**人は書き起こしを確かめていない。** 書き起こしは AI が画像から行った。別の AI の読みとの一致は、人の確認の代わりにならない。

## 読めたこと

1通目（コマ 0993、Luftgaukommando VII から Flugabwehrkommando Schwarzwald へ、4部）：

> G.Kdos. 1.) Flakgruppe Friedrichshafen gibt an Flugabwehrkommando Schwarzwald ab: 1. und 3. Zug der 3. Batterie Res. Lei. Flakabteilung 932 (Herbertingen). Die beiden Züge werden durch Flugabwehrkommando Schwarzwald transportiert und gem. fernmündlicher Besprechung eingesetzt. 2.) Flakgruppe Friedrichshafen setzt 3. Zug Fla. M.G. Res. Komp. 304 (Sigmaringen) beim Schutzobjekt Herbertingen ein. Transport durch Flakgruppe Friedrichshafen. Die neuen Stellungen und Feuerbereitschaft zu melden. Luftgaukommando VII/Ia op 2 Nr. 2851/40 g.Kdos.

2通目（コマ 1025〜1027、Flugabwehrkommando Schwarzwald Ic の発信、2部）：

> Geheime Kommandosache. Am 16.5.40 wurde dem Flgabw.Kdo. Schwarzwald der I. Zug 2./932 (2 cm) von Flakgruppe Friedrichshafen zugeteilt. Der Zug ist seit 22.30 Uhr in Stellung 3031 westl. Tüllingen feuerbereit. Er ist Abt. 942 unterstellt. Flgabw.Kdo. Schwarzwald Ic Nr. F 161/40 g.Kdos.

暗号化された文面そのもの（`GKDOS X ERSTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X GIBT AN …`）と綴りの決まりは `docs/READING.md`、字の並びは `data/plaintext.txt`。

## 方式と鍵

二重の列転置。平文を幅 24 の格子に行の順に書き、鍵の番号の順に列を読む。それを幅 28 の格子に書き、同じように読む。各部の最初の5字群は鍵の識別の群で、本文に含まない。

```
前の鍵（24）  15 12 20 8 17 4 22 9 19 2 16 11 5 21 10 3 14 24 7 13 1 6 18 23
後ろの鍵（28）24 17 10 21 6 18 27 1 22 16 7 25 11 2 20 23 4 8 13 19 28 14 5 9 15 3 26 12
```

復号：`python3 src/decrypt.py`。テスト：`python3 -m unittest discover -s tests`。

## 数字

| 項目 | 1通目（0993、634字） | 2通目（1025〜1027、389字） |
|---|---|---|
| 語として通る字 | 629（99.2%） | 387（99.5%） |
| 対照（でたらめな鍵 1,000 組。6部まとめて） | 本物以上 0 組（3字組の数：本物 66、最高 19） | 同左 |
| 鍵探しに使っていない部分 | 1・2部（347字）がそのまま読めた。3部は入れ替わった2行を戻すと読めた | 全部（平文を見ずに復号した） |
| 別の読み手（OpenAI Codex）との一致 | 99.1%（最初の版）、99.2%（見直した版） | 93.8%（復号する前の版）、95.4%（復号の後に 7字を直した版） |
| 較正（当時の文との字の一致） | 98.8%（1・2部と清書） | 91.1%（印字の電信と） |
| 画像での判定（そろった字の抜き取り 80。Codex・Sonnet が1回目の読みを選んだ数） | 80・80（仕込み 10 は 10・10） | 80・76（仕込み 10 は 8・8） |

数え方と断り書きは `docs/METHOD.md`。

## 1940年6月4日の電報（2026年11月11日に追加）

同じリールのコマ 0863〜0867（Flugabwehrkommando Schwarzwald の発信、5部、本文 928字）も、その日の鍵（前 19・後ろ 22）で全部を復号した。平文は同じ綴の印字の電信（コマ 0862）に当時の形で残っており、鍵はそれを使う既知平文の方法で戻した。新しいのはこの日の鍵である。

> Zum Schutze von Heeresausladungen gehen in Stellung am 3. Juni 40: II./2./942 von Bahnhof Immendingen nach Bahnhof Sankt Georgen, seit 19.45 Uhr feuerbereit. … 4./321 (Eis) von Hüfingen nach Villingen, seit 4. Juni 40 04.35 Uhr feuerbereit.

| 項目 | 値 |
|---|---|
| 語として通る字 | 925/928（99.7%） |
| 対照（でたらめな鍵 1,000 組） | 本物以上 0 組 |
| 鍵探しに使っていない部分 | 5部（199字）がそのまま読めた |
| 別の読み手（Codex）との一致 | 電報全体 94.9%（5部の古い回を使うと 92.7%）。1〜4部 96.8〜98.9%、5部 74.5〜84.8% |

**断り書き：** 5部は書き手の字形が特殊で（x を旗の付いた r の形、r を輪のある h の形で書く）、こちらの書き起こしは鍵を知ってから字形を決めた。5部の書き起こしは独立の読みではない。詳しくは `docs/READING_0604.md`、復号は `python3 src/decrypt_0604.py`。

## AI の使用

書き起こし・平文の当てはめ・鍵探し・復号・文書は Claude Fable 5.1（Anthropic）。2回目の書き起こしと画像での判定は OpenAI Codex（gpt-6-astra）と Claude Sonnet。6月4日の電報（2026-11-11 追加）の書き起こし・平文の候補・鍵探し・復号・文書は Claude Opus 5.5、2回目の書き起こしは OpenAI Codex（gpt-6-astra）。人が行ったのは、作業の指示と公開の判断である。人は画像と書き起こし・読みを照らしていない。

## ファイル

- `data/`：書き起こし（`ciphertext_0993.txt`、`ciphertext_1025_1027.txt`、復号する前の版、6月4日の `ciphertext_0863_0867.txt`）、鍵（`key.txt`、`key_0604.txt`）、平文（`plaintext.txt`、`plaintext_0604.txt`）
- `src/`：復号と対照（`decrypt.py`）、較正（`calib.py`）、鍵探しの道具（`kpa.c`、`kpb.c`）
- `second/`：2回目の書き起こしの依頼文と結果、画像での判定の問いと答え
- `docs/`：方法（METHOD）、読み（READING）、未解決（OPEN）、先行の確かめ（PRIOR_CHECK）
- `SOURCES.md`：資料とコマ番号。画像はこのリポジトリに入れていない

## 更新履歴

- 2026-11-11：1940年6月4日の電報（コマ 0863〜0867）の鍵と読みを追加（`docs/READING_0604.md`）。5月17日の鍵と読みは変えていない。

## ライセンス

コードは MIT、自作の文書とデータは CC BY 4.0（`LICENSE`）。
