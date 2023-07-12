libavcodec_arm_optional_sources = {
  'aac_decoder' : files('aacpsdsp_init_arm.c','sbrdsp_init_arm.c'),
  'ac3dsp' : files('ac3dsp_init_arm.c','ac3dsp_arm.S'),
  'audiodsp' : files('audiodsp_init_arm.c'),
  'blockdsp' : files('blockdsp_init_arm.c'),
  'dca_decoder' : files('synth_filter_init_arm.c'),
  'fft' : files('fft_init_arm.c'),
  'flacdsp' : files('flacdsp_init_arm.c','flacdsp_arm.S'),
  'fmtconvert' : files('fmtconvert_init_arm.c'),
  'g722dsp' : files('g722dsp_init_arm.c'),
  'h264chroma' : files('h264chroma_init_arm.c'),
  'h264dsp' : files('h264dsp_init_arm.c'),
  'h264pred' : files('h264pred_init_arm.c'),
  'h264qpel' : files('h264qpel_init_arm.c'),
  'hevc_decoder' : files('hevcdsp_init_arm.c'),
  'hpeldsp' : files('hpeldsp_init_arm.c','hpeldsp_arm.S'),
  'idctdsp' : files('idctdsp_init_arm.c','idctdsp_arm.S','jrevdct_arm.S','simple_idct_arm.S'),
  'llauddsp' : files('lossless_audiodsp_init_arm.c'),
  'me_cmp' : files('me_cmp_init_arm.c'),
  'mlp_decoder' : files('mlpdsp_init_arm.c'),
  'mpegaudiodsp' : files('mpegaudiodsp_init_arm.c'),
  'mpegvideo' : files('mpegvideo_arm.c'),
  'mpegvideoenc' : files('mpegvideoencdsp_init_arm.c'),
  'neon_clobber_test' : files('neontest.c'),
  'pixblockdsp' : files('pixblockdsp_init_arm.c'),
  'rdft' : files('rdft_init_arm.c'),
  'rv34dsp' : files('rv34dsp_init_arm.c'),
  'rv40_decoder' : files('rv40dsp_init_arm.c'),
  'sbc_encoder' : files('sbcdsp_init_arm.c'),
  'truehd_decoder' : files('mlpdsp_init_arm.c'),
  'vc1dsp' : files('vc1dsp_init_arm.c'),
  'videodsp' : files('videodsp_init_arm.c'),
  'vorbis_decoder' : files('vorbisdsp_init_arm.c'),
  'vp3dsp' : files('vp3dsp_init_arm.c'),
  'vp6_decoder' : files('vp6dsp_init_arm.c'),
  'vp8dsp' : files('vp8dsp_init_arm.c'),
  'vp9_decoder' : files('vp9dsp_init_10bpp_arm.c','vp9dsp_init_12bpp_arm.c','vp9dsp_init_arm.c'),
}

libavcodec_arm_x86asm_optional_sources = {
}

libavcodec_arm_armv5te_optional_sources = {
  'idctdsp' : files('idctdsp_init_armv5te.c','simple_idct_armv5te.S'),
  'mlp_decoder' : files('mlpdsp_armv5te.S'),
  'mpegvideo' : files('mpegvideo_armv5te.c','mpegvideo_armv5te_s.S'),
  'truehd_decoder' : files('mlpdsp_armv5te.S'),
  'videodsp' : files('videodsp_init_armv5te.c','videodsp_armv5te.S'),
}

libavcodec_arm_armv6_optional_sources = {
  'ac3dsp' : files('ac3dsp_armv6.S'),
  'hpeldsp' : files('hpeldsp_init_armv6.c','hpeldsp_armv6.S'),
  'idctdsp' : files('idctdsp_init_armv6.c','idctdsp_armv6.S','simple_idct_armv6.S'),
  'me_cmp' : files('me_cmp_armv6.S'),
  'mlp_decoder' : files('mlpdsp_armv6.S'),
  'mpegaudiodsp' : files('mpegaudiodsp_fixed_armv6.S'),
  'mpegvideoenc' : files('mpegvideoencdsp_armv6.S'),
  'pixblockdsp' : files('pixblockdsp_armv6.S'),
  'sbc_encoder' : files('sbcdsp_armv6.S'),
  'startcode' : files('startcode_armv6.S'),
  'truehd_decoder' : files('mlpdsp_armv6.S'),
  'vp8dsp' : files('vp8_armv6.S','vp8dsp_init_armv6.c','vp8dsp_armv6.S'),
}

libavcodec_arm_armv8_optional_sources = {
}

libavcodec_arm_neon_optional_sources = {
  'aac_decoder' : files('aacpsdsp_neon.S','sbrdsp_neon.S'),
  'ac3dsp' : files('ac3dsp_neon.S'),
  'audiodsp' : files('audiodsp_init_neon.c','audiodsp_neon.S','int_neon.S'),
  'blockdsp' : files('blockdsp_init_neon.c','blockdsp_neon.S'),
  'dca_decoder' : files('synth_filter_neon.S'),
  'fft' : files('fft_neon.S'),
  'fmtconvert' : files('fmtconvert_neon.S'),
  'g722dsp' : files('g722dsp_neon.S'),
  'h264chroma' : files('h264cmc_neon.S'),
  'h264dsp' : files('h264dsp_neon.S','h264idct_neon.S'),
  'h264pred' : files('h264pred_neon.S'),
  'h264qpel' : files('h264qpel_neon.S','hpeldsp_neon.S'),
  'hevc_decoder' : files('hevcdsp_init_neon.c','hevcdsp_deblock_neon.S','hevcdsp_idct_neon.S','hevcdsp_qpel_neon.S','hevcdsp_sao_neon.S'),
  'hpeldsp' : files('hpeldsp_init_neon.c','hpeldsp_neon.S'),
  'idctdsp' : files('idctdsp_init_neon.c','idctdsp_neon.S','simple_idct_neon.S'),
  'llauddsp' : files('lossless_audiodsp_neon.S'),
  'mdct' : files('mdct_neon.S'),
  'mpegvideo' : files('mpegvideo_neon.S'),
  'pixblockdsp' : files('pixblockdsp_neon.S'),
  'rdft' : files('rdft_neon.S'),
  'rv30_decoder' : files('rv34dsp_neon.S'),
  'rv40_decoder' : files('rv34dsp_neon.S','rv40dsp_neon.S'),
  'sbc_encoder' : files('sbcdsp_neon.S'),
  'vc1dsp' : files('vc1dsp_init_neon.c','vc1dsp_neon.S'),
  'vorbis_decoder' : files('vorbisdsp_neon.S'),
  'vp3dsp' : files('vp3dsp_neon.S'),
  'vp6_decoder' : files('vp6dsp_neon.S'),
  'vp8dsp' : files('vp8dsp_init_neon.c','vp8dsp_neon.S'),
  'vp9_decoder' : files('vp9itxfm_16bpp_neon.S','vp9itxfm_neon.S','vp9lpf_16bpp_neon.S','vp9lpf_neon.S','vp9mc_16bpp_neon.S','vp9mc_neon.S'),
}

libavcodec_arm_vfp_optional_sources = {
  'dca_decoder' : files('synth_filter_vfp.S'),
  'fft' : files('fft_vfp.S'),
  'fmtconvert' : files('fmtconvert_vfp.S'),
  'mdct' : files('mdct_vfp.S'),
}

libavcodec_arm_mmx_optional_sources = {
}

libavcodec_arm_shlib_optional_sources = {
}

libavcodec_arm_slib_optional_sources = {
}

libavcodec_arm_optional_tests = {
}

