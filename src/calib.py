"""Calibration: turn the decrypted plaintext back into ordinary writing and compare it, as a sequence of letters and
digits, with the contemporary texts in the same file (frame 0993: the recipient's fair copy on frames 0994-0995;
frames 1025-1027: the teleprinter message on frame 1024).
Agreement = (characters matched in order) / (characters of the contemporary text).
The contemporary texts below were read from the frame images by the transcriber of this repository.
Parts 3 and 4 of frame 0993 were used to recover the keys, so only parts 1-2 and frames 1025-1027 are blind.

Usage (from the repository root): python3 src/calib.py [v]
"""
import re, difflib, sys
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import decrypt
NUM={'NULL':'0','EINS':'1','ZWO':'2','DREI':'3','VIER':'4','FUENF':'5','SEQS':'6','SIEBEN':'7','AQT':'8','NEUN':'9'}
ROM={'1':'I','2':'II','3':'III','7':'VII'}
def digits(tok):
    out=''; t=tok
    while t:
        for w,d in NUM.items():
            if t.startswith(w): out+=d; t=t[len(w):]; break
        else: return None
    return out
def normal(pt):
    toks=[t for t in pt.split('X') if t]; out=[]; rom=False
    for t in toks:
        t=t.replace('KLAMMER',' ').replace('DOPPELPUNKT',' ').replace('ERSTENS','1').replace('ZWOTENS','2')
        for part in t.split():
            s=part.replace('STRIQ','/').replace('ROEM','~')
            res=''
            for piece in re.split(r'(/|~)',s):
                if piece=='/': res+=''
                elif piece=='~': rom=True
                else:
                    d=digits(piece)
                    if d is not None and piece: res+=(ROM.get(d,d) if rom else d); rom=False
                    else:
                        res+={'ANTON':'A','CAESAR':'C','FRITZ':'F'}.get(piece,piece); 
                        if piece: rom=False
            out.append(res)
    return ''.join(out).replace('Q','CH')
def letters(s):
    s=s.upper().replace('Ä','AE').replace('Ö','OE').replace('Ü','UE').replace('ß','SS')
    return re.sub(r'[^A-Z0-9]','',s)
REF={
 '0993 parts 1-2 (blind)':"Gkdos. 1.) Flakgruppe Friedrichshafen gibt an Flugabwehrkommando Schwarzwald ab: 1. und 3. Zug der 3. Batterie Res. Lei. Flakabteilung 932 (Herbertingen). Die beiden Züge werden durch Flugabwehrkommando Schwarzwald transportiert und gem. fernmündlicher Besprechung eingesetzt. 2.) Flakgruppe Friedrichshafen",
 '0993 parts 3-4 (used for key recovery)':"setzt 3. Zug Fla. M.G. Res. Komp. 304 (Sigmaringen) beim Schutzobjekt Herbertingen ein. Transport durch Flakgruppe Friedrichshafen. Die neuen Stellungen und Feuerbereitschaft zu melden. Luftgaukommando VII/I a op 2 Nr. 2851/40 gk.",
 '1025-1027 (blind)':"Geheime Kommandosache Am 16.5.40 wurde dem Flugabwehrkommando Schwarzwald der I. Zug 2./932 (2cm) von Flakgruppe Friedrichshafen zugeteilt. Der Zug ist seit 22.30 Uhr in Stellung 3031 westl. Tüllingen feuerbereit. Er ist Abt. 942 unterstellt. Flugabwehrkommando Schwarzwald I c. F 161/40 g.K.",
}
B=dict(decrypt.bodies()); D={k:decrypt.dec(v) for k,v in B.items()}
# The parts end at word boundaries, so an X is put between them when they are joined.
PT={'0993 parts 1-2 (blind)':D['0993 part 1']+'X'+D['0993 part 2'],'0993 parts 3-4 (used for key recovery)':D['0993 part 3']+'X'+D['0993 part 4'],'1025-1027 (blind)':D['1025 part 1']+'X'+D['1027 part 2']}
for k in REF:
    a=letters(REF[k]); b=letters(normal(PT[k]))
    m=sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())
    print('%s: contemporary text %d characters, normalised decryption %d, matched %d = %.1f%%' % (k, len(a), len(b), m, 100*m/len(a)))
    if len(sys.argv)>1: print('   ',a); print('   ',b)
