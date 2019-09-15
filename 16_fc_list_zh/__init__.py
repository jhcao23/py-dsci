# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-14'
__product__ = 'PyCharm'
__filename__ = '16_fc_list_zh'

import subprocess
from threading import Timer
import os


def call_fc_list_zh():
    """Cache and list the font filenames known to `fc-list`.
    """
    # Delay the warning by 5s.
    timer = Timer(5, print('wait 5s'))
    timer.start()
    try:
        out = subprocess.check_output(['fc-list', ':lang=zh', '--format=%{file}\\n'])
    except (OSError, subprocess.CalledProcessError):
        return []
    finally:
        timer.cancel()
    return [os.fsdecode(fname) for fname in out.split(b'\n')]
