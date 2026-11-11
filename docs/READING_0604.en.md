# Radio message of 4 June 1940 (frames 0863-0867): key and reading

Added on 11 November 2026. Same system as 17 May (double columnar transposition), with another daily key.

## Material
- Cipher text: NARA RG 242, T405 roll 9, frames 0863-0867 (Funkspruch, five parts of 179, 190, 194, 186 and 204 letters, hand-written; parts 1-4 and part 5 are in different hands). Transcription: `data/ciphertext_0863_0867.txt`.
- Plaintext lead: frame 0862 of the same file (teleprinter message SRO 037, 4 June 1940 11.45, Flugabwehrkommando Schwarzwald Ic to Luftgaukommando VII Ia op 2 and others): Flak units that went into new positions on 3-4 June "to protect army detrainments", with the times at which they were ready to fire.

## Key
```
key A (19)  9 14 17 1 12 6 18 3 16 10 4 8 19 13 7 2 11 15 5
key B (22)  19 22 9 17 1 12 7 16 21 13 10 20 4 18 2 15 6 3 8 11 5 14
```
Decryption: `python3 src/decrypt_0604.py` (plaintext in `data/plaintext_0604.txt`).

## How the key was found
1. Before any decryption, the text of 0862 was rewritten into a candidate radio plaintext with the spelling rules found for 17 May (digits spelled one by one, slash = STRIQ, Roman numerals = ROEM, X around names and numbers): 918 letters (the real text has 928).
2. The tool that searches from the side of the second key (`src/kpb.c`) was run on each of parts 1-4 for all key lengths 8-35. All four parts independently put (19, 22) first (0.56-0.69; the second best is 0.50 or less).
3. Parts 1, 2 and 4 returned the same second key. With it fixed, a hill-climb on German tetragram statistics found the same first key (19) in four out of four restarts.
4. Part 5, not used in the search, decrypts with that key (see "Letter shapes of part 5").

## Reading (letters in bold do not make words)
> Geheime Kommandosache. Zum Schutze von Heeresausladungen gehen in Stellung am 3. Juni 40: II./2./942 von Bahnhof Imme**m**dingen nach Bahnhof Sankt Georgen, seit 19.45 Uhr feuerbereit. II./2./851 von Bodersweier nach Triberg, seit 20.30 Uhr feuerbereit. II./4./251 von Hattingen nach Peterzell, seit 20.45 Uhr feuerbereit. II./10./351 von Ettlingen nach Haslach, seit 20.45 Uhr feuerbereit. I./Leichte Reserve-Flakbatt[r]. 453 von Horb nach Marbach, seit 21.00 Uhr feuerbereit. I./3./851 von Ichenheim nach Bahnhof Hornberg, seit 21.00 Uhr feuerbereit. 4./321 (Eis) von Hüfingen nach Villingen, seit 4. Juni 40 04.35 Uhr feuerbereit. Flugabw.Kdo. Roem. I C[aesar] … Fritz 225/40 g.Kdos.

The enciphered letter string (`GEHEIMEKOMMANDOSAQEXZUMSQUTZEVON…`) is in `data/plaintext_0604.txt`.
- The content agrees with teleprinter message 0862 (whose OCR "19.85" is 19.45 and "Immenddngen" is Immendingen).
- Spelling: dates as DREI X JUNI X VIERNULL (month as a word; on 17 May it was a number), the 10 of II./10./351 as ZEHN, "Le.Res.Flakbatt." as LEIQTE RESERVE FLAKBATT (the R is unexplained), Sankt as SANKT.
- In part 2 there is no X in "ROEM ZWO" (elsewhere ROEM X ZWO). This is not a letter error and is not counted.
- Part 5 ends `ROEM X EINS X CAESAR X NRO X FRITZ X ZWOZWOFUENF X STRIQ X VIERNULL X GKDOS`. What the O of NRO stands for is not known (a slip for Nr. or a form of the abbreviation).

## Figures
| Item | Value |
|---|---|
| Letters of text | 928 (without the five indicator groups) |
| Letters that do not make words | 3 (M of IMMEMDINGEN, U of EIUS in part 2, O of NRO): 925/928 (99.7%) make sense |
| Control (1,000 random keys) | 0 at or above the real keys (trigram hits: real 45, best random 17; tetragram score: real −4.666 per letter, best random −7.125) |
| Part not used for the key | part 5 (199 letters) decrypts directly |
| Agreement with a second reader (OpenAI Codex, gpt-6-astra, reasoning high) | Parts 1-4 (our first transcription, before changes): 177/179, 185/190, 189/194, 180/186 (96.8-98.9%); after the changes 178, 187, 189, 181. Part 5: 173/204 (84.8%) against the transcription with letter shapes fixed by the key, 181/204 (88.7%) against the first transcription before that. The first run on part 5 (31 October 2026, with a prompt that described the letter shapes wrongly) gives 152/204 (74.5%) and 188/204 (92.2%). Whole message (parts 1-4 before changes, part 5 after): 904/953 (94.9%); with the first run on part 5, 883/953 (92.7%) |
| Agreement with the candidate plaintext made from the teleprinter text before decryption | 857/928 (92.3%); the differences are mainly spellings (JUNI, SANKT, ZEHN …) |

Counting: agreement is the number of letters matched between our transcription and Codex's reading, aligned as strings. Where Codex wrote "a/b", the first choice counts. In part 5 both Codex and our first transcription often read x as r, so agreement between the two readers does not mean the letters are right (the first transcription, before the changes, agrees better with Codex).

## Changes to the transcription
- **Parts 1-4**: of the 18 letters where Codex differed, 4 were changed to Codex's reading after looking at the image again (part 1 letter 8 u→n; part 2 letter 65 n→m and letter 182 l→f; part 4 letter 131 q→g; counted from the start of the part, indicator group included, 1-based). The image was looked at by the first reader; no second model judged these. The other 14 stay as first read.
- **Letter shapes of part 5**: this writer makes x like an r with a small flag on top, and r like a looped h. The first transcription read them as r and h, so the decrypted text had R where the word-separator X belongs. Mapping the decrypted letters back to the cipher text changes 47 letters (r→x 26, h→r 10, n→r 5, others 6), all of this kind. The transcription of part 5 therefore **fixed the letter shapes after the key was known** and is not an independent reading. Codex's second run hesitated between r and x at 25 places; with its second choices it has 196/204.

## Prior work
On 11 November 2026 a full-text search of the dbourdeau/cyphersolver ledger (origin/main c95be258d) for Immendingen, Bodersweier, Hornberg, 0867, "Juni 1940" and "4 June 1940" gave no hits. The ledger's flak1940 page lists 4 June as "another key, not read". The plaintext survives in its contemporary form in teleprinter message 0862 of the same file, so no unknown text was read; what is new is the key of the day.

## Human check
No human has compared the transcription or the reading with the images.
