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

EXTERN_THINGS = [
    ['AVOutputFormat', 'muxer', 'libavformat/allformats.c', 'muxer_list'],
    ['AVInputFormat', 'demuxer', 'libavformat/allformats.c', 'demuxer_list'],
    ['AVCodec', 'encoder', 'libavcodec/allcodecs.c', 'encoder_list'],
    ['AVCodec', 'decoder', 'libavcodec/allcodecs.c', 'decoder_list'],
    ['AVCodecParser', 'parser', 'libavcodec/parsers.c', 'parser_list'],
    ['AVBitStreamFilter', 'bsf', 'libavcodec/bitstream_filters.c', 'bsf_list'],
    ['AVHWAccel', 'hwaccel', 'libavcodec/hwaccels.h', 'hwaccel_list'],
    ['URLProtocol', 'protocol', 'libavformat/protocols.c', 'protocol_list'],
    ['AVOutputFormat', 'muxer', 'libavdevice/alldevices.c', 'outdev_list', 'outdev'],
    ['AVInputFormat', 'demuxer', 'libavdevice/alldevices.c', 'indev_list', 'indev'],
]

def list_components(infile, type, suffix, thing_suffix):
    things = []

    for line in infile:
        matches = re.match(r'^extern.*' + type +
                            ' *ff_([^ ]*)_' + suffix + ';', line.strip())
        if matches:
            things += [matches.group(1).strip()]

    return ['%s_%s' % (thing, thing_suffix) for thing in things]

def update_meson_options(options):
    has_generated = False
    lines = []
    with open('meson_options.txt', 'r', encoding='utf8') as meson_file:
        opening = '#### --- GENERATED EXTERN OPTIONS --- ####\n'
        closing = opening.replace('GENERATED', 'END GENERATED')
        for l in meson_file.readlines():
            if l == opening:
                has_generated = True
                lines.append(l)
                for component, list in options.items():
                    lines.append(f'# Generated {component} options\n')
                    for option in list:
                        if re.match(f'^null_{component}', option):
                            value = 'enabled'
                        else:
                            value = 'auto'
                        lines.append(
                            ('option(\'%s\', type: \'feature\', value: \'%s\')\n' % (option, value)))
                    lines.append('\n')
            elif l == closing:
                lines.append(l)
                has_generated = False
            elif not has_generated:
                lines.append(l)

    with open('meson_options.txt', 'w') as meson_file:
        meson_file.write(''.join(lines))

# Used to extract list of muxers, demuxers, encoders, etc.
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Find extern declarations in all*.c')

    arg_parser.add_argument('--suffix', metavar='STRING',
                            default='',
                            help='Variable name suffix, e.g. muxer')
    arg_parser.add_argument('--update-options', action='store_true',
                            help='update the Meson options list and exit')
    arg_parser.add_argument('--type', metavar='STRING',
                            default='',
                            help='Variable type, e.g. AVOutputFormat')
    arg_parser.add_argument('--thing-suffix', metavar='STRING',
                            default='',
                            help='suffix to add to the thing name')
    arg_parser.add_argument('files', metavar='FILE', nargs='*',
                            type=argparse.FileType('r'),
                            help='File with lists of declarations, ' +
                            'or "-" for standard input')

    args = arg_parser.parse_args()

    if args.update_options:
        options = {}

        for extern_thing in EXTERN_THINGS:
            type = extern_thing[0]
            suffix = extern_thing[1]
            filename = extern_thing[2]

            if len(extern_thing) > 4:
                thing_suffix = extern_thing[4]
            else:
                thing_suffix = suffix

            with open(filename, 'r', encoding='utf-8') as infile:
                components = list_components(
                    infile, type, suffix, thing_suffix)
                options[thing_suffix] = components

        update_meson_options(options)
    else:
        things = []
        for infile in args.files:
            things += list_components(infile, args.type, args.suffix, args.thing_suffix)

        print('\n'.join(things))
