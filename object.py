# Object Detection using YOLOv8 (Ultralytics)
# --------------------------------------------
# This code loads a pretrained model, detects objects in an image,
# and saves an output image with bounding boxes and labels.

from ultralytics import YOLO
import cv2

print("Starting object detection...")

# Step 1: Load the pre-trained YOLOv8 model
# "yolov8n.pt" = nano version (fast and small)
print("Loading model...")
model = YOLO('yolov8n.pt')
print("Model loaded.")

# Step 2: Load your input image
image_path = "image.jpg"       # Replace with your actual image filename
print(f"Loading image from {image_path}...")
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
    exit(1)
print("Image loaded.")

# Step 3: Perform object detection
print("Performing object detection...")
results = model(image)
print("Detection completed.")

# Step 4: Visualize the results and save labeled output
# The result[0].plot() automatically draws boxes and labels
print("Annotating image...")
annotated_image = results[0].plot()

# Step 5: Save the output image
print("Saving output image...")
cv2.imwrite("output_image.jpg", annotated_image)
print("Output image saved.")

# Step 6: Display detected objects in console
print("Detected objects:")
for box in results[0].boxes.data.tolist():
    x1, y1, x2, y2, confidence, class_id = box
    label = model.names[int(class_id)]
    print(f"{label}: {confidence:.2f}")

print("✅ Detection complete! Check 'output_image.jpg' for results.")
