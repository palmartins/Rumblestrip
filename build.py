#!/usr/bin/python3

import os
import sys
from subprocess import call

def cmake(*arguments):
    """Runs a cmake command directly in os. Exits in case of error."""

    ret_code = call(['cmake'] + list(arguments))

    if ret_code != 0:
        sys.exit(ret_code)


def get_generator() -> str:
    """Returns cmake generator based on platform."""

    if sys.platform == 'linux' or sys.platform == 'linux2':
        return 'Unix Makefiles'
    if sys.platform == 'win32':
        return 'Visual Studio 16 2019'
    if sys.platform == 'darwin':
        return 'Xcode'
    sys.exit('Unknown platform')

cmake(
    '-B', 'build', '-G', get_generator()
)

cmake(
    '--build',  'build'
)

sys.exit(0)
