
This project demonstrates a simple implementation of object detection using the pre-trained YOLOv8 (nano) model from Ultralytics. The provided Python script loads an image, identifies objects within it, draws bounding boxes and labels, and saves the annotated image.

## Files in this Repository

  * `object.py`: The main Python script that performs the object detection.
  * `image.jpg`: The sample input image used for detection.
  * `output_image.jpg`: The resulting image after the script has run, showing the detected objects.

## How It Works

The `object.py` script performs the following steps:

1.  **Load Model**: It loads the pre-trained `yolov8n.pt` (nano version) model from Ultralytics.
2.  **Load Image**: It reads the input image (`image.jpg`) using OpenCV.
3.  **Perform Detection**: The model processes the image and identifies objects.
4.  **Annotate and Save**: The script uses the results to draw bounding boxes and labels on the image and saves this new image as `output_image.jpg`.
5.  **Display Results**: It prints a list of all detected objects and their confidence scores to the console.

## Requirements

You will need Python and the following libraries to run this script:

  * `ultralytics`
  * `opencv-python`

## How to Run

1.  **Clone or Download**: Get the files `object.py` and `image.jpg` and place them in the same directory.

2.  **Install Dependencies**: Open your terminal or command prompt and install the required libraries using pip:

    ```bash
    pip install ultralytics opencv-python
    ```

3.  **Execute the Script**: Navigate to the directory containing the files and run the script:

    ```bash
    python object.py
    ```

4.  **Check the Output**:

      * A new file, `output_image.jpg`, will be created in the same directory.
      * Your terminal will display the detection progress and a final list of detected objects.

    **Example Console Output:**

    ```
    Starting object detection...
    Loading model...
    Model loaded.
    Loading image from image.jpg...
    Image loaded.
    Performing object detection...
    Detection completed.
    Annotating image...
    Saving output image...
    Output image saved.
    Detected objects:
    bus: 0.91
    car: 0.89
    airplane: 0.86
    car: 0.84
    person: 0.81
    car: 0.80
    truck: 0.67
    bicycle: 0.66
    traffic light: 0.62
    car: 0.60
    ...
    ✅ Detection complete! Check 'output_image.jpg' for results.
    ```

## Example Result

The script processes the input image and generates an output image with all detected objects clearly labeled.

**Input (`image.jpg`)**

**Output (`output_image.jpg`)**
