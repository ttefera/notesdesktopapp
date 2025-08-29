# clean build output
rm -rf build_output
mkdir build_output

# run pyinstaller with custom output dirs + asset bundling
pyinstaller \
  --onefile \
  --windowed \
  --distpath build_output/dist \
  --workpath build_output/build \
  --specpath build_output \
#   --add-data "background.png:." \
#   --add-data "save_icon.png:." \
  NotesApp.py