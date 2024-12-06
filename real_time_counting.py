import cv2 
from ultralytics import YOLO

cap = cv2.VideoCapture("cars.mp4")

model = YOLO("yolov5s.pt") 

vehicle_classes = [2, 3, 5, 7] 

def find_centre(x1, y1, x2, y2):
    cx, cy = ((x1+x2)//2, (y1+y2)//2)
    return cx, cy 

count = 0
detect = []
while True:
    ret, frame = cap.read() 

    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Filter results for vehicles
    vehicle_results = []
    for result in results[0].boxes.data.tolist():  # Extract bounding boxes
        x1, y1, x2, y2, confidence, class_id = result
        if int(class_id) in vehicle_classes:  # Check if the object is a vehicle
            vehicle_results.append((x1, y1, x2, y2))

    cv2.line(frame, (150, 40), (500, 40), color=(255, 0, 0), thickness=2)

    # Draw bounding boxes on the image
    for x1, y1, x2, y2 in vehicle_results:
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=1)

        #Find the center point of the rectangle
        center = find_centre(x1, y1, x2, y2)

        #Append calculated center to the list 'detect'
        detect.append(center)
        cv2.circle(frame, center, 4, (0, 255, 0), -1)

        for (x, y) in detect:
            if 150 <= x <= 500 and y == 40:
                count += 1
            
            #Draw a line from point (150, 40) to point (500, 40)
            cv2.line(frame, (150, 40), (500, 40), (0, 125, 230), 2)

            #Remove the counted center point from 'detect' list
            detect.remove((x, y))
        
        cv2.putText(frame, f"Vehicle Count: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    cv2.imshow("Image", frame) 
    
    #press 'q' to stop the execution
    if cv2.waitKey(20) & 0xff == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows() 

