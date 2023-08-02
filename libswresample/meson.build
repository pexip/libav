kwargs = {'prefix': '#include "libswresample/version.h"'} + get_version_define_kwargs

libswresample_majorver = cc.get_define('LIBSWRESAMPLE_VERSION_MAJOR', kwargs: kwargs)
minorver = cc.get_define('LIBSWRESAMPLE_VERSION_MINOR', kwargs: kwargs)
microver = cc.get_define('LIBSWRESAMPLE_VERSION_MICRO', kwargs: kwargs)

libswresample_version = f'@libswresample_majorver@.@minorver@.@microver@'

#### --- GENERATED --- ####

libswresample_sources = files(
  'audioconvert.c',
  'dither.c',
  'options.c',
  'rematrix.c',
  'resample.c',
  'resample_dsp.c',
  'swresample.c',
  'swresample_frame.c',
  'version.c',
)

libswresample_headers = files(
  'swresample.h',
  'version.h',
  'version_major.h',
)

libswresample_optional_sources = {
  'libsoxr' : files('soxr_resample.c'),
}

libswresample_x86asm_optional_sources = {
}

libswresample_armv5te_optional_sources = {
}

libswresample_armv6_optional_sources = {
}

libswresample_armv8_optional_sources = {
}

libswresample_neon_optional_sources = {
}

libswresample_vfp_optional_sources = {
}

libswresample_mmx_optional_sources = {
}

libswresample_shlib_sources = files(
  'log2_tab.c',
)

libswresample_shlib_optional_sources = {
}

libswresample_slib_optional_sources = {
}

libswresample_tests = [
  ['swresample', files('tests/swresample.c')],
]

libswresample_optional_tests = {
}

#### --- END GENERATED --- ####

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libswresample_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

install_headers(libswresample_headers, subdir: 'libswresample')

configure_file(
  input: 'libswresample.v.in',
  output: 'libswresample.ver',
  configuration: ver_conf,
)

subdir('aarch64')
subdir('arm')
subdir('x86')
