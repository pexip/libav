#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path
import os
import stat
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description='Make Nasm executable')
    parser.add_argument('dir', type=Path, help='Source directory')
    args = parser.parse_args()
    os.chmod(args.dir / "nasm", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH | stat.S_IWUSR)
