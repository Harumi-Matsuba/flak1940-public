import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
import decrypt


class TestDecrypt(unittest.TestCase):
    def test_keys_are_permutations(self):
        self.assertEqual(sorted(decrypt.KEY_A), list(range(1, 25)))
        self.assertEqual(sorted(decrypt.KEY_B), list(range(1, 29)))

    def test_round_trip(self):
        for name, c in decrypt.bodies():
            self.assertEqual(decrypt.enc(decrypt.dec(c)), c, name)

    def test_lengths(self):
        self.assertEqual([len(c) for _, c in decrypt.bodies()], [174, 173, 162, 125, 200, 189])

    def test_plaintext_words(self):
        pt = dict((n, decrypt.dec(c)) for n, c in decrypt.bodies())
        self.assertTrue(pt['0993 part 1'].startswith('GKDOSXERSTENSKLAMMERFLAKGRUPPEXFRIEDRICHSHAFENXGIBTAN'))
        self.assertIn('DIEBEIDENZUEGEWERDENDURQFLUGABWEHRKOMMANDOXSCHWARZWALD', pt['0993 part 2'])
        self.assertTrue(pt['0993 part 3'].endswith('DIENEUENSTELLUNGEN'))
        self.assertIn('LUFTGAUKOMMANDOXROEMXSIEBENXSTRIQROEMXEINSXANTONXOPXZWO', pt['0993 part 4'])
        self.assertTrue(pt['1025 part 1'].startswith('GEHEIMEKOMMANDOSAQEXAMXEINSSEQSXFUENFXVIERNULL'))
        self.assertIn('WESTLXTUELLINGENXFEUERBEREIT', pt['1027 part 2'])

    def test_plaintext_file(self):
        path = os.path.join(decrypt.DATA, 'plaintext.txt')
        saved = [l.split()[-1] for l in open(path, encoding='utf-8') if l.strip()]
        self.assertEqual(saved, [decrypt.dec(c) for _, c in decrypt.bodies()])

    def test_control(self):
        real, scores = decrypt.control(n=200, seed=1)
        self.assertGreater(real, 2 * max(scores))


if __name__ == '__main__':
    unittest.main()
