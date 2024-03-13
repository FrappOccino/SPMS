from three_obj_classifv2 import obj_classifier
from customtkinter import *
import cv2
from tkinter import *
import threading
from queue import Queue
import subprocess
from PIL import ImageGrab, Image
import os
from CTkMessagebox import CTkMessagebox
from CTkToolTip import *
from tktooltip import ToolTip
from PIL import Image, ImageTk
from util import get_parking_spots_bboxes, empty_or_not




#variables
#obj detection model
user_classif_model = r'C:\Users\DICT\Desktop\Entrance vid\3_class_data_set\3_classification_weights_v2.1\best.pt' # teaching, non_teaching, staff
yolo_pretrained_model = r"C:\Users\DICT\Desktop\SPMS\weights\yolov8n.pt" #for vehicle classification
video_pathD = r'C:\Users\DICT\Desktop\Entrance vid\3_class_data_set\3class_vid3.mp4'

#parking detection
maskA = r'C:/Users/DICT/Desktop/SPMS/Images/SAM.png'
video_pathA = r'C:/Users/DICT/Desktop/SPMS/Vid/SA_vid_loop.mp4'

maskB = r'C:/Users/DICT/Desktop/SPMS/Images/SBM.png'
video_pathB =r'C:/Users/DICT/Desktop/SPMS/Vid/SB_vid_loop.mp4'

maskC = r'C:/Users/DICT/Desktop/SPMS/Images/C.png'
video_pathC ='C:/Users/DICT/Desktop/SPMS/Vid/SC_vid_loop.mp4'

parking_lot_1 ='Parking Lot A'
parking_lot_2 ='Parking Lot B'
parking_lot_3 ='Parking Lot C'


capA = cv2.VideoCapture(video_pathA)
capB = cv2.VideoCapture(video_pathB)
capC = cv2.VideoCapture(video_pathC)




frame_w = 600
frame_h = 500

data_queue = Queue()
data_queue_spot = Queue()
data_q_class = Queue()
data_q_has_class = Queue()

update_lock = threading.Lock()

#video label for A window (Display)
def video_a_label(event):
    global video_a_path_entry, mask_a_path_entry
    print('vid is clicked')
    vid_a_window = CTkToplevel(app)
    vid_a_window.title('Video A')
    vid_a_window.geometry('500x200')
    vid_a_window.resizable(False, False)
    vid_a_window.wm_attributes('-topmost', True)

    #widgets
    #label widgets
    video_path_Label1 = CTkLabel(vid_a_window, text="Video source:")
    mask_path_Label1 = CTkLabel(vid_a_window, text="Mask Path:")


    #entry widgets
    video_a_path_entry = CTkEntry(vid_a_window, width=350, placeholder_text="Camera path")
    mask_a_path_entry = CTkEntry(vid_a_window, width=350, placeholder_text="Camera mask")


    #button widgets
    save_vid_a = CTkButton(vid_a_window, text='save',command=lambda: update_values_vid_a(mask_a_path_entry,video_a_path_entry, capA))
    video_a_dir = CTkButton(vid_a_window, width=30, text='...', command=lambda: open_directory(video_a_path_entry))
    mask_a_dir = CTkButton(vid_a_window, width=30, text='...', command=lambda: open_directory(mask_a_path_entry))

    #widget initialization
    video_path_Label1.place(x=10, y=30)
    video_a_path_entry.place(x=90, y=30)
    video_a_dir.place(x=450, y=30)
    mask_path_Label1.place(x=10, y=90)
    mask_a_path_entry.place(x=90, y=90)
    mask_a_dir.place(x=450, y=90)
    save_vid_a.place(x=185,y=150)

