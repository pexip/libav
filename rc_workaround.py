#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
from pathlib import Path
import os
import re

if __name__ == '__main__':
    parser = ArgumentParser(description='Patch .rc file to work around RC include precedences')
    parser.add_argument('input', type=Path, help='Input file to patch')
    parser.add_argument('build_folder', type=Path, help='Build folder')

    args = parser.parse_args()

    base_folder: Path = args.input.parent

    build_folder: Path = args.build_folder

    common_root = os.path.relpath(build_folder, base_folder)

    relative_path = Path(common_root).as_posix()

    with args.input.open('r', encoding='utf-8') as f:
        for line in f.readlines():
            if re.match('^#include "config.h"', line):
                # use <folder of the input>/../.../config.h
                print(f'#include "{relative_path}/config.h"')
            else:
                print(line.strip())
