from ultralytics import YOLO
import glob
import cv2

# Load YOLOv5 model pre-trained on the COCO dataset
model = YOLO("yolov5s.pt")  # Use "yolov5s.pt" (small), or replace with "yolov5m.pt"/"yolov5l.pt"/"yolov5x.pt" for larger models

# Define the categories for vehicles (based on COCO dataset labels)
vehicle_classes = [2, 3, 5, 7]  # Correspond to 'car', 'motorcycle', 'bus', 'truck'

images_folder = glob.glob("Traffic images/*.jpg")


for image_path in images_folder:
    # Perform object detection
    image = cv2.imread(image_path)

    results = model(image, conf=0.20)

    # Filter results for vehicles
    vehicle_results = []
    for result in results[0].boxes.data.tolist():  # Extract bounding boxes
        x1, y1, x2, y2, confidence, class_id = result
        if int(class_id) in vehicle_classes:  # Check if the object is a vehicle
            vehicle_results.append((x1, y1, x2, y2))

    # Number of vehicles detected
    no_of_vehicles = len(vehicle_results)
    print(no_of_vehicles)

    # Draw bounding boxes on the image
    for x1, y1, x2, y2 in vehicle_results:
        label = model.names[int(class_id)]
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)

    # Countdown timer
    if no_of_vehicles >= 30:
        countdown = 30 
    
    elif no_of_vehicles <= 5:
        countdown = 5
    
    else:
        countdown = no_of_vehicles 

    while countdown > 0:
        # Create a copy of the image to update the display
        display_image = image.copy()
        
        # Display the countdown text
        text = f"Seconds left: {countdown}"
        #cv2.putText()
        cv2.putText(display_image, text, (1, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

        # Show the image with the countdown
        cv2.imshow("Image", display_image)
        
        # Wait for 1 second
        if cv2.waitKey(1000) & 0xFF == ord('q'):  # Allow early exit with 'q'
            break

        # Decrement the countdown
        countdown -= 1

    # Clear the window after countdown ends
    cv2.destroyAllWindows()
