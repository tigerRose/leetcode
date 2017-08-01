import sys
import os
import glob

file_template = """

import unittest

class Solution(object):

    def %s(self):
        return -1

class %sTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_%s1(self):
        assert self.s.%s() == 0

    def test_%s2(self):
        assert self.s.%s() == 0

if __name__ == '__main__':
    unittest.main()

"""

def create_dir(name):
    dirs = glob.glob('*.*')
    dirs = [d for d in dirs if os.path.isdir(d)]
    orders = [int(d.split('.')[0]) for d in dirs]
    orders.sort()

    order = orders[-1] + 1

    new_dir = '%03d.%s' % (order, name)
    os.mkdir(new_dir)
    return new_dir

def create_file(d, name):
    new_file = os.path.join(d, "%s.py" % name)

    with open(new_file, 'w') as fh_out:
        fh_out.write(file_template % ((name,)*6))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "python %s <name>" % sys.argv[0]
        sys.exit()

    name = sys.argv[1]
    new_dir = create_dir(name)

    create_file(new_dir, name)
