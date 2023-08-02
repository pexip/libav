kwargs = {'prefix': '#include "libpostproc/version.h"'} + get_version_define_kwargs

libpostproc_majorver = cc.get_define('LIBPOSTPROC_VERSION_MAJOR', kwargs: kwargs)
minorver = cc.get_define('LIBPOSTPROC_VERSION_MINOR', kwargs: kwargs)
microver = cc.get_define('LIBPOSTPROC_VERSION_MICRO', kwargs: kwargs)

libpostproc_version = f'@libpostproc_majorver@.@minorver@.@microver@'

#### --- GENERATED --- ####

libpostproc_sources = files(
  'postprocess.c',
  'version.c',
)

libpostproc_headers = files(
  'postprocess.h',
  'version.h',
  'version_major.h',
)

libpostproc_optional_sources = {
}

libpostproc_x86asm_optional_sources = {
}

libpostproc_armv5te_optional_sources = {
}

libpostproc_armv6_optional_sources = {
}

libpostproc_armv8_optional_sources = {
}

libpostproc_neon_optional_sources = {
}

libpostproc_vfp_optional_sources = {
}

libpostproc_mmx_optional_sources = {
}

libpostproc_shlib_optional_sources = {
}

libpostproc_slib_optional_sources = {
}

libpostproc_optional_tests = {
}

#### --- END GENERATED --- ####

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libpostproc_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

install_headers(libpostproc_headers, subdir: 'libpostproc')

configure_file(
  input: 'libpostproc.v.in',
  output: 'libpostproc.ver',
  configuration: ver_conf,
)
