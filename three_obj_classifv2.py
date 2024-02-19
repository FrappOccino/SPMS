import cv2
from ultralytics import YOLO
import numpy as np
from PIL import Image, ImageTk



def obj_classifier(ui_label, obj_mdl_path, veh_mdl_path, vid_path, frame_w, frame_h, data_q_class, data_q_has_class):
    # YOLO model for general object detection
    yolo_objects = YOLO(obj_mdl_path)

    # YOLO model for car and motorcycle detection
    yolo_vehicles = YOLO(veh_mdl_path, "v8")

    # Open the video file
    cap = cv2.VideoCapture(vid_path)

    # Define the ROI for vehicle detection
    roi_points = np.array([[(0, 175), (1270, 175), (1270, 816), (0, 816)]], dtype=np.int32)

    user_vehicle_classification = None  # Initialize the variable

    if cap.isOpened():
        while cap.isOpened():
            # Read the video frame by frame
            ret, frame = cap.read()
            if ret:
                # Draw the ROI for vehicle detection on the frame
                cv2.polylines(frame, [roi_points], isClosed=True, color=(0, 0, 255), thickness=2)

                # Apply the YOLO model for car and motorcycle detection to the frame
                results_vehicles = yolo_vehicles.predict(source=frame)

                # Flags to keep track of vehicle and object classification
                car_detected = False
                staff_detected = False
                teaching_detected = False
                non_teaching_detected = False
                motorcycle_detected = False
                car_has_class = False

                # Check if a car is Inside ROI
                for result_vehicle in results_vehicles:
                    for i in range(len(result_vehicle.boxes.xyxy)):
                        x, y = int(result_vehicle.boxes.xyxy[i][0]), int(result_vehicle.boxes.xyxy[i][1])
                        if cv2.pointPolygonTest(roi_points, (x, y), False) >= 0:
                            # Car is inside the ROI, proceed with drawing and classification
                            class_name_vehicle = yolo_vehicles.names[int(result_vehicle.boxes.cls[i])]

                            # Filter only desired classes (e.g., "car" and "motorcycle")
                            if class_name_vehicle in ["car", "motorcycle"]:
                                car_detected = True
                                if class_name_vehicle == 'motorcycle':
                                    motorcycle_detected = True

                                # Draw bounding box for the car
                                x1, y1, x2, y2 = map(int, result_vehicle.boxes.xyxy[i])
                                label = f'{class_name_vehicle}: {result_vehicle.boxes.conf[i]:.2f}'
                                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                                frame = cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                                # Extract sub-region within car bounding box
                                sub_roi = frame[y1:y2, x1:x2]

                                # Apply the YOLO model for staff, teaching, non_teaching to the sub-region
                                results_objects = yolo_objects.predict(source=sub_roi)

                                # Check if objects are inside sub-ROI
                                for result_obj in results_objects:
                                    for j in range(len(result_obj.boxes.xyxy)):
                                        x_obj, y_obj = int(result_obj.boxes.xyxy[j][0]), int(result_obj.boxes.xyxy[j][1])

                                        # Convert object coordinates to global frame
                                        x_obj_global, y_obj_global = x_obj + x1, y_obj + y1

                                        if cv2.pointPolygonTest(roi_points, (x_obj_global, y_obj_global), False) >= 0:
                                            # Object is inside the ROI, proceed with drawing and classification
                                            # Draw bounding box
                                            x1_obj, y1_obj, x2_obj, y2_obj = map(int, result_obj.boxes.xyxy[j])
                                            label_obj = f'{yolo_objects.names[int(result_obj.boxes.cls[j])]}: {result_obj.boxes.conf[j]:.2f}'
                                            frame = cv2.rectangle(frame, (x1_obj + x1, y1_obj + y1), (x2_obj + x1, y2_obj + y1),
                                                                  (255, 0, 0), 2)
                                            frame = cv2.putText(frame, label_obj, (x1_obj + x1, y1_obj + y1 - 10),
                                                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                                            # Check for object classifications
                                            if yolo_objects.names[int(result_obj.boxes.cls[j])] == 'staff':
                                                staff_detected = True
                                                car_has_class = True
                                            elif yolo_objects.names[int(result_obj.boxes.cls[j])] == 'teaching':
                                                teaching_detected = True
                                                car_has_class = True
                                            elif yolo_objects.names[int(result_obj.boxes.cls[j])] == 'non_teaching':
                                                non_teaching_detected = True
                                                car_has_class = True


                #print(str(car_has_class))
                # Determine the user_vehicle_classification
                if car_detected:
                    if staff_detected:
                        user_vehicle_classification = 'staff'
                    elif teaching_detected:
                        user_vehicle_classification = 'teaching'
                    elif non_teaching_detected:
                        user_vehicle_classification = 'non_teaching'
                    elif motorcycle_detected:
                        user_vehicle_classification = 'motorcycle'
                    else:
                        user_vehicle_classification = None



                frame_resized = cv2.resize(frame, (frame_w, frame_h))
                frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame_rgb)
                image_tk = ImageTk.PhotoImage(image)

                ui_label.config(image=image_tk)
                ui_label.image = image_tk

                data_q_has_class.put(car_has_class)
                data_q_class.put(user_vehicle_classification)

    else:
        img = Image.open(r'C:\Users\DICT\Desktop\SPMS\Images\no_video.png')  # Replace with the path to your image
        image_resize = img.resize((frame_w, frame_h))

        image_tk = ImageTk.PhotoImage(image_resize)

        ui_label.config(image=image_tk)
        ui_label.image = image_tk
