
import sys
import time
import math


class ProgressBar(object):
    """
    Display a progress bar in the shell
    """

    def __init__(self, width=78, max_value=100):
        """
        :param width:      Width of progress bar in characters
        :param max_value:  Value (int or float) that means 100% complete
        """
        self.width = width
        max_value = 100
        self.steps = self.width / (max_value * 1.0)
        line=""

    def bump(self, value):
        progress = int(math.ceil(value * self.steps))
        remaining = int(self.width - progress)
        line = "[%s>%s]" % (progress * '=', remaining * ' ',)
        print "\r" + line,
        sys.stdout.flush()


if __name__ == '__main__':
    max_value=100
    pb = ProgressBar(max_value=max_value)
    for value in range(max_value + 1):
        pb.bump(value)
        time.sleep(0.01)
