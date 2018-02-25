libpostproc_majorver = '55'
minorver = '0'
microver = '100'

libpostproc_version = libpostproc_majorver + '.' + minorver + '.' + microver

libpostproc_sources = files([
  'postprocess.c',
])

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libpostproc_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  configuration: ver_conf,
)

configure_file(
  input: 'libpostproc.v.in',
  output: 'libpostproc.ver',
  configuration: ver_conf,
)
