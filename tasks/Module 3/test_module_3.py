"""Test all we can in Module 3."""
import unittest
import task_2


class TestModule2(unittest.TestCase):
    """TestCase  class."""

    def test_my_split(self):
        """Test my_split finction from module task_2."""
        self.assertEqual(task_2.my_split("Python is cool", " "),
                         "Python is cool".split(' '))
        self.assertEqual(task_2.my_split(",,,,", ','),
                         ",,,,".split(','))
        self.assertEqual(task_2.my_split("trololo", 'trololo'),
                         'trololo'.split('trololo'))
        self.assertEqual(task_2.my_split("Python", "Javascript"),
                         "Python".split("Javascript"))
        self.assertEqual(task_2.my_split(
                        'my brother broght brokoli bro', 'bro'),
                         'my brother broght brokoli bro'.split('bro'))
        with self.assertRaises(ValueError):
            task_2.my_split("Python is cool", '')


if __name__ == '__main__':
    unittest.main()
