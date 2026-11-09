"""Decrypt the Luftwaffe radio messages of 17 May 1940 (NARA T405 roll 9, frames 0993 and 1025-1027).

System: double columnar transposition. The plaintext is written in rows under key A (24 columns) and read off
column by column in the order of the key numbers; the result is written in rows under key B (28 columns) and read
off the same way. The first five-letter group of each part is the key indicator group and is not part of the text.

Usage (run from the repository root):
    python3 src/decrypt.py            print the plaintext of all six parts
    python3 src/decrypt.py control    compare the real keys with 1000 random keys of the same lengths
"""
import os, random, sys

KEY_A = [15, 12, 20, 8, 17, 4, 22, 9, 19, 2, 16, 11, 5, 21, 10, 3, 14, 24, 7, 13, 1, 6, 18, 23]
KEY_B = [24, 17, 10, 21, 6, 18, 27, 1, 22, 16, 7, 25, 11, 2, 20, 23, 4, 8, 13, 19, 28, 14, 5, 9, 15, 3, 26, 12]
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')


def order(key):
    """Column indices in the order in which the columns are read."""
    return sorted(range(len(key)), key=lambda c: key[c])


def enc1(pt, key):
    k = len(key)
    return ''.join(pt[c::k] for c in order(key))


def dec1(ct, key):
    k, n = len(key), len(ct)
    out, p = [None] * n, 0
    for c in order(key):
        for i in range(c, n, k):
            out[i] = ct[p]
            p += 1
    return ''.join(out)


def enc(pt, a=KEY_A, b=KEY_B):
    return enc1(enc1(pt, a), b)


def dec(ct, a=KEY_A, b=KEY_B):
    return dec1(dec1(ct, b), a)


def load(name):
    """Return the parts of a transcription file as strings (upper case, no spaces)."""
    parts = []
    for line in open(os.path.join(DATA, name), encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('['):
            parts.append('')
        else:
            parts[-1] += ''.join(line.split()).upper()
    return parts


def bodies():
    """Message bodies without the indicator group, with the two repairs to frame 0993, part 3:
    letter 113 is read as T, and lines 2 and 3 (50 letters each) are put back in order."""
    p = load('ciphertext_0993.txt')
    p3 = p[2][:112] + 'T' + p[2][113:]
    p3 = p3[:50] + p3[100:150] + p3[50:100] + p3[150:]
    q = load('ciphertext_1025_1027.txt')
    return [('0993 part 1', p[0][5:]), ('0993 part 2', p[1][5:]), ('0993 part 3', p3[5:]), ('0993 part 4', p[3][5:]),
            ('1025 part 1', q[0][5:]), ('1027 part 2', q[1][5:])]


# Thirty frequent trigrams of ordinary German prose (a general list, not taken from these messages).
TRIGRAMS = ('EIN ICH NDE DIE UND DER CHE END GEN SCH CHT DEN INE NGE NUN UNG DAS HEN IND ENW '
            'ENS IES STE TEN ERE LIC ACH NDI SSE AUS').split()


def german(text):
    """Number of positions at which one of the listed trigrams starts."""
    return sum(text[i:i + 3] in TRIGRAMS for i in range(len(text) - 2))


def control(n=1000, seed=17):
    B = bodies()
    real = sum(german(dec(c)) for _, c in B)
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
            print(name, len(c), dec(c))
