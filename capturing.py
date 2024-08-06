import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np

# Load pre-trained models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Image feature extraction model (ResNet)
resnet = models.resnet50(pretrained=True)
resnet.eval()
resnet.to(device)

# Text generation model (Transformer-based)
# For demonstration, we'll use a simplified model. In practice, you would use a pre-trained captioning model.
class SimpleCaptioningModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    
    def generate_caption(self, features):
        # Simple placeholder for demonstration
        # Replace with an actual caption generation model
        return "This is a placeholder caption."

captioning_model = SimpleCaptioningModel()

# Preprocessing functions
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(image).unsqueeze(0).to(device)

def extract_features(image_tensor):
    with torch.no_grad():
        features = resnet(image_tensor)
    return features

# Function to process and display the image and its caption
def process_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)
        image_tensor = preprocess_image(image)
        features = extract_features(image_tensor)
        caption = captioning_model.generate_caption(features)
        display_image_with_caption(image, caption)

def display_image_with_caption(image, caption):
    image = image.resize((400, 400))
    image_tk = ImageTk.PhotoImage(image)
    label_img.configure(image=image_tk)
    label_img.image = image_tk
    label_caption.configure(text=caption)

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Captioning")

# Create GUI elements
btn_open = tk.Button(root, text="Open Image", command=process_image)
btn_open.pack(pady=10)

label_img = tk.Label(root)
label_img.pack(padx=10, pady=10)

label_caption = tk.Label(root, text="", wraplength=400)
label_caption.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()