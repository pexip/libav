#### --- GENERATED --- ####

fftools_sources = files(
  'cmdutils.c',
  'opt_common.c',
)

fftools_optional_sources = {
  # MANUAL 'ffmpeg ' : files('ffmpeg_demux.c','ffmpeg_filter.c','ffmpeg_hw.c','ffmpeg_mux.c','ffmpeg_mux_init.c','ffmpeg_opt.c','objpool.c','sync_queue.c','thread_queue.c'),
}

fftools_x86asm_optional_sources = {
}

fftools_armv5te_optional_sources = {
}

fftools_armv6_optional_sources = {
}

fftools_armv8_optional_sources = {
}

fftools_neon_optional_sources = {
}

fftools_vfp_optional_sources = {
}

fftools_mmx_optional_sources = {
}

fftools_shlib_optional_sources = {
}

fftools_slib_optional_sources = {
}

fftools_optional_tests = {
}

#### --- END GENERATED --- ####

ffmpeg_sources = files(
  'ffmpeg_demux.c',
  'ffmpeg_filter.c',
  'ffmpeg_hw.c',
  'ffmpeg_mux.c',
  'ffmpeg_mux_init.c',
  'ffmpeg_opt.c',
  'objpool.c',
  'sync_queue.c',
  'thread_queue.c',
  'ffmpeg.c'
)

ffplay_sources = files(
  'ffplay.c'
)

ffprobe_sources = files(
  'ffprobe.c'
)

if host_machine.system() == 'windows'
  fftoolsres = windows.compile_resources(files('fftoolsres.rc'),
    depend_files: files('fftools.manifest'),
    include_directories: include_directories('.')
  )

  fftools_sources += fftoolsres
endif
