import random
import unittest

from textflint.input.component.sample import UTCnSample
from textflint.generation.transformation.UTCN import CnSpellingError

sample = UTCnSample({
    'x': '我接受了她的礼物。',
    'y': 1,
})
trans_method = CnSpellingError(get_pos=True)


class TestSpellingError(unittest.TestCase):
    def test_transformation(self):
        special_sample = UTCnSample({'x': '', 'y': "negative"})
        self.assertEqual([], trans_method.transform(special_sample))

        special_sample = UTCnSample({'x': '~!@#$%^7890"\'', 'y': "negative"})
        self.assertEqual([], trans_method.transform(special_sample))

        random.seed(100)
        # test if the item change
        change_sample = trans_method.transform(sample)
        self.assertEqual(1, len(change_sample))
        for s in change_sample:
            self.assertEqual(sample.get_tokens('x')[:1], s.get_tokens('x')[:1])
            self.assertEqual(sample.get_tokens('x')[-6:], s.get_tokens('x')[-6:])

        self.assertEqual(change_sample[0].get_value('x'), '我加收了她的礼物。')


if __name__ == "__main__":
    unittest.main()
