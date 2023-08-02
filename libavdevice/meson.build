kwargs = {'prefix': '#include "libavdevice/version.h"'} + get_version_define_kwargs

libavdevice_majorver = cc.get_define('LIBAVDEVICE_VERSION_MAJOR', kwargs: kwargs)
minorver = cc.get_define('LIBAVDEVICE_VERSION_MINOR', kwargs: kwargs)
microver = cc.get_define('LIBAVDEVICE_VERSION_MICRO', kwargs: kwargs)

libavdevice_version = f'@libavdevice_majorver@.@minorver@.@microver@'

#### --- GENERATED --- ####

libavdevice_sources = files(
  'alldevices.c',
  'avdevice.c',
  'utils.c',
  'version.c',
)

libavdevice_headers = files(
  'avdevice.h',
  'version.h',
  'version_major.h',
)

libavdevice_optional_sources = {
  'alsa_indev' : files('alsa_dec.c','alsa.c','timefilter.c'),
  'alsa_outdev' : files('alsa_enc.c','alsa.c'),
  'android_camera_indev' : files('android_camera.c'),
  'audiotoolbox_outdev' : files('audiotoolbox.m'),
  'avfoundation_indev' : files('avfoundation.m'),
  'bktr_indev' : files('bktr.c'),
  'caca_outdev' : files('caca.c'),
  'decklink_indev' : files('decklink_dec.cpp','decklink_dec_c.c','decklink_common.cpp'),
  'decklink_outdev' : files('decklink_enc.cpp','decklink_enc_c.c','decklink_common.cpp'),
  'dshow_indev' : files('dshow_crossbar.c','dshow.c','dshow_enummediatypes.c','dshow_enumpins.c','dshow_filter.c','dshow_pin.c','dshow_common.c'),
  'fbdev_indev' : files('fbdev_dec.c','fbdev_common.c'),
  'fbdev_outdev' : files('fbdev_enc.c','fbdev_common.c'),
  'gdigrab_indev' : files('gdigrab.c'),
  'iec61883_indev' : files('iec61883.c'),
  'jack_indev' : files('jack.c','timefilter.c'),
  'kmsgrab_indev' : files('kmsgrab.c'),
  'lavfi_indev' : files('lavfi.c'),
  'libcdio_indev' : files('libcdio.c'),
  'libc_msvcrt' : files('file_open.c'),
  'libdc1394_indev' : files('libdc1394.c'),
  'openal_indev' : files('openal-dec.c'),
  'opengl_outdev' : files('opengl_enc.c'),
  'oss_indev' : files('oss_dec.c','oss.c'),
  'oss_outdev' : files('oss_enc.c','oss.c'),
  'pulse_indev' : files('pulse_audio_dec.c','pulse_audio_common.c','timefilter.c'),
  'pulse_outdev' : files('pulse_audio_enc.c','pulse_audio_common.c'),
  'sdl2_outdev' : files('sdl2.c'),
  'sndio_indev' : files('sndio_dec.c','sndio.c'),
  'sndio_outdev' : files('sndio_enc.c','sndio.c'),
  'v4l2_indev' : files('v4l2.c','v4l2-common.c','timefilter.c'),
  'v4l2_outdev' : files('v4l2enc.c','v4l2-common.c'),
  'vfwcap_indev' : files('vfwcap.c'),
  'xcbgrab_indev' : files('xcbgrab.c'),
  'xv_outdev' : files('xv.c'),
}

libavdevice_x86asm_optional_sources = {
}

libavdevice_armv5te_optional_sources = {
}

libavdevice_armv6_optional_sources = {
}

libavdevice_armv8_optional_sources = {
}

libavdevice_neon_optional_sources = {
}

libavdevice_vfp_optional_sources = {
}

libavdevice_mmx_optional_sources = {
}

libavdevice_shlib_optional_sources = {
  'decklink_indev' : files('reverse.c'),
}

libavdevice_slib_optional_sources = {
}

libavdevice_optional_tests = {
  'jack_indev' : [
    ['timefilter', files('tests/timefilter.c')],
  ],
}

languages_map += {
  'audiotoolbox_outdev': ['objc'],
  'avfoundation_indev': ['objc'],
  'decklink_outdev': ['cpp'],
  'decklink_indev': ['cpp'],
}
#### --- END GENERATED --- ####

# Version file
ver_conf = configuration_data()
ver_conf.set('majorver', libavdevice_majorver)
ver_conf.set('minorver', minorver)
ver_conf.set('microver', microver)

install_headers(libavdevice_headers, subdir: 'libavdevice')

configure_file(
  input: 'libavdevice.v.in',
  output: 'libavdevice.ver',
  configuration: ver_conf,
)
