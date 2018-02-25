libswresample_x86_sources = files([
  'audio_convert_init.c',
  'rematrix_init.c',
  'resample_init.c',
])

libswresample_x86_optional_sources = {
  'xmm_clobber_test' : files(['w64xmmtest.c',]),
}

libswresample_x86_x86asm_sources = files([
  'audio_convert.asm',
  'rematrix.asm',
  'resample.asm',
])
