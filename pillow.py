from PIL import Image


image_path_list = ['Black & White Simple Initial Circle Badge Logo.png', 'Brown Yellow Green Illustration Circle Badge Banana Snack Logo.png', '1. çıkartma.png']


image_list = [Image.open(file) for file in image_path_list]


image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=1000, # in milliseconds
            loop=0)