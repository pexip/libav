project('nasm', version : '2.16.01')

download_binary = find_program(meson.current_source_dir() / 'download-binary.py')

arch = host_machine.system()

if not ['windows', 'darwin'].contains(arch)
  warning('Can only download nasm for Windows or macOS, sorry')
  subdir_done()
endif

message('Downloading and extracting nasm binaries for @0@...'.format(arch))

if arch == 'windows'
  arch = host_machine.cpu_family()
  if arch == 'x86_64'
    zip_hash = '029eed31faf0d2c5f95783294432cbea6c15bf633430f254bb3c1f195c67ca3a'
  else
    zip_hash = 'e289fa70c88594b092c916344bb8bfcd6896b604bfab284ab57b1372997c820c'
  endif
else
  # macOS binaries are only identified as architecture "macosx"
  zip_hash = 'd53c9a1bc9cd92d22e37924d31e9c68413fa03104fd165a6e7b7faf8800a1822'
endif

download = run_command(download_binary, meson.project_version(), arch, zip_hash)

if download.returncode() != 0
  warning('Download failed: @0@'.format(download.stderr().strip()))
  subdir_done()
endif

nasm_path = meson.current_source_dir() / 'nasm-@0@'.format(meson.project_version())

if host_machine.system() != 'windows'
  # Fix ZIP permissions -- zipfile doesn't support this extended format
  patch_nasm = find_program('patch_nasm.py', required: true)
  run_command(patch_nasm, nasm_path, check: true)
endif

meson.override_find_program('nasm', find_program(nasm_path / 'nasm'))
