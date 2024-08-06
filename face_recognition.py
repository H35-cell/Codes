import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Load pre-trained Haar cascade model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image, faces

# Function to open an image file
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("path_to_image", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = cv2.imread(file_path)
        image, faces = detect_faces(image)
        if faces:
            display_image(image)
        else:
            messagebox.showinfo("Face Detection", "No faces detected.")

# Function to display an image in the Tkinter window
def display_image(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    image_tk = ImageTk.PhotoImage(image_pil)
    label_img.configure(image=image_tk)
    label_img.image = image_tk

# Create the main window
root = tk.Tk()
root.title("Face Detection and Recognition")

# Create a button to open an image file
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)

# Create a label to display the image
label_img = tk.Label(root)
label_img.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
