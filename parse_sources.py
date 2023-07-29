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
import io
import sys
from pprint import pprint
from collections import defaultdict

ASM_EXTS = ['asm', 'S', 'c']

SOURCE_TYPE_EXTS_MAP = {
    'c': ['c', 'cpp', 'm', 'cl', 'S'],
    'asm': ASM_EXTS,
    'armv5te': ASM_EXTS,
    'armv6': ASM_EXTS,
    'armv8': ASM_EXTS,
    'vfp': ASM_EXTS,
    'neon': ASM_EXTS,
    'test-prog': ['c'],
    'mmx': ['c'],
    'shlib': ['c'],
    'slib': ['c'],
}
SOURCE_TYPE_DIRS = {'test-prog': 'tests'}


def add_source(f, source, prefix='', suffix=''):
    if not source.startswith('opencl/'):
        source = os.path.basename(source)
    f.write("%s'%s'%s" % (prefix, source, suffix))


def add_language(languages_map, ext, label):
    if ext == 'cpp':
        languages_map[label].add('cpp')
    elif ext == 'm':
        languages_map[label].add('objc')


def make_to_meson(path):
    source_maps = {
      'c': defaultdict(list),
      'asm': defaultdict(list),
      'armv5te': defaultdict(list),
      'armv6': defaultdict(list),
      'armv8': defaultdict(list),
      'vfp': defaultdict(list),
      'neon': defaultdict(list),
      'test-prog': defaultdict(list),
      'mmx': defaultdict(list),
      'shlib': defaultdict(list),
      'slib': defaultdict(list),
    }

    skipped = set()

    with open(os.path.join(path, 'Makefile'), 'r') as f:
        accum = []
        accumulate = False
        optional = False
        source_type = None
        languages_map = defaultdict(set)

        for l in f.readlines():
            l = l.strip()
            l = l.rsplit('#', 1)[0]

            if accumulate:
                ofiles = l
            elif re.match('OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'c' # arguable ^^
            elif re.match('OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'c'
            elif re.match('OBJS-ffmpeg\s+\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('OBJS-')[1]
                source_type = 'c' # arguable ^^
            elif re.match('DNN-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'c'  # arguable too ^^
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
            elif re.match('SLIBOBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'slib'
            elif re.match('SHLIBOBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'shlib'
            elif re.match('SLIBOBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'slib'
            elif re.match('SHLIBOBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'shlib'
            elif re.match('TLS-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'c' # arguable ^^
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
            elif re.match('ARMV5TE-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'armv5te'
            elif re.match('ARMV5TE-OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'armv5te'
            elif re.match('ARMV5TE-OBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'armv5te'
            elif re.match('ARMV6-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'armv6'
            elif re.match('ARMV6-OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'armv6'
            elif re.match('ARMV6-OBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'armv6'
            elif re.match('ARMV8-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'armv8'
            elif re.match('ARMV8-OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'armv8'
            elif re.match('ARMV8-OBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'armv8'
            elif re.match('VFP-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'vfp'
            elif re.match('VFP-OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'vfp'
            elif re.match('VFP-OBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'vfp'
            elif re.match('NEON-OBJS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'neon'
            elif re.match('NEON-OBJS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'neon'
            elif re.match('NEON-OBJS.*=.*', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'neon'
            elif re.match('TESTPROGS-.*CONFIG.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('CONFIG_')[1].rstrip(' )')
                source_type = 'test-prog'
            elif re.match('TESTPROGS-.*HAVE.*\+\=.*', l):
                label, ofiles = l.split('+=')
                label = label.split('HAVE_')[1].rstrip(' )')
                source_type = 'test-prog'
            elif re.match('TESTOBJS.*=', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = 'c'
            elif re.match('TESTPROGS.*=', l):
                label = ''
                ofiles = l.split('=')[1]
                source_type = "test-prog"
            else:
                continue

            accumulate = ofiles.endswith('\\')
            ofiles = ofiles.strip('\\')
            ofiles = ofiles.split()
            exts = SOURCE_TYPE_EXTS_MAP[source_type]
            ifiles = []
            for ofile in ofiles:
                fname = os.path.splitext(ofile)[0]
                for ext in exts:
                    tmpf = fname + '.' + ext
                    if os.path.exists(os.path.join(path, SOURCE_TYPE_DIRS.get(source_type, ''), tmpf)):
                        ifiles.append(tmpf)
                        add_language(languages_map, ext, label)
                        break
                    elif os.path.exists(os.path.join(path, SOURCE_TYPE_DIRS.get(source_type, ''), os.path.basename(tmpf))):
                        ifiles.append(tmpf)
                        add_language(languages_map, ext, label)
                        break

            if len([of for of in ofiles if not of.startswith("$")]) != len(ifiles):
                print("WARNING: %s and %s size don't match, not building!" % ([of for of in ofiles if not of.startswith("$")], ifiles))
                skipped.add(label)

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


    lines = []
    has_not_generated = False
    try:
        with open(os.path.join(path, 'meson.build'), 'r') as meson_file:
            for l in meson_file.readlines():
                if l == '#### --- GENERATED --- ####\n':
                    lines += [l, '\n']
                    has_not_generated = True
                    break
                lines.append(l)
    except FileNotFoundError:
        pass

    f = io.StringIO()

    source_types = (
        ('', source_maps['c']),
        ('x86asm_', source_maps['asm']),
        ('armv5te_', source_maps['armv5te']),
        ('armv6_', source_maps['armv6']),
        ('armv8_', source_maps['armv8']),
        ('neon_', source_maps['neon']),
        ('vfp_', source_maps['vfp']),
        ('mmx_', source_maps['mmx']),
        ('shlib_', source_maps['shlib']),
        ('slib_', source_maps['slib'])
    )

    for source_type, map_ in source_types:
        default_sources = map_.pop('', [])

        if default_sources:
            f.write('%ssources = files(\n' % '_'.join((path.replace('/', '_'), source_type)))
            for source in default_sources:
                if '$' in source:
                    print ('Warning: skipping %s' % source)
                    continue
                add_source(f, source, prefix='  ', suffix=',\n')
            f.write(')\n\n')

        f.write('%soptional_sources = {\n' % '_'.join((path.replace('/', '_'), source_type)))
        for label in sorted (map_):
            if label in skipped:
                f.write("  # '%s' : files(" % label.lower())
            else:
                f.write("  '%s' : files(" % label.lower())
            l = len (map_[label])
            for i, source in enumerate(map_[label]):
                if '$' in source:
                    print ('Warning: skipping %s' % source)
                    continue
                add_source(f, source)
                if i + 1 < l:
                    f.write(',')
            f.write('),\n')
        f.write('}\n\n')

    test_source_map = source_maps['test-prog']

    default_test_sources = test_source_map.pop('', [])

    if default_test_sources:
        f.write('%s_tests = [\n' % path.replace('/', '_'))
        for source in default_test_sources:
            if '$' in source:
                print ('Warning: skipping %s' % source)
                continue
            basename = os.path.basename(source)
            testname = os.path.splitext(basename)[0]
            f.write("  ['%s', files('tests/%s')],\n" % (testname, basename))
        f.write(']\n\n')

    f.write('%s_optional_tests = {\n' % path.replace('/', '_'))
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

    if languages_map:
        f.write('languages_map += {\n')
        for label, languages in languages_map.items():
            f.write("  '%s': %s,\n" % (label.lower(), list(languages)))
        f.write('}\n')

    if has_not_generated:
        lines.append(f.getvalue())
        with open(os.path.join(path, 'meson.build'), 'r') as meson_file:
            out_generated = False
            for l in meson_file.readlines():
                if l == '#### --- END GENERATED --- ####\n':
                    out_generated = True
                if out_generated:
                    lines.append(l)
        content = ''.join(lines)
    else:
        content = f.getvalue()


    with open(os.path.join(path, 'meson.build'), 'w') as meson_file:
        meson_file.write(content)

paths = [
        'fftools',
        'libavdevice',
        'libavformat',
        'libavutil',
        'libavutil/aarch64',
        'libavutil/arm',
        'libavutil/x86',
        'libswscale',
        'libswscale/aarch64',
        'libswscale/arm',
        'libswscale/x86',
        'libavcodec',
        'libavcodec/aarch64',
        'libavcodec/arm',
        'libavcodec/neon',
        'libavcodec/x86',
        'libswresample',
        'libswresample/aarch64',
        'libswresample/arm',
        'libswresample/x86',
        'libavfilter',
        'libavfilter/aarch64',
        'libavfilter/x86',
        'libavfilter/dnn',
        'libpostproc',
]

if __name__=='__main__':
    for path in paths:
        make_to_meson(path)
