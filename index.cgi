#!/usr/bin/env python
from wsgiref.handlers import CGIHandler
import os
import sys

me = os.path.dirname(os.path.abspath(__file__))
# Add us to the PYTHONPATH/sys.path if we're not on it
if not me in sys.path:
    sys.path.insert(0, me)

from fastsnotsearch.app import app as application

if __name__ == '__main__':
    CGIHandler().run(application)
