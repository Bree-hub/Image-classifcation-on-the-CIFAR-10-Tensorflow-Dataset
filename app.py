import uvicorn
from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
model_path = 'model/model5.h5'  # Update this with the path to your model
model = load_model(model_path)

# Define class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image file
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    img = img.resize((32, 32))  # Resize to the model's expected input size
    
    # Preprocess the image
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    return {"predicted_class": predicted_class, "confidence": float(confidence)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
