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
    img_resized = conv_rgb.resize(size)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
        )
    ])
    img_tensor = transform(img_resized)
    img_tensor = img_tensor.unsqueeze(0)
    
    return img_tensor


