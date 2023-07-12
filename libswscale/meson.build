kwargs = {'prefix': '#include "libswscale/version.h"'} + get_version_define_kwargs

libswscale_majorver = cc.get_define('LIBSWSCALE_VERSION_MAJOR', kwargs: kwargs)
minorver = cc.get_define('LIBSWSCALE_VERSION_MINOR', kwargs: kwargs)
microver = cc.get_define('LIBSWSCALE_VERSION_MICRO', kwargs: kwargs)

libswscale_version = f'@libswscale_majorver@.@minorver@.@microver@'

libswscale_headers = files(
  'swscale.h',
)


#### --- GENERATED --- ####

libswscale_sources = files(
  'alphablend.c',
  'hscale.c',
  'hscale_fast_bilinear.c',
  'gamma.c',
  'input.c',
  'options.c',
  'output.c',
  'rgb2rgb.c',
  'slice.c',
  'swscale.c',
  'swscale_unscaled.c',
  'utils.c',
  'yuv2rgb.c',
  'vscale.c',
)

libswscale_optional_sources = {
}

libswscale_x86asm_optional_sources = {
}

libswscale_armv5te_optional_sources = {
}

libswscale_armv6_optional_sources = {
}

libswscale_armv8_optional_sources = {
}

libswscale_neon_optional_sources = {
}

libswscale_vfp_optional_sources = {
}

libswscale_mmx_optional_sources = {
}

libswscale_shlib_sources = files(
  'log2_tab.c',
)

libswscale_shlib_optional_sources = {
}

libswscale_slib_optional_sources = {
}

libswscale_tests = [
  ['colorspace', files('tests/colorspace.c')],
  ['floatimg_cmp', files('tests/floatimg_cmp.c')],
  ['pixdesc_query', files('tests/pixdesc_query.c')],
  # MANUAL ['swscale', files('tests/swscale.c')],
]

libswscale_optional_tests = {
}

#### --- END GENERATED --- ####

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libswscale_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

install_headers(libswscale_headers, subdir: 'libswscale')

configure_file(
  input: 'libswscale.v.in',
  output: 'libswscale.ver',
  configuration: ver_conf,
)

subdir('aarch64')
subdir('arm')
subdir('x86')
