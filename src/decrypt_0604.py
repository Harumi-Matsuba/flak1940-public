"""Decrypt the Luftwaffe radio message of 4 June 1940 (NARA T405 roll 9, frames 0863-0867, five parts).

Same system as 17 May 1940 (see decrypt.py), with the key of 4 June: key A has 19 columns, key B 22.
The first five-letter group of each part is the key indicator group and is not part of the text.

Usage (run from the repository root):
    python3 src/decrypt_0604.py            print the plaintext of the five parts
    python3 src/decrypt_0604.py control    compare the real keys with 1000 random keys of the same lengths
"""
import random, sys
from decrypt import dec, enc, load, german

KEY_A = [9, 14, 17, 1, 12, 6, 18, 3, 16, 10, 4, 8, 19, 13, 7, 2, 11, 15, 5]
KEY_B = [19, 22, 9, 17, 1, 12, 7, 16, 21, 13, 10, 20, 4, 18, 2, 15, 6, 3, 8, 11, 5, 14]


def bodies():
    return [('0863-0867 part %d' % (i + 1), p[5:]) for i, p in enumerate(load('ciphertext_0863_0867.txt'))]


def control(n=1000, seed=17):
    B = bodies()
    real = sum(german(dec(c, KEY_A, KEY_B)) for _, c in B)
    rnd = random.Random(seed)
    scores = []
    for _ in range(n):
        a, b = KEY_A[:], KEY_B[:]
        rnd.shuffle(a)
        rnd.shuffle(b)
        scores.append(sum(german(dec(c, a, b)) for _, c in B))
    return real, scores


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        real, scores = control()
        print('real keys: %d trigram hits; 1000 random keys: max %d, mean %.1f; random >= real: %d'
              % (real, max(scores), sum(scores) / len(scores), sum(s >= real for s in scores)))
    else:
        for name, c in bodies():
            print(name, len(c), dec(c, KEY_A, KEY_B))
