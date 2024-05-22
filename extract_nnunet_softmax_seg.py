# Converts SoftMax output from nnUNet deep learning model
#   from npz to nifti format

import pickle
import numpy as np
import SimpleITK as sitk

segmentation_softmax = 'nnUNet_trained_models/nnUNet_prediction/chop_000.npz' # output by --save_npz flag in nnUNet_predict command
out_fname = 'nnUNet_trained_models/nnUNet_prediction/chop_000_seg_softmax.nii.gz'

file_to_read = open(segmentation_softmax[:-4] + ".pkl", "rb")
properties_dict = pickle.load(file_to_read)

segmentation_softmax = np.load(segmentation_softmax)
segmentation_softmax = segmentation_softmax['softmax']

# get initial parameters
current_shape = segmentation_softmax.shape
shape_original_after_cropping = properties_dict.get('size_after_cropping')
shape_original_before_cropping = properties_dict.get('original_size_of_raw_data')

# handle multiple labels
seg_old_spacing = segmentation_softmax[1,:,:,:] # grab only the label=1
## if want to add all layers together, uncomment the lines below
# for label_layer in range(1, segmentation_softmax.shape[0]-1):
#     ind = label_layer+1
#     seg_old_spacing = seg_old_spacing + segmentation_softmax[ind,:,:,:]

# put result into bbox of cropping
bbox = properties_dict.get('crop_bbox')
print(bbox)

if bbox is not None:
    seg_old_size = np.zeros(shape_original_before_cropping)
    for c in range(3):
        bbox[c][1] = np.min((bbox[c][0] + seg_old_spacing.shape[c], shape_original_before_cropping[c]))
    seg_old_size[bbox[0][0]:bbox[0][1],
    bbox[1][0]:bbox[1][1],
    bbox[2][0]:bbox[2][1]] = seg_old_spacing
else:
    seg_old_size = seg_old_spacing

seg_old_size_postprocessed = seg_old_size

# save to disk
seg_resized_itk = sitk.GetImageFromArray(seg_old_size_postprocessed.astype(np.float32))
seg_resized_itk.SetSpacing(properties_dict['itk_spacing'])
seg_resized_itk.SetOrigin(properties_dict['itk_origin'])
seg_resized_itk.SetDirection(properties_dict['itk_direction'])
sitk.WriteImage(seg_resized_itk, out_fname)
