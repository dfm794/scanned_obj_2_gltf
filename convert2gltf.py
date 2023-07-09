from pathlib import Path
import os
import shutil

scanned_objects_dataset_path = Path('/data/scanned_objects')
output_path = Path('/data/dfm/scanned_objects_gltf')

# Create output directory
if not output_path.exists():
    os.mkdir(output_path)
    

# list all files in scanned_objects_dataset_path that end in .zip
zip_files = list(scanned_objects_dataset_path.glob('*.zip'))

# for each element in zip_files
#  extract the string of the filename without the extension
#  create a temporary directory with that name
#  extract the zip file into that directory
#  create a symbolic link from the temporary directory / materials / textures / texture.png to the temporary directory / meshes / texture.png
#  convert the obj file in the temporary directory / meshes / model.obj to gltf using the extracted file name as the output file name + .gltf and store it in the output directory
#  delete the temporary directory
for zip_file in zip_files:
    file_name = zip_file.stem
    temp_dir = output_path / file_name
    if not temp_dir.exists():
        os.mkdir(temp_dir)
    shutil.unpack_archive(str(zip_file), str(temp_dir))
    os.symlink(str(temp_dir / 'materials' / 'textures' / 'texture.png'), str(temp_dir / 'meshes' / 'texture.png'))
    os.system(f'obj2gltf -i {temp_dir / "meshes" / "model.obj"} -o {output_path / file_name}.gltf')
    shutil.rmtree(temp_dir)
    