# stylegan3_train
A stylegan3 refactored code for easy inference and taining.

## Instructions for initialization
git clone https://github.com/waleedrazakhan92/stylegan3_train.git

```
cd stylegan3_train

chmod +x *

./run_setup.txt
```

## Config file instructions

Set all the parameters in the config file according to your dataset.

**path_raw_images** is the path to your images before they are being preprocessed for training.

**path_corrupt_images** is the path to move images in case there are unwanted images in the raw dataset.

**path_processed_images** is the path where the training dataset images are to be moved.

**resolution** set the image resolution for the training.

**resume_ckpt** is the path to a pretrained model in case you want to do transfer learning. Or else set it to 'none'.

**experiment_dir** is the directory where model checkpoints and test images will be stored during training process.

Set the rest of the training details according to official training configurations https://github.com/NVlabs/stylegan3/blob/main/docs/configs.md

**inference_ckpt** is the path to the model file for inference.

**gen_images_path** is the path where synthetic images will be stored.

**num_images** is the number of images you want to generate.

**trunc** truncation index.

# Dataset Preparation
```
./run_check_eligibility.txt
```
```
./run_dataset_tool.txt
```
# Training
```
./run_train.txt
```
# Inference
```
./run_inference.txt
```
