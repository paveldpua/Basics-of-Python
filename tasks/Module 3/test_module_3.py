"""Test all we can in Module 3."""
import unittest
import task_2


class TestModule2(unittest.TestCase):
    """TestCase  class."""
    def test_my_split(self):
        """test my_split finction from module task_2."""
        self.assertEqual(task_2.my_split("Python is cool", " "), ['Python', 'is', 'cool'])
        self.assertEqual(task_2.my_split(",,,,", ','), ['', '', '', '', ''])
        self.assertEqual(task_2.my_split("Python", "Javascript"), ['Python'])
        self.assertEqual(task_2.my_split('my brother broght brokoli bro', 'bro'),
                         ['my ', 'ther ', 'ght ', 'koli ', ''])
        with self.assertRaises(TypeError):
            task_2.my_split("Python is cool", None)
            task_2.my_split("Python is cool")

if __name__ == '__main__':
    unittest.main()
