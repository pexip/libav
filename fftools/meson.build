ffmpeg_sources = files([
  'ffmpeg.c',
  'ffmpeg_opt.c',
  'ffmpeg_filter.c',
  'ffmpeg_hw.c',
  'cmdutils.c',
])

ffmpeg_optional_sources = {
  'cuvid' : files('ffmpeg_cuvid.c'),
  'libmfx' : files('ffmpeg_qsv.c'),
  'vda' : files('ffmpeg_videotoolbox.c'),
  'videotoolbox' : files('ffmpeg_videotoolbox.c'),
}

ffplay_sources = files([
  'ffplay.c',
  'cmdutils.c',
])

ffprobe_sources = files([
  'ffprobe.c',
  'cmdutils.c',
])
