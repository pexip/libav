#!/usr/bin/env python3
# Copyright (c) 2022 L. E. Segovia <amy@amyspark.me>
#
# This file is part of the FFmpeg Meson build
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.

import argparse
import pathlib
import os
import re
import subprocess
import tempfile

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Craft the Windows exports file')

    arg_parser.add_argument('vscript', metavar='VERSION_SCRIPT',
                            type=argparse.FileType('r'), help='Version script')
    arg_parser.add_argument('--prefix', metavar='PREFIX',
                            help='Prefix for extern symbols')
    arg_parser.add_argument('--nm', metavar='NM_PATH', type=pathlib.Path,
                            help='If specified, runs this instead of dumpbin (MinGW)')
    arg_parser.add_argument('--dumpbin', metavar='DUMPBIN_PATH', type=pathlib.Path,
                            help='If specified, runs this instead of nm (MSVC)')
    arg_parser.add_argument('libname', metavar='FILE', type=pathlib.Path,
                            help='Library to parse')

    args = arg_parser.parse_args()

    libname = args.libname

    if not libname.exists():
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), libname)

    prefix = args.prefix or ''
    started = 0
    regex = []

    for line in args.vscript:
        # We only care about global symbols
        if re.match(r'^\s+global:', line):
            started = 1
            line = re.sub(r'^\s+global: *', '', line)
        else:
            if re.match('^\s+local:', line):
                started = 0

        if started == 0:
            continue

        line = line.replace(';', '')

        for exp in line.split():
            # Remove leading and trailing whitespace
            regex.append(exp.strip())

    if args.nm is not None:
        # Use eval, since NM="nm -g"
        s = subprocess.run([args.nm, '--defined-only',
                            '-g', libname], capture_output=True, text=True, check=True)
        dump = s.stdout.splitlines()
        # Exclude lines with ':' (object name)
        dump = [x for x in dump if ":" not in x]
        # Exclude blank lines
        dump = [x for x in dump if len(x) > 0]
        # Take only the third field (split by spaces)
        dump = [x.split()[2] for x in dump]
        # Subst the prefix out
        dump = [x.replace(prefix, '') for x in dump]

    else:
        dump = subprocess.run([args.dumpbin, '-linkermember:1', libname],
                              capture_output=True, text=True).stdout.splitlines()
        # Find the index of the first line with
        # "public symbols", keep the rest
        # Then the line with " Summary",
        # delete it and the rest
        for i, line in enumerate(dump):
            if 'public symbols' in line:
                start = i
            elif re.match(r'\s+Summary', line):
                end = i
        dump = dump[start:end]
        # Substitute prefix out
        dump = [re.sub(f'\s+{prefix}', ' ', x) for x in dump]
        # Substitute big chonky spaces out
        dump = [re.sub(f'\s+', ' ', x) for x in dump]
        # Exclude blank lines
        dump = [x for x in dump if len(x) > 0]
        # Take only the *second* field (split by spaces)
        # Python's split excludes whitespace at the beginning
        dump = [x.split()[1] for x in dump]

    list = []
    for exp in regex:
        for i in dump:
            if re.match(f'^{exp}', i):
                list.append(f'    {i}')

    print("EXPORTS")
    print("\n".join(sorted(set(list))))
