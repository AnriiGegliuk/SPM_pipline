import os
import argparse
from utils.identify_nii import find_images

# creating argparse arguments to run the function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find and count medical image files in a folder and its subfolders.')
    parser.add_argument('folder_path', type=str, help='Path to the folder to be searched')
    
    args = parser.parse_args()
    find_images(args.folder_path)