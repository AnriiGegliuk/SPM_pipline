import os
import argparse
from utils.brain_mask import brain_mask_generation

# mask generation
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Please type the file path to generate brain mask based on output segmentation after SPM')
    parser.add_argument('folder_path', type=str, help='Path to the directory containing c1T2.nii, c2T2.nii, and c3T2.nii')
    
    args = parser.parse_args()
    brain_mask_generation(args.folder_path)

