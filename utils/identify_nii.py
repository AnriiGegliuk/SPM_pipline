import os
from collections import defaultdict


def find_images(folder_path):
    """
    This function traverses through the given folder and its subfolders to detect 
    and count the '.nii', '.dcm', and other files. It prints the counts, paths, 
    and the folder with the most '.nii' files.

    :param folder_path: The path to the folder to be searched.
    :return: A dictionary containing the count and list of paths of '.nii' and '.dcm' files.
    """
    medical_images = defaultdict(lambda: {'count': 0, 'paths': []})
    most_nii_folder = {'folder': None, 'count': 0}
    
    for foldername, subfolders, filenames in os.walk(folder_path):
        local_nii_count = 0
        total_files_count = len(filenames)
        
        for filename in filenames:
            if filename.endswith('.nii'):
                medical_images['.nii']['count'] += 1
                medical_images['.nii']['paths'].append(os.path.join(foldername, filename))
                local_nii_count += 1
            elif filename.endswith('.dcm'):
                medical_images['.dcm']['count'] += 1
                medical_images['.dcm']['paths'].append(os.path.join(foldername, filename))
        
        if local_nii_count > most_nii_folder['count']:
            most_nii_folder = {'folder': foldername, 'count': local_nii_count}
        
        print(f"Total number of files in folder '{foldername}': {total_files_count}")
    
    print("Number of .nii files: ", medical_images['.nii']['count'])
    print("Paths of .nii files: ", medical_images['.nii']['paths'])
    print("Number of .dcm files: ", medical_images['.dcm']['count'])
    print("Paths of .dcm files: ", medical_images['.dcm']['paths'])
    
    if most_nii_folder['folder']:
        print(f"The folder '{most_nii_folder['folder']}' contains the most .nii files: {most_nii_folder['count']}")
    
    return medical_images   