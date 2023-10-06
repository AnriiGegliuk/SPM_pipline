import pandas as pd
import numpy as np
import nibabel as nib

def align_to_template_w_intens(raw_img, raw_header, template_header):
    """
    Align the raw image to the template image based on the affine parameters from the template header.
    
    Parameters:
        raw_img (numpy.ndarray): The raw image data.
        raw_header (nibabel header): The header of the raw image.
        template_header (nibabel header): The header of the template image.
    
    Returns:
        numpy.ndarray: The aligned image.
        nibabel header: The updated header for the aligned image.
    """
    affine_params = {
        'qform_code': template_header['qform_code'],
        'sform_code': template_header['sform_code'],
        'quatern_b': template_header['quatern_b'],
        'quatern_c': template_header['quatern_c'],
        'quatern_d': template_header['quatern_d'],
        'qoffset_x': template_header['qoffset_x'],
        'qoffset_y': template_header['qoffset_y'],
        'qoffset_z': template_header['qoffset_z'],
        'srow_x': raw_header['srow_x'] * 10,
        'srow_y': raw_header['srow_y'] * 10,
        'srow_z': raw_header['srow_z'] * 10
    }
    
    for key, value in affine_params.items():
        raw_header[key] = value
    
    return raw_img, raw_header


def rotate_axial_slices(image_data, degrees=180):
    """
    Rotates the axial slices of the image by the specified degrees.

    Parameters:
        image_data (numpy.ndarray): The 3D image data.
        degrees (int): The degrees by which to rotate the axial slices. Default is 180.

    Returns:
        numpy.ndarray: The image data with rotated axial slices.
    """
    rotated_image_data = np.copy(image_data)
    
    for z in range(image_data.shape[2]):
        rotated_image_data[:, :, z] = np.rot90(image_data[:, :, z], k=degrees//90)
        
    return rotated_image_data






# def align_orientation_to_template_wo_intens(raw_img, raw_header, template_header):
#     """
#     Align the orientation of the raw image to match that of the template.

#     Parameters:
#         raw_img (numpy.ndarray): The raw image data.
#         raw_header (nibabel header): The header of the raw image.
#         template_header (nibabel header): The header of the template image.

#     Returns:
#         numpy.ndarray: The original raw image (unchanged).
#         nibabel header: The updated header for the raw image.
#     """

#     orientation_params = {
#         'quatern_b': template_header['quatern_b'],
#         'quatern_c': template_header['quatern_c'],
#         'quatern_d': template_header['quatern_d'],
#         'srow_x': template_header['srow_x'],
#         'srow_y': template_header['srow_y'],
#         'srow_z': template_header['srow_z']
#     }

#     for key, value in orientation_params.items():
#         raw_header[key] = value

#     return raw_img, raw_header