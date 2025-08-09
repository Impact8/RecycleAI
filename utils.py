from PIL import Image
import torch
import torchvision.transforms as transforms


def load_image_for_user(file):
    img = Image.open(file)
    rgb_img = img.convert("RGBA")
    return rgb_img