#video label for B window (Display)
def video_b_label(event):
    global video_b_path_entry, mask_b_path_entry
    print('vid is clicked')
    vid_b_window = CTkToplevel(app)
    vid_b_window.title('Video B')
    vid_b_window.geometry('500x200')
    vid_b_window.resizable(False, False)
    vid_b_window.wm_attributes('-topmost', True)

    #widgets
    ##label widgets
    video_path_Label2 = CTkLabel(vid_b_window, text="Video source:")
    mask_path_Label2 = CTkLabel(vid_b_window, text="Mask Path:")


    ##entry widgets
    video_b_path_entry = CTkEntry(vid_b_window, width=350, placeholder_text="Camera path")
    mask_b_path_entry = CTkEntry(vid_b_window, width=350, placeholder_text="Camera mask")


    ##button widgets
    save_vid_b = CTkButton(vid_b_window, text='save',command=lambda: update_values_vid_b(mask_b_path_entry,video_b_path_entry, capB))
    video_b_dir = CTkButton(vid_b_window, width=30, text='...', command=lambda: open_directory(video_b_path_entry))
    mask_b_dir = CTkButton(vid_b_window, width=30, text='...', command=lambda: open_directory(mask_b_path_entry))

    ##widget initialization
    video_path_Label2.place(x=10, y=30)
    video_b_path_entry.place(x=90, y=30)
    video_b_dir.place(x=450, y=30)
    mask_path_Label2.place(x=10, y=90)
    mask_b_path_entry.place(x=90, y=90)
    mask_b_dir.place(x=450, y=90)
    save_vid_b.place(x=185,y=150)

#video label for A window (Display)   
def video_c_label(event):
    global video_c_path_entry, mask_c_path_entry
    print('vid is clicked')
    vid_c_window = CTkToplevel(app)
    vid_c_window.title('Video C')
    vid_c_window.geometry('500x200')
    vid_c_window.resizable(False, False)
    vid_c_window.wm_attributes('-topmost', True)

    #widgets
    ##label widgets
    video_path_Label3 = CTkLabel(vid_c_window, text="Video source:")
    mask_path_Label3 = CTkLabel(vid_c_window, text="Mask Path:")


    ##entry widgets
    video_c_path_entry = CTkEntry(vid_c_window, width=350, placeholder_text="Camera path")
    mask_c_path_entry = CTkEntry(vid_c_window, width=350, placeholder_text="Camera mask")


    ##button widgets
    save_vid_c = CTkButton(vid_c_window, text='save',command=lambda: update_values_vid_c(mask_c_path_entry,video_c_path_entry, capC))
    video_c_dir = CTkButton(vid_c_window, width=30, text='...', command=lambda: open_directory(video_c_path_entry))
    mask_c_dir = CTkButton(vid_c_window, width=30, text='...', command=lambda: open_directory(mask_c_path_entry))

    ##widget initialization
    video_path_Label3.place(x=10, y=30)
    video_c_path_entry.place(x=90, y=30)
    video_c_dir.place(x=450, y=30)
    mask_path_Label3.place(x=10, y=90)
    mask_c_path_entry.place(x=90, y=90)
    mask_c_dir.place(x=450, y=90)
    save_vid_c.place(x=185,y=150)
    
def update_values_vid_a(entry_mask, entry_video, cap):
    global maskA, video_pathA
    with update_lock:
        maskA = entry_mask.get()
        new_video_path = entry_video.get()

    if video_pathA != new_video_path:
        with update_lock:
            video_pathA = new_video_path
            cap.release()
            cap.open(video_pathA)
            
def update_values_vid_b(entry_mask, entry_video, cap):
    global maskB, video_pathB
    with update_lock:
        maskB = entry_mask.get()
        new_video_path = entry_video.get()

    if video_pathB != new_video_path:
        with update_lock:
            video_pathB = new_video_path
            cap.release()
            cap.open(video_pathB)

def update_values_vid_c(entry_mask, entry_video, cap):
    global maskC, video_pathC
    with update_lock:
        maskC = entry_mask.get()
        new_video_path = entry_video.get()

    if video_pathC != new_video_path:
        with update_lock:
            video_pathC = new_video_path
            cap.release()
            cap.open(video_pathC)

#Segements the parking lots spaces
def segment_vid(mask, video_path, label, frame_w, frame_h, data_queue, data_queue_spot, lot_segment, cap):
    global avail ,f_element,frame_seg
    while True:
        img_mask = cv2.imread(mask, 0)
        connected_components = cv2.connectedComponentsWithStats(img_mask, 4, cv2.CV_32S)
        spots = get_parking_spots_bboxes(connected_components)

        # Initialize the list to store spot status
        spots_status = [None for j in spots]

        ret, frame = cap.read()

        frame_seg = (lot_segment,frame)

        if ret:
            for spot_indx, spot in enumerate(spots):
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                spot_status = empty_or_not(spot_crop)
                spots_status[spot_indx] = spot_status

                # Display spot index on the frame
                cv2.putText(frame, str(spot_indx + 1), (x1 + w // 2, y1 + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 2)

            # Rest of the code for visualization and updating the frame
            for spot_indx, spot in enumerate(spots):
                spot_status = spots_status[spot_indx]
                x1, y1, w, h = spots[spot_indx]

                # Draw rectangles based on spot status
                if spot_status:
                    frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
                else:
                    frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

            # Generate and print empty spot indices after processing the frame
            empty_spots_indices = [f"{lot_segment}{index + 1}" for index, status in enumerate(spots_status) if status]
            if empty_spots_indices:
                f_element = (lot_segment,empty_spots_indices[0])
            else:
                f_element = (lot_segment)
            #print(f_element)

            # Visualization of the frame
            frame_resized = cv2.resize(frame, (frame_w, frame_h))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            image_tk = ImageTk.PhotoImage(image)

            label.config(image=image_tk)
            label.image = image_tk

            # Send the current spots_status to the main thread
            avail = [lot_segment,spots_status]

            #Switching frames w/o stoping threads
            with update_lock:
                if lot_segment == 'A':
                    new_mask = maskA
                    new_video_path = video_pathA
                    if mask != new_mask or video_path != new_video_path:
                        mask = new_mask
                        video_path = new_video_path
                elif lot_segment == 'B':
                    new_mask = maskB
                    new_video_path = video_pathB
                    if mask != new_mask or video_path != new_video_path:
                        mask = new_mask
                        video_path = new_video_path
                elif lot_segment == 'C':
                    new_mask = maskC
                    new_video_path = video_pathC

                    if mask != new_mask or video_path != new_video_path:
                        mask = new_mask
                        video_path = new_video_path
                #update_values(mask, video_path, capA)  # Update video capture instance
        else:
            img = Image.open(r'C:\Users\DICT\Desktop\SPMS\Images\no_video.png')  # Replace with the path to your image
            image_resize = img.resize((frame_w, frame_h))

            image_tk = ImageTk.PhotoImage(image_resize)

            label.config(image=image_tk)
            label.image = image_tk

def open_directory(cam_entry):
    directory = filedialog.askopenfilename()
    cam_entry.delete(0, 'end')
    cam_entry.insert(0, directory)


#Caputure Display
def capture_label_content(widget, ss_spot, count=[0]):
    x, y, width, height = widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_width(), widget.winfo_height()
    image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    save_path = r'D:\screen capture'
    os.makedirs(save_path, exist_ok=True)

    filename = f"label_content_{count[0]:04d}.png"
    count[0] += 1

    image.save(os.path.join(save_path, filename))
    print(f"Content of {widget.cget('text')} captured and saved at {save_path}/{filename}!")
    CTkMessagebox(title="Info", message='Screen Capture {}'.format(ss_spot))

def capture_frame(name):
    frame_is_not_a = True
    while frame_is_not_a:
        if frame_seg[0] == 'A':
            save_path = r'D:\screen capture'
            frame_name = save_path + "{}.jpg".format(name)
            cv2.imwrite(frame_name, frame_seg[1])
            print('segment A frame successfully save')
            frame_is_not_a = False
            
def run_segment():
    # Replace with the absolute path to your virtual environment's activate script
    venv_activate_script = r"C:\Users\DICT\Desktop\SPMS\venv\Scripts\activate.bat"

    # Replace with the absolute path to your Python script
    script_to_run = r"C:\Users\DICT\Desktop\SPMS\image_segmentor_two.py"

    # Construct the command to activate the virtual environment and run the script
    command = f'call "{venv_activate_script}" && python "{script_to_run}"'

    # Run the command
    subprocess.call(command, shell=True)

#continuously access and display available spot
def access_spots_status(lot1,lot2,lot3,total,proceed_to_label):
    spot_A_len = 0
    spot_A_ava = 0

    spot_B_len = 0
    spot_B_ava = 0

    spot_C_len = 0
    spot_C_ava = 0



    spot_display_A = ""
    spot_display_B = ""
    spot_display_C = ""


    while True:
        user_class = data_q_class.get()
        print(user_class)
        user_has_class = data_q_has_class.get()
        print(user_has_class)
        f_spot = f_element
        print(f_spot)
        # print(user_class)
        # print(user_has_class)

        available_spot = avail
        #print(sum(available_spot[1]))
        print(available_spot[1])
        print(available_spot[0])

        parkingA = ''
        parkingB = ''
        parkingC = ''

        if available_spot[0] == 'A':
            spot_A_len = len(available_spot[1])
            print('len of A:',spot_A_len)
            spot_A_ava = sum(available_spot[1])
            #print(spot_A_len)
        elif available_spot[0] == 'B':
            spot_B_len = len(available_spot[1])
            spot_B_ava = sum(available_spot[1])
            #print(spot_B_len)

        elif available_spot[0] == 'C':
            spot_C_len = len(available_spot[1])
            spot_C_ava = sum(available_spot[1])
            #print(spot_C_len)


        total_avail = spot_A_ava + spot_B_ava + spot_C_ava
        total_spot = spot_A_len + spot_B_len + spot_C_len

        #if len(f_spot) != 0:
        if f_spot[0] == "A":
            if len(f_spot) != 1:
                spot_display_A = f_spot[1]
            else:
                spot_display_A = f_spot[0] + ' is FULL'
                parkingA = 'FULL'
        elif f_spot[0] == "B":
            if len(f_spot) != 1:
                spot_display_B = f_spot[1]
            else:
                spot_display_B = f_spot[0] + ' is FULL'
                parkingB = 'FULL'

        elif f_spot[0] == "C":
            if len(f_spot) != 1:
                spot_display_C = f_spot[1]
            else:
                spot_display_C = f_spot[0] + ' is FULL'
                parkingC = 'FULL'



        if user_class == 'teaching' and user_has_class == True:
            if parkingA != 'FULL':
                spot_to_proceed = spot_display_A
                proceed = 'PROCEED TO:'
            else:
                spot_to_proceed = spot_display_A
                proceed = ''
        elif user_class == 'non_teaching' and user_has_class == True:
            if parkingB != 'FULL':
                spot_to_proceed = spot_display_B
                proceed = 'PROCEED TO:'
            else:
                spot_to_proceed = spot_display_B
                proceed = ''
        elif user_class == 'staff' and user_has_class == True:
            if parkingC != 'FULL':
                spot_to_proceed = spot_display_C
                proceed = 'PROCEED TO:'
            else:
                spot_to_proceed = spot_display_C
                proceed = ''
        elif user_class == 'motorcycle':
            if parkingC != 'FULL':
                spot_to_proceed = spot_display_A
                proceed = 'PROCEED TO:'
            else:
                spot_to_proceed = spot_display_A
                proceed = ''
        else:
            spot_to_proceed = ''
            proceed = ''

        lot1.config(text='teaching Parking:\n{}/{}'.format(spot_A_ava, spot_A_len))
        lot2.config(text='non-teaching Parking:\n{}/{}'.format(spot_B_ava, spot_B_len))
        lot3.config(text='staff Parking:\n{}/{}'.format(spot_C_ava, spot_C_len))
        total.config(text='total: {}/{}'.format(total_avail, total_spot))


        proceed_to_label.config(text='{}{}'.format(proceed,spot_to_proceed))

#GUI
app = CTk()

#getting screen width and height of display
width = app.winfo_screenwidth()
height = app.winfo_screenheight()

#setting tkinter window size
app.geometry("%dx%d" % (width, height))
app.title("Video Stream")

screen_cap_icon = CTkImage(dark_image=Image.open(r"D:\white_icon_1.png"), size=(25,25))
setting_icon = CTkImage(dark_image=Image.open(r"D:\white_user.png"), size=(30,30))

#Widgets
#settings_button = CTkButton(app,text='', image=setting_icon, command=open_setting, width=25)
buttonA = CTkButton(app, image=screen_cap_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture_label_content(label0,"A"))
buttonB = CTkButton(app, image=screen_cap_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture_label_content(label1,"B"))
buttonC = CTkButton(app, image=screen_cap_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture_label_content(label2,"C"))
buttonD = CTkButton(app, image=screen_cap_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture_label_content(label3,"D"))
label0 = Label(app, text="video 1", anchor='center')
label1 = Label(app, text="Video 2", background="red", anchor='center')
label2 = Label(app, text="Video 3", background="blue")
label3 = Label(app, text="Video 4", background="yellow")
label4 = Label(app, text="teaching Parking\n 10/10 ", font=("CrashNumberingGothic", 30),fg='white', background="#556E53")
label5 = Label(app, font=("LED BOARD REVERSED", 35, "bold"),fg='yellow', background="black")
label6 = Label(app,text="non_teaching Parking\n 10/10", font=("CrashNumberingGothic", 30), fg='white', background='#4E2161')
label7 = Label(app,text="staff Parking\n 10/10", font=("CrashNumberingGothic", 30), fg='white', background='#774E26')
label8 = Label(app,text="total: 10/10", font=("CrashNumberingGothic", 30), fg='white', background='#427D9D')

#Bind
label0.bind("<Button-1>", video_a_label)
label1.bind("<Button-1>", video_b_label)
label2.bind("<Button-1>", video_c_label)





info_frame = CTkFrame(app, width=380)




#define grid
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=4)
app.columnconfigure(2, weight=4)
app.columnconfigure(3, weight=1)
app.columnconfigure(4, weight=2)
app.columnconfigure(5, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=4)
app.rowconfigure(2, weight=4)
app.rowconfigure(3, weight=1)

#place a widget
#settings_button.grid(row=0, column=5)
buttonA.grid(row=1, column=1, sticky='sw', ipady=1, ipadx=1)
buttonA.lift()
buttonB.grid(row=1, column=2, sticky='sw', padx=5, pady=5)
buttonB.lift()
buttonC.grid(row=2, column=1, sticky='sw', padx=5, pady=5)
buttonC.lift()
buttonD.grid(row=2, column=2, sticky='sw', padx=5, pady=5)
buttonD.lift()
label0.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
label1.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)
label2.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
label3.grid(row=2, column=2, sticky='nsew', padx=10, pady=10)
label4.grid(row=1, column=4, sticky='n', pady=80, ipadx=35)
label5.grid(row=2, column=4, sticky='ew')
label6.grid(row=1, column=4)
label7.grid(row=1, column=4, sticky='s', pady=80, ipadx=63)
label8.grid(row=1, column=4, sticky='s', pady=10)
info_frame.grid(row=1, column=4, sticky='ns')

