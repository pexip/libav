#!/usr/bin/env python3

# Copyright (c) 2018 Mathieu Duponchelle <mathieu@centricular.com>
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
import re

def list_components(infile, full):
    things = []

    for line in infile:
        if not full:
            matches = re.match(
                r'^[^#]*extern AVFilter\s*ff_[^_]*_(.*);', line.strip())
        else:
            matches = re.match(r'^[^#]*extern AVFilter\s*ff_(.*_.*);', line.strip())
        if (matches):
            if not args.full:
                things.append(('%s_filter' % matches.group(1).strip()))
            else:
                things.append(matches.group(1).strip())

    return things

def update_meson_options(options):
    has_generated = False
    lines = []
    with open('meson_options.txt', 'r', encoding='utf8') as meson_file:
        opening = '#### --- GENERATED FILTER OPTIONS --- ####\n'
        closing = opening.replace('GENERATED', 'END GENERATED')
        for l in meson_file.readlines():
            if l == opening:
                has_generated = True
                lines.append(l)
                for option in options:
                    if re.match(f'^null(.*)_filter', option):
                        value = 'enabled'
                    else:
                        value = 'auto'
                    lines.append(
                        ('option(\'%s\', type: \'feature\', value: \'%s\')\n' % (option, value)))
                lines.append(
                    "option('filters', type: 'feature', value: 'auto', description: 'Enable or disable all filters')\n")
            elif l == closing:
                lines.append(l)
                has_generated = False
            elif not has_generated:
                lines.append(l)

    with open('meson_options.txt', 'w') as meson_file:
        meson_file.write(''.join(lines))

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Find filter registrations in allfilters.c')

    arg_parser.add_argument('--update-options', action='store_true',
                            help='update the Meson options list and exit')
    arg_parser.add_argument('--full', action='store_true')
    arg_parser.add_argument('files', metavar='FILE', nargs='*',
                            type=argparse.FileType('r'),
                            help='File with lists of declarations, ' +
                            'or "-" for standard input')

    args = arg_parser.parse_args()

    things = []

    if args.update_options:
        options = {}
        with open('libavfilter/allfilters.c', 'r', encoding='utf-8') as infile:
                components = list_components(
                    infile, False)
                options = components

        update_meson_options(options)
    else:
        things = []
        for infile in args.files:
            things += list_components(infile, args.full)

        print('\n'.join(things))
