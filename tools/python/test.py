#!/usr/bin/python3

import os

for item, value in os.environ.items():
    print('{}: {}'.format(item, value))
