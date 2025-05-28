import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from __class__ import *
from data import Al, A
from base import *

print(A)
print(Result)