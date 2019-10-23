import unittest
from unittest import mock

import para


def handler(value):
    return f'{value}_yay'


def callback(result):
    print(result)


class TestPara(unittest.TestCase):

    @mock.patch('__main__.callback')
    def test_by_thread(self, cb):
        para.by_thread(handler, ['one', 'two'], callback, workers=2)
        self.assertEqual(2, cb.call_count)

    @mock.patch('__main__.callback')
    def test_by_process(self, cb):
        para.by_process(handler, ['one', 'two', 'three'], callback, workers=2)
        self.assertEqual(3, cb.call_count)


if __name__ == '__main__':
    unittest.main()
