import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
import decrypt
import decrypt_0604 as d


class TestDecrypt0604(unittest.TestCase):
    def test_keys_are_permutations(self):
        self.assertEqual(sorted(d.KEY_A), list(range(1, 20)))
        self.assertEqual(sorted(d.KEY_B), list(range(1, 23)))

    def test_lengths(self):
        # part lengths from the form headings (179, 190, 194, 186, 204) minus the indicator group
        self.assertEqual([len(c) for _, c in d.bodies()], [174, 185, 189, 181, 199])

    def test_round_trip(self):
        for name, c in d.bodies():
            self.assertEqual(decrypt.enc(decrypt.dec(c, d.KEY_A, d.KEY_B), d.KEY_A, d.KEY_B), c, name)

    def test_plaintext_words(self):
        pt = [decrypt.dec(c, d.KEY_A, d.KEY_B) for _, c in d.bodies()]
        self.assertTrue(pt[0].startswith('GEHEIMEKOMMANDOSAQEXZUMSQUTZEVONHEERESAUSLADUNGEN'))
        self.assertIn('VONXBODERSWEIERXNAQXTRIBERG', pt[1])
        self.assertIn('VONXETTLINGENXNAQXHASLACH', pt[2])
        self.assertIn('VONXICHENHEIMXNAQBAHNHOFXHORNBERG', pt[3])
        self.assertTrue(pt[4].endswith('ZWOZWOFUENFXSTRIQXVIERNULLXGKDOS'))

    def test_plaintext_file(self):
        path = os.path.join(decrypt.DATA, 'plaintext_0604.txt')
        saved = [l.split()[-1] for l in open(path, encoding='utf-8') if l.strip()]
        self.assertEqual(saved, [decrypt.dec(c, d.KEY_A, d.KEY_B) for _, c in d.bodies()])

    def test_control(self):
        real, scores = d.control(n=200, seed=1)
        self.assertGreater(real, 2 * max(scores))


if __name__ == '__main__':
    unittest.main()
