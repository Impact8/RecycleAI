import torchvision.models
import torch

classes = ["landfill", "compost", "recycle"]

num_classes = len(classes)

def build_model():
    model = torchvision.models.resnet18(pretrained=True)
    in_feature = model.fc.in_features
    model.fc = torch.nn.Linear(in_feature, num_classes)
    model.eval()               
    return model

def get_device():
    if torch.cuda.is_available():
        return "cuda"
    elif torch.mps.is_available():
        return "mps"
    else:
        return "cpu"
    



