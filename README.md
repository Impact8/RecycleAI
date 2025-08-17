RecycleAI is a simple AI-powered app that classifies waste items into landfill, compost, or recycle using a ResNet18 model.  
Built with Streamlit + PyTorch.

---
To Start

Clone this repo:
```bash
git clone https://github.com/your-username/recycleai.git
cd recycleai

python3 -m venv venv
source venv/bin/activate   # on Mac
venv\Scripts\activate      # on Windows

pip install -r requirements.txt

streamlit run app.py


How it Works: 
Upload a photo of trash (png/jpg/jpeg)
The model processes the image and predicts whether it belongs in:
-Landfill
-Compost
-Recycle

