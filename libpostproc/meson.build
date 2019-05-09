libpostproc_majorver = '55'
minorver = '3'
microver = '100'

libpostproc_version = libpostproc_majorver + '.' + minorver + '.' + microver

libpostproc_headers = files(
  'postprocess.h',
)

libpostproc_sources = files(
  'postprocess.c',
)

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libpostproc_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  configuration: ver_conf,
  install_dir: join_paths(get_option('includedir'), 'libpostproc'),
  install: true,
)

install_headers(libpostproc_headers, subdir: 'libpostproc')

configure_file(
  input: 'libpostproc.v.in',
  output: 'libpostproc.ver',
  configuration: ver_conf,
)
