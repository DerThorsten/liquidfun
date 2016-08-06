#!/usr/bin/env python
from __future__ import print_function
import sys
sys.path.append('.')

from example import foo


import numpy

data = numpy.arange(10).astype('float32')
print(data)
foo(data)
