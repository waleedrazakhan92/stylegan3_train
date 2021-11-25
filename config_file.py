path_raw_images='raw_images/'
path_corrupt_images='corrupt_images/'
path_processed_images='processed_images/'
resolution='1024x1024'
resume_ckpt='none' #'none' if you want to start training from scratch 
experiment_dir='piccaso_experiment/' 
#----------------------------------------
#Train options
cfg='stylegan3-r'
aug='ada'
gpus=1
batch=32
batch_gpu=8
gamma=2
mirror=1
kimg=5000
snap=1
#----------------------------------------
#Test options
inference_ckpt='stylegan3/pretrained/stylegan3-r-ffhq-1024x1024.pkl'
gen_images_path='generated_images/'
num_images=10
trunc=0.7