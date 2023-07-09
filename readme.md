## Converting the Google Scanned Object Dataset

The Google scanned object dataset is in sdf format which references the mesh files in obj format.

This code attempt to convered the sdf format to gltf format.

The basic logic is, given an output directory and a path to the dataset, the code will:
1. Create the output directory
2. create a list of the dataset's .zip files
3. For each .zip file in the list, it will:
    1. Copy the .zip file to a temporary directory
    2. Unzip the .zip file
    3. link the texture to the meshes directory
    4. call obj2gltf to convert the obj file to gltf file, using the .zip file's name as the gltf file's name
    5. Move the gltf file to the output directory
    6. Delete the temporary directory


