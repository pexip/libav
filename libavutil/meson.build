libavutil_majorver = '56'
minorver = '18'
microver = '102'

libavutil_version = libavutil_majorver + '.' + minorver + '.' + microver

libavutil_sources = files([
  'adler32.c',
  'aes.c',
  'aes_ctr.c',
  'audio_fifo.c',
  'avstring.c',
  'base64.c',
  'blowfish.c',
  'bprint.c',
  'buffer.c',
  'cast5.c',
  'camellia.c',
  'channel_layout.c',
  'color_utils.c',
  'cpu.c',
  'crc.c',
  'des.c',
  'dict.c',
  'display.c',
  'downmix_info.c',
  'encryption_info.c',
  'error.c',
  'eval.c',
  'fifo.c',
  'file.c',
  'file_open.c',
  'float_dsp.c',
  'fixed_dsp.c',
  'frame.c',
  'hash.c',
  'hmac.c',
  'hwcontext.c',
  'imgutils.c',
  'integer.c',
  'intmath.c',
  'lfg.c',
  'lls.c',
  'log.c',
  'log2_tab.c',
  'mathematics.c',
  'mastering_display_metadata.c',
  'md5.c',
  'mem.c',
  'murmur3.c',
  'opt.c',
  'parseutils.c',
  'pixdesc.c',
  'pixelutils.c',
  'random_seed.c',
  'rational.c',
  'reverse.c',
  'rc4.c',
  'ripemd.c',
  'samplefmt.c',
  'sha.c',
  'sha512.c',
  'slicethread.c',
  'spherical.c',
  'stereo3d.c',
  'threadmessage.c',
  'time.c',
  'timecode.c',
  'tree.c',
  'twofish.c',
  'utils.c',
  'xga_font_data.c',
  'xtea.c',
  'tea.c',
])

libavutil_optional_sources = {
  'cuda' : files('hwcontext_cuda.c'),
  'd3d11va' : files('hwcontext_d3d11va.c'),
  'dxva2' : files('hwcontext_dxva2.c'),
  'libdrm' : files('hwcontext_drm.c'),
  'lzo' : files('lzo.c'),
  'mediacodec' : files('hwcontext_mediacodec.c'),
  'opencl' : files('hwcontext_opencl.c'),
  'qsv' : files('hwcontext_qsv.c'),
  'vaapi' : files('hwcontext_vaapi.c'),
  'vdpau' : files('hwcontext_vdpau.c'),
  'videotoolbox' : files('hwcontext_videotoolbox.c'),
}

libavutil_x86asm_optional_sources = {
}

libavutil_mmx_optional_sources = {
}

libavutil_tests = [
  ['adler32', files(['tests/adler32.c'])],
  ['aes', files(['tests/aes.c'])],
  ['aes_ctr', files(['tests/aes_ctr.c'])],
  ['audio_fifo', files(['tests/audio_fifo.c'])],
  ['avstring', files(['tests/avstring.c'])],
  ['base64', files(['tests/base64.c'])],
  ['blowfish', files(['tests/blowfish.c'])],
  ['bprint', files(['tests/bprint.c'])],
  ['cast5', files(['tests/cast5.c'])],
  ['camellia', files(['tests/camellia.c'])],
  ['color_utils', files(['tests/color_utils.c'])],
  ['cpu', files(['tests/cpu.c'])],
  ['crc', files(['tests/crc.c'])],
  ['des', files(['tests/des.c'])],
  ['dict', files(['tests/dict.c'])],
  ['display', files(['tests/display.c'])],
  ['error', files(['tests/error.c'])],
  ['eval', files(['tests/eval.c'])],
  ['fifo', files(['tests/fifo.c'])],
  ['hash', files(['tests/hash.c'])],
  ['hmac', files(['tests/hmac.c'])],
  ['hwdevice', files(['tests/hwdevice.c'])],
  ['integer', files(['tests/integer.c'])],
  ['imgutils', files(['tests/imgutils.c'])],
  ['lfg', files(['tests/lfg.c'])],
  ['lls', files(['tests/lls.c'])],
  ['log', files(['tests/log.c'])],
  ['md5', files(['tests/md5.c'])],
  ['murmur3', files(['tests/murmur3.c'])],
  ['opt', files(['tests/opt.c'])],
  ['pca', files(['tests/pca.c'])],
  ['parseutils', files(['tests/parseutils.c'])],
  ['pixdesc', files(['tests/pixdesc.c'])],
  ['pixelutils', files(['tests/pixelutils.c'])],
  ['pixfmt_best', files(['tests/pixfmt_best.c'])],
  ['random_seed', files(['tests/random_seed.c'])],
  ['rational', files(['tests/rational.c'])],
  ['ripemd', files(['tests/ripemd.c'])],
  ['sha', files(['tests/sha.c'])],
  ['sha512', files(['tests/sha512.c'])],
  ['softfloat', files(['tests/softfloat.c'])],
  ['tree', files(['tests/tree.c'])],
  ['twofish', files(['tests/twofish.c'])],
  # ['utf8', files(['tests/utf8.c'])],
  ['xtea', files(['tests/xtea.c'])],
  ['tea', files(['tests/tea.c'])],
]

# Test tries to map a file and write to the buffer, except
# on Windows MapViewOfFile is called with FILE_MAP_READ ...
if host_machine.system() != 'windows'
  libavutil_tests += [['file', files(['tests/file.c'])]]
endif

libavutil_optional_tests = {
  'lzo1x_999_compress' : [
    ['lzo', files(['tests/lzo.c']), {'extra_libs': ['lzo2']}],
  ],
  'threads' : [
    ['cpu_init', files(['tests/cpu_init.c'])],
  ],
}

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libavutil_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  configuration: ver_conf,
)

# Lavu configuration file
lavu_conf = configuration_data()
lavu_conf.set10('AV_HAVE_BIGENDIAN', host_machine.endian() == 'big')
lavu_conf.set10('HAVE_FAST_UNALIGNED', ['x86', 'x86_64', 'aarch', 'ppc'].contains(host_machine.cpu_family()))

configure_file(
  output: 'avconfig.h',
  configuration: lavu_conf,
)

configure_file(
  input: 'libavutil.v.in',
  output: 'libavutil.ver',
  configuration: ver_conf,
)

ffversion_h = custom_target('ffversion.h',
  output: 'ffversion.h',
  command: [find_program('version.py'), join_paths(meson.current_source_dir(), '..'), '@OUTPUT@', ''],
  build_by_default: true,
)

subdir('x86')
