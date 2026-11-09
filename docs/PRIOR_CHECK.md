# 先行の確かめ（2026年11月10日）

この日（1940年5月17日）の鍵と、コマ 0993・1025〜1027 の解読が既に出ていないかを探した。探したのは、読みを作った読み手と、それを見ていない別の読み手（Claude Sonnet。否定するつもりで探すよう指示した）の2者である。

**結果：下の先では見当たらない。** 見つからないことは、存在しないことの証拠ではない。

断っておくこと：
- **平文は同じ綴に当時の形で残っている**（0993 は受け手の清書 0994・0995、1025〜1027 は印字の電信 1024）。ここで戻したのは、その日の鍵と、暗号文と平文の字ごとの対応である。
- 台帳の目録 704 のページ自身が、近くのコマの印字の電信を手がかりにして二重転置を解く手順（鍵の長さ 15〜25）を案内している。ここで使ったのは同じ型の方法である（後ろの鍵の長さは 28 で、その案内の範囲の外だった）。
- 読んだ電報は、台帳の目録 704 が挙げるコマの範囲（964〜1003、1025〜1056）に入っている。

| 先 | 見た版・日付 | 語 | 結果 |
|---|---|---|---|
| Cyphersolver 台帳（git、全体を検索） | origin/main 180c8b295（2026-11-09 16:46 UTC） | T405、Flugabwehrkommando、Luftgauschl、332033680、Doppelw、Luftgau、Flak、double transposition、Würfel、roll 9、0993、1025、0863、Funkspruch、Schwarzwald、Luftwaffe | 目録 704 の記載と 1939年の再現だけ。1940年の電報の作業フォルダ・解読なし |
| 台帳の issue・プルリクエスト | 全 361 件を本文ごと（2026-11-10） | T405、Flugabwehr、Luftgau、332033680、704、Schwarzwald | 該当なし（当たった2件は別の数字「0.704」「704 of 1024」） |
| 台帳の公開ページ | cyphersolver.com/solve/704.html（Last-Modified 2026-11-09） | — | 「open」 |
| Cryptiana（友清理士） | code/unsolved.htm（2026-11-05）、code/ai.htm（2026-10-19）、ブログの feed 300 件（2026-11-09 更新） | T405、Luftgau、Flugabwehr、Flak、Doppelw、Luftwaffe、double transposition、Funkspruch、1940 | 該当なし |
| Cryptoole | idx.json 全 2,086 件（2026-11-06） | 同上 | 台帳の写し（cyphersolver:704、open）だけ |
| Klaus Schmeh のブログ | 検索ページ2枚（Luftwaffe、Doppelwürfel。2026-11-10） | — | Luftgau・Flak・T405 の記事なし |
| GitHub | リポジトリ検索 9 語、コード検索（語 4 つ、この分野の利用者 6 人のリポジトリ） | "Flugabwehrkommando Schwarzwald"、Luftgauschluessel、T405 ほか | 台帳自身のファイルだけ |
| ウェブ検索 | 独語・英語で 6 回 | Luftgauschlüssel、Doppelwürfel Luftwaffe 1940、T405 roll 9、Flugabwehrkommando Schwarzwald ほか | 該当なし |

調べていない・読めなかった先：cryptocellar.org のサイト内（検索が効かなかった）、George Lasry の二重転置の論文の本文、Bundesarchiv の同じ部隊の文書とその刊本、DECODE、Google Books、Internet Archive の全文。
