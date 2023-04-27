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

import re
import os

if __name__ == '__main__':
     with open(f'{os.environ["MESON_BUILD_ROOT"]}/meson-logs/meson-log.txt', encoding="utf-8", mode='r') as f:
        lines = [line for line in f if 'Build Options' in line]

        options = re.match(r'Build Options:\s+(.+)$', lines[-1])

        if options is not None:
            print(options.group(1))

