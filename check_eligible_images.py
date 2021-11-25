from config_file import path_raw_images,path_corrupt_images
from PIL import Image
import numpy as np
from glob import glob
import shutil
import os
## check eligible images
def check_eligible_images(path_raw_images, path_corrupt_images):
    if not os.path.isdir(path_corrupt_images):
        os.mkdir(path_corrupt_images)

    all_images = glob(path_raw_images+'/*')

    for i in range(0,len(all_images)):
        img = Image.open(all_images[i])
        if len(np.shape(img))!=3:
            print('Moving ', all_images[i],np.shape(img))
            shutil.move(all_images[i], path_corrupt_images)
        elif np.shape(img)[2]!=3:
            shutil.move(all_images[i], path_corrupt_images)
            print('Moving ', all_images[i],np.shape(img))

    print('Total number of images moved :', len(os.listdir(path_corrupt_images)))

def main():
    check_eligible_images(path_raw_images,path_corrupt_images)

main()