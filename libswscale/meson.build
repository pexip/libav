libswscale_majorver = '5'
minorver = '2'
microver = '100'

libswscale_version = libswscale_majorver + '.' + minorver + '.' + microver

libswscale_sources = files([
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
])

libswscale_optional_sources = {
  'shared' : files('log2_tab.c'),
}

libswscale_tests = [
  ['colorspace', files(['tests/colorspace.c'])],
  ['pixdesc_query', files(['tests/pixdesc_query.c'])],
  # ['swscale', files(['tests/swscale.c'])], Too slow
]

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libswscale_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  configuration: ver_conf,
)

configure_file(
  input: 'libswscale.v.in',
  output: 'libswscale.ver',
  configuration: ver_conf,
)

subdir('x86')
