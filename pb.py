#!/usr/bin/python
#  -*- coding: utf-8 -*-
import time
import sys

import sys

def cli_progress_test(end_val, bar_length=20):
    for i in xrange(0, end_val):
        percent = float(i) / end_val
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()

#for i in range(100):
#    time.sleep(1)
#    sys.stdout.write("\r%d%%" % i)
#    sys.stdout.flush()