#Configuration
label0.config(width=100, height=100)
label1.config(width=100, height=100)
label2.config(width=100, height=100)
label3.config(width=100, height=100)
label5.config(width=5, height=5, relief=RAISED, borderwidth=3)

label4.lift()
label6.lift()
label7.lift()
label8.lift()





#tip message
CTkToolTip(buttonA, message="Capture the current event in Parking lot A")
CTkToolTip(buttonB, message="Capture the current event in Parking lot B")
CTkToolTip(buttonC, message="Capture the current event in Parking lot C")
CTkToolTip(buttonD, message="Capture the current event in Parking Entrance")
ToolTip(label0, msg="Parking Lot A")
ToolTip(label1, msg="Parking Lot B")
ToolTip(label2, msg="Parking Lot C")
ToolTip(label3, msg="Parking Lot Entrance")
ToolTip(label4, msg="Parking lot Info")
ToolTip(label5, msg="LED matrix display of user")


#Menu bar cofigurations
menubar = Menu(app, background='blue', fg='white')
option_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Segment", command=run_segment)
app.config(menu=menubar)

#access spots_status value
access_thread = threading.Thread(target=access_spots_status, args=(label4, label6, label7, label8, label5))

#Run access thread
access_thread.start()

#Main threads
segment_A_thread = threading.Thread(target=segment_vid, args=(maskA, video_pathA, label0, frame_w, frame_h, data_queue, data_queue_spot , "A", capA))
segment_B_thread = threading.Thread(target=segment_vid, args=(maskB, video_pathB, label1, frame_w, frame_h, data_queue, data_queue_spot , "B", capB))
segment_C_thread = threading.Thread(target=segment_vid, args=(maskC, video_pathC, label2, frame_w, frame_h, data_queue, data_queue_spot , "C", capC))
segment_D_thread = threading.Thread(target=obj_classifier, args=(label3, user_classif_model, yolo_pretrained_model, video_pathD, frame_w, frame_h, data_q_class, data_q_has_class))

#start threads
segment_A_thread.start()
segment_B_thread.start()
segment_C_thread.start()
segment_D_thread.start()


app.mainloop()
cv2.destroyAllWindows()
