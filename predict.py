from ultralytics import YOLO

# Load the trained uniform detection model
model = YOLO("weights/best.pt")

# Predict on an input image
results = model.predict(
    source="examples/input.jpg",
    save=True
)

print("Prediction completed!")