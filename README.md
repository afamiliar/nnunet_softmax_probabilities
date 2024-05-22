## generate nnUNet softmax map

Example code to extract a spatial probability (softmax) map for a model inference (after running `nnUNet_predict` command with the `--save_npz` flag). Uses the original image size to pad the segmentation result (based on the bounding box) and converts npz to NIfTI file format. Set to generate the map for label=1 (background=0; for >1 labels, see lines 23-26). Tested only with 3D segmentations.

Based on:
- https://github.com/MIC-DKFZ/nnUNet/issues/620
- https://github.com/MIC-DKFZ/nnUNet/issues/1050
- https://github.com/MIC-DKFZ/nnUNet/issues/1076
- https://github.com/MIC-DKFZ/nnUNet/issues/1337
