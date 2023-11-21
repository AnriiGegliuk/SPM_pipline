import os
import nibabel as nib
import numpy as np
from scipy.ndimage import binary_fill_holes


def brain_mask_generation(dir_path):
    print("Function brain_mask_generation is called.")
    # looking for 3 files
    c1_path = os.path.join(dir_path, 'c1T2.nii')
    c2_path = os.path.join(dir_path, 'c2T2.nii')
    c3_path = os.path.join(dir_path, 'c3T2.nii')
    # printing infor about files
    print(f"Looking for c1 at {c1_path}")
    print(f"Looking for c2 at {c2_path}")
    print(f"Looking for c3 at {c3_path}")

    # giving an error message if path our files not exist
    if not os.path.exists(c1_path) or not os.path.exists(c2_path) or not os.path.exists(c3_path):
        print("One or more required files do not exist in the specified directory.")
        return 
    
    # loading data
    c1 = nib.load(c1_path)
    c2 = nib.load(c2_path)
    c3 = nib.load(c3_path)

    # loading data as an image
    c1_data = c1.get_fdata()
    c2_data = c2.get_fdata()
    c3_data = c3.get_fdata()

    mask = np.zeros(c1_data.shape, dtype=c1_data.dtype)
    mask[(c1_data > 0) | (c2_data > 0) | (c3_data > 0)] = 1
    filled_mask = binary_fill_holes(mask).astype(mask.dtype)

    # saving mask as img
    filled_mask_img = nib.Nifti1Image(filled_mask, c1.affine, c1.header)
    output_path = os.path.join(dir_path, 'brain_mask_filled.nii')
    nib.save(filled_mask_img, output_path)
    print(f"Saved filled brain mask to {output_path}")