#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nirbheek Chauhan <nirbheek@centricular.com>
# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@centricular.com>
# SPDX-License-Ref: LGPL-2.1-or-later

import os
import sys
import ssl
import zipfile
import hashlib
import urllib.request
import urllib.error

# Disable certificate checking because it always fails on Windows
# We verify the checksum anyway.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASENAME = 'nasm-{}-{}.zip'
UPSTREAM_URL = 'https://www.nasm.us/pub/nasm/releasebuilds/{}/{}/{}'
GSTREAMER_URL = 'https://gstreamer.freedesktop.org/src/mirror/{}'

version = sys.argv[1]
if sys.argv[2] == 'darwin':
    arch = 'macosx'
elif sys.argv[2] == 'x86_64':
    arch = 'win64'
else:
    arch = 'win32'
zip_sha256 = sys.argv[3]
source_dir = os.path.join(os.environ['MESON_SOURCE_ROOT'], os.environ['MESON_SUBDIR'])
dest = BASENAME.format(version, arch)
dest_path = os.path.join(source_dir, dest)

def get_sha256(zipf):
    hasher = hashlib.sha256()
    with open(zipf, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

if os.path.isfile(dest_path):
    found_sha256 = get_sha256(dest_path)
    if found_sha256 == zip_sha256:
        print('{} already downloaded'.format(dest))
    else:
        os.remove(dest)
        print('{} checksum mismatch, redownloading'.format(dest), file=sys.stderr)

if not os.path.isfile(dest_path):
    for url in (GSTREAMER_URL.format(dest), UPSTREAM_URL.format(version, arch, dest)):
        print('Downloading {} to {}'.format(url, dest))
        try:
            with open(dest_path, 'wb') as d:
                f = urllib.request.urlopen(url, context=ctx)
                d.write(f.read())
            break
        except BaseException as ex:
            print(ex, file=sys.stderr)
            print('Failed to download from {!r}, trying mirror...'.format(url), file=sys.stderr)
            continue
    else:
        curdir = os.path.dirname(sys.argv[0])
        print('Couldn\'t download {!r}! Try downloading it manually and '
            'placing it into {!r}'.format(dest, curdir), file=sys.stderr)
        sys.exit(1)

found_sha256 = get_sha256(dest_path)
if found_sha256 != zip_sha256:
    print('SHA256 of downloaded file {} was {} instead of {}'
          ''.format(dest, found_sha256, zip_sha256), file=sys.stderr)
    sys.exit(1)

print('Extracting {}'.format(dest))
zf = zipfile.ZipFile(dest_path, "r")
zf.extractall(path=source_dir)
