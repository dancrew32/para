import unittest

import para


def handler(value):
    print(value)


class TestPara(unittest.TestCase):

    def test_by_thread(self):
        para.by_thread(handler, ['one', 'two'], 2)

    def test_by_process(self):
        para.by_process(handler, ['one', 'two'], 2)


if __name__ == '__main__':
    unittest.main()
