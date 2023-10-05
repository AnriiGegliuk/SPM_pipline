Brain masking improvement pipline


This project is focused on processing and analyzing medical images, primarily those in the .nii (Neuroimaging Informatics Technology Initiative) and .dcm (DICOM) formats.


# Main Components:

### Image Detection and Counting:
* A script traverses through specified folders and their subfolders to detect and count **.nii** and **.dcm** files. It provides insights into the number of medical images present in each folder and the paths to these images. It also identifies the folder containing the most **.nii** files.

### Brain Mask Generation:
* Based on segmentation results from **SPM** (Statistical Parametric Mapping), a brain mask is generated by a separate script. This script searches for **c1T2.nii**, **c2T2.nii**, and **c3T2.nii** files in the specified directory, and if found, processes them to create a filled brain mask, which is subsequently saved as brain_mask_filled.nii. If any of the required files are missing, the script informs the user about the absence of these necessary files.
