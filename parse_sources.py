# Copyright (c) 2018 Mathieu Duponchelle <mathieu@centricular.com>
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


import re
import os
import sys
from pprint import pprint
from collections import defaultdict

source_maps = {
  'c': defaultdict(list),
  'asm': defaultdict(list),
  'test-prog': defaultdict(list),
  'mmx': defaultdict(list),
}

with open('%s/Makefile' % sys.argv[1], 'r') as f:
    accum = []
    accumulate = False
    optional = False
    source_type = None

    for l in f.readlines():
        l = l.strip()
        l = l.rsplit('#', 1)[0]

        if accumulate:
            ofiles = l
        elif re.match('OBJS-.*CONFIG.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('CONFIG_')[1].rstrip(' )')
            source_type = 'c' # arguable ^^
        elif re.match('OBJS.*=.*', l):
            label = ''
            ofiles = l.split('=')[1]
            source_type = 'c'
        elif re.match('X86ASM-OBJS-.*CONFIG.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('CONFIG_')[1].rstrip(' )')
            source_type = 'asm'
        elif re.match('X86ASM-OBJS.*=.*', l):
            label = ''
            ofiles = l.split('=')[1]
            source_type = 'asm'
        elif re.match('MMX-OBJS-.*CONFIG.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('CONFIG_')[1].rstrip(' )')
            source_type = 'mmx'
        elif re.match('MMX-OBJS-.*HAVE.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('HAVE_')[1].rstrip(' )')
            source_type = 'mmx'
        elif re.match('MMX-OBJS.*=.*', l):
            label = ''
            ofiles = l.split('=')[1]
            source_type = 'mmx'
        elif re.match('TESTPROGS-.*CONFIG.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('CONFIG_')[1].rstrip(' )')
            source_type = 'test-prog'
        elif re.match('TESTPROGS-.*HAVE.*\+\=.*', l):
            label, ofiles = l.split('+=')
            label = label.split('HAVE_')[1].rstrip(' )')
            source_type = 'test-prog'
        elif re.match('TESTPROGS.*=', l):
            label = ''
            ofiles = l.split('=')[1]
            source_type = "test-prog"
        else:
            continue

        accumulate = ofiles.endswith('\\')
        ofiles = ofiles.strip('\\')
        ofiles = ofiles.split()
        ext = {'c': 'c', 'asm': 'asm', 'test-prog': 'c', 'mmx': 'c'}[source_type]
        ifiles = [os.path.splitext(ofile)[0] + '.' + ext for ofile in ofiles]

        if accumulate:
            accum += ifiles
        else:
            map_ = source_maps[source_type]
            map_[label] += accum + ifiles
            accum = []

    # Makefiles can end with '\' and this is just a porting script ;)
    if accum:
        map_ = source_maps[source_type]
        map_[label] += accum
        accum = []


with open('generated.build', 'w') as f:
    for source_type, map_ in (('', source_maps['c']), ('x86asm_', source_maps['asm']), ('mmx_', source_maps['mmx'])):
        default_sources = map_.pop('', [])

        if default_sources:
            f.write('%ssources = files(\n' % '_'.join((sys.argv[1].replace('/', '_'), source_type)))
            for source in default_sources:
                if '$' in source:
                    print ('Warning: skipping %s' % source)
                    continue
                f.write("  '%s',\n" % os.path.basename(source))
            f.write(')\n\n')

        f.write('%soptional_sources = {\n' % '_'.join((sys.argv[1].replace('/', '_'), source_type)))
        for label in sorted (map_):
            f.write("  '%s' : files(" % label.lower())
            l = len (map_[label])
            for i, source in enumerate(map_[label]):
                if '$' in source:
                    print ('Warning: skipping %s' % source)
                    continue
                f.write("'%s'" % os.path.basename(source))
                if i + 1 < l:
                    f.write(',')
            f.write('),\n')
        f.write('}\n\n')

    test_source_map = source_maps['test-prog']

    default_test_sources = test_source_map.pop('', [])

    if default_test_sources:
        f.write('%s_tests = [\n' % sys.argv[1].replace('/', '_'))
        for source in default_test_sources:
            if '$' in source:
                print ('Warning: skipping %s' % source)
                continue
            basename = os.path.basename(source)
            testname = os.path.splitext(basename)[0]
            f.write("  ['%s', files('tests/%s')],\n" % (testname, basename))
        f.write(']\n\n')

    f.write('%s_optional_tests = {\n' % (sys.argv[1].replace('/', '_')))
    for label in sorted (test_source_map):
        f.write("  '%s' : [\n" % label.lower())
        for source in test_source_map[label]:
            if '$' in source:
                print ('Warning: skipping %s' % source)
                continue
            basename = os.path.basename(source)
            testname = os.path.splitext(basename)[0]
            f.write("    ['%s', files('tests/%s')],\n" % (testname, basename))
        f.write('  ],\n')
    f.write('}\n\n')
