from PIL import Image
import torch
import torchvision.transforms as transforms


def load_image_for_user(file):
    img = Image.open(file)
    rgb_img = img.convert("RGBA")
    return rgb_img

def load_image_for_model(file):
    size = 224, 224
    img1 = Image.open(file)
    conv_rgb = img1.convert("RGB")
    fully_proc_image = conv_rgb.resize(size)

    transform = transforms.ToTensor()

    return fully_proc_image


