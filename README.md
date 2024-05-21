## generate nnUNet softmax map

Example code to extract a spatial probability (softmax) map for a model inference (after running `nnUNet_predict` command with the `--save_npz` flag). Uses the original image size to pad the segmentation result (based on the bounding box) and converts npz to NIfTI file format.

Based on:
- https://github.com/MIC-DKFZ/nnUNet/issues/620
- https://github.com/MIC-DKFZ/nnUNet/issues/1050
- https://github.com/MIC-DKFZ/nnUNet/issues/1076
- https://github.com/MIC-DKFZ/nnUNet/issues/1337
