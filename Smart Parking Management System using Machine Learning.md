**SMART PARKING MANAGEMENT SYSTEM USING MACHINE LEARNING**

An Independent Study Presented to the Faculty of  
Institute of Computing Studies and Library Information Science  
City College of Angeles  
Angeles City

![][image1]

In Partial Fulfillment of the Requirement for the Degree  
Bachelor of Science in Computer Science

By:  
Cyjay M. Cunanan  
Jeffrey G. Wong  
Kurt Ryan C. Garcia

November 2023

# **APPROVAL SHEET** {#heading}

	This Independent Study entitled **“SMART PARKING MANAGEMENT SYSTEM USING MACHINE LEARNING”** prepared and submitted by:

Cyjay M. Cunanan  
Jeffrey G. Wong  
Kurt Ryan C. Garcia

In partial fulfillment of the requirements for the degree Bachelor of Science in Computer Science, has been examined and is recommended for acceptance and approval for Oral Examination.

| Mr. Aaron L. Batac, MIT |  | Ms. Jannette G. Zapata |
| :---: | :---: | :---: |
| Thesis Instructor |  | Adviser |

**THESIS COMMITTEE**  
	After having been presented is hereby accepted by the Committee on Oral Examination towards the fulfillment of the requirements for the Degree of Bachelor of Science in Computer Science.

| Mr. Jonathan C. Vital |  |  |
| :---: | :---: | :---: |
| Chairman |  |  |
|  |  |  |
| **Mr. Juniel J. Cabo** |  | **Mr. Aaron L. Batac, MIT** |
| Member |  | Member |

Noted by:

| Mr. Aaron L. Batac, MIT |  | Mr. Mark Gil Q. Superio, MIT |
| :---: | :---: | :---: |
| Academic Coordinator, BSCS |  | Dean, ICSLIS |

# 

# **ACKNOWLEDGEMENT** {#height-:-5’6”/175-cm}

The researchers would like to express their heartfelt appreciation and genuine thanks to the following persons for their support in the preparation and execution of this study work:  
First and foremost, we would like to thank our adviser, Ms. Jannette G. Zapata, for his continuous encouragement of our research, as well as his patience, inspiration, motivation, and extensive knowledge. As during research and writing of this thesis, his guidance was helpful. We couldn't have asked for better advice for our research.

We would like to extend our heartfelt gratitude to Dr. Aaron L. Batac, our research instructor, for his unwavering guidance, support, and boundless patience as we worked to complete this project.

To Mr. Jonathan Vital, Mr. Juniel J. Cabo and Mr. Mark Angelo Balboa, instructors and panelists, for making ideas to improve the researchers' research study.

To the researchers' families, friends, and classmates, who provide inspiration when they are discouraged and immensely assist them in completing the study.

Above all, the Almighty God for imparting the gift of wisdom, good health in this type of scenario, resourcefulness, patience, and resolve on them.

# **TABLE OF CONTENTS** {#table-of-contents}

[APPROVAL SHEET](\#heading)	ii

[ACKNOWLEDGEMENT](\#height-:-5’6”/175-cm)	iii

[TABLE OF CONTENTS](\#table-of-contents)	iv

[LIST OF TABLES](\#list-of-tables)	vii

[LIST OF FIGURES](\#list-of-figures)	viii

[ABSTRACT	1](\#abstract)

[INTRODUCTION	2](\#introduction)

[Background of the Study	2](\#background-of-the-study)

[Statement of the Problem	6](\#statement-of-the-problem)

[Objectives of the Study	6](\#objectives-of-the-study)

[Scope of the Study	7](\#scope-of-the-study)

[Delimitations of the Study	8](\#delimitations-of-the-study-the-study-may-concentrate-on-specific-technologies-used-in-smart-parking-systems-made-exclusively-for-parking-lots.-thus-still-has-limitation-that-are-being-bounded-by-time-and-can-be-added-in-the-future:)

[Conceptual Framework 	9](\#conceptual-framework-the-figure-below-displays-the-flow-of-the-smart-parking-management-system-using-machine-learning:)

[Significance of the Study	10](\#significance-of-the-study)

[Definition of Terms	11](\#definition-of-terms)

[METHODOLOGY	12](\#methodology)

[Algorithms	13](\#algorithms)

[Research Design	20](\#research-design)

[System Development Methodology	21](\#system-development-methodology)

[Participants	24](\#participants)

[Procedure	24](\#procedure)

[Data Analysis	27](\#data-analysis)

[Design and Implementation	29](\#design-and-implementation)

[Requirement Specification Analysis	29](\#requirement-specification-analysis)

[System Design and Specifications	30](\#system-design-and-specifications)

[Logical Specifications	33](\#logical-specifications)

[Hardware Specifications	34](\#hardware-specifications)

[Software Specifications	35](\#software-specifications)

[RESULTS	36](\#results)

[System / Application Outputs	36](\#system-/-application-outputs)

[Evaluation Results	43](\#evaluation-results)

[DISCUSSION	47](\#discussion)

[Summary of Findings	47](\#summary-of-findings)

[Conclusions	47](\#conclusions)

[Recommendations	48](\#recommendations)

[REFERENCES	49](\#references)

[Appendix A: Evaluation Instrument for I.T Experts	54](\#appendix-a:-evaluation-instrument-for-i.t-experts)

[Appendix B: Frequency Count of Distribution for I.T Experts	58](\#appendix-b:-frequency-count-of-distribution-for-i.t-experts)

[Appendix C: Frequency Count Distribution and Percentage of I.T Experts	62](\#appendix-c:-frequency-count-distribution-and-percentage-of-i.t-experts)

[Appendix D: Evaluation Instrument for Non-IT Experts	64](\#appendix-d:-evaluation-instrument-for-non-it-experts)

[Appendix E: Frequency Count of Distribution for Non- I.T Experts	66](\#appendix-e:-frequency-count-of-distribution-for-non--i.t-experts)

[Appendix F: Frequency Count Distribution and Percentage of Non- I.T Experts	68](\#appendix-f:-frequency-count-distribution-and-percentage-of-non--i.t-experts)

[Appendix G:  Use Case Diagram	70](\#appendix-g:-use-case-diagram)

[Appendix H:  Flow Chart	71](\#appendix-h:-flow-chart)

[Appendix I: Sequence Diagram	72](\#appendix-i:-sequence-diagram)

[Appendix J: I.T Experts Resume	73](\#appendix-j:-i.t-experts-resume)

[Appendix K: Researcher’s Resume	84](\#appendix-k:-researcher’s-resume)

[Appendix L: Source Code	90](\#appendix-l:-source-code)

# 

# **LIST OF TABLES** {#list-of-tables}

Table 1: *Likert Scale*	36  
Table 2: *Likert Scale Equivalent*	37  
Table 3: *Desktop specifications used in development and testing*	42  
Table 4: *Evaluation Results of I.T. Experts*	51  
Table 5:  *Evaluation Results of Non-I.T. Experts*	53  
[Table 6](https://docs.google.com/document/d/1SWUTyTZ1ZHcdAY-cbRiRs-mcMK8UcxS6xNlXLVFBJbc/edit\#heading=h.1opuj5n): *Accuracy of the system* *in terms of functional suitability*	70  
Table 7: *Accuracy of the system* *in terms of performance efficiency*	70  
Table 8: *Accuracy of the system* *in terms of compatibility*	79  
Table 9: *Accuracy of the system* *in terms of usability*	71  
Table 10: *Accuracy of the system* *in terms of reliability*	71  
Table 11: *Accuracy of the system* *in terms of security*	71  
Table 12: *Accuracy of the system* *in terms of maintainability*	71  
Table 13: *Accuracy of the system* *in terms of portability*	72  
Table 14*: Accuracy of the system* *in terms of functional suitability*	76  
Table 15*: Accuracy of the system* *in terms of performance efficiency*	76  
Table 16*: Accuracy of the system* *in terms of usability*	76  
Table 17*: Accuracy of the system* *in terms of reliability*	77

# 

# **LIST OF FIGURES** {#list-of-figures}

Figure 1*. Flow Chart Diagram*	17  
Figure 2: Parking Spot Detection *(PSD) Algorithm for Detecting Available*   
*Parking spot	22*  
Figure 3: *Object and User Classifier (OUC) Algorithm for User Detection*	25  
Figure 4\.*The Agile Methodology Diagram*	30  
 Figure 5: *Admin Panel*	38  
Figure 6: *Segment Dialog Box*	39  
Figure 7: *Segmenter Window*	39  
Figure 8: *Video Stream*	40  
Figure 9: *Admin Panel*	44  
Figure 10: *Save Configuration*	45  
Figure 11: *Save Button* 	46  
Figure 12: *Dialog Box*	47  
Figure 13: *Save Dialog Box*	47  
Figure 14: *Segment Dialog Box*	48  
Figure 15: *Segmenter Window*	49  
Figure 16: *Save Prompt*	49  
Figure 17: *No Video Feed* 	50  
Figure 18: *Video Stream*	50

# 

# **ABSTRACT** {#abstract}

	The increasing number of cars on the road, especially in congested locations or during travel, has led to a rapid evolution of daily life to being digital, including locating a parking spot. This is why technology is making our lives easier. Researchers thought that by providing users with access to a system, they might easily find accessible parking spaces, as humans struggle to regulate circumstances in parking lots. The assessment was carried out from forty-seven (47) respondents and three (3) IT professionals. Experts and the whole review process's findings revealed that the system satisfies all requirements and has the potential to benefit users. In order to effectively manage parking, the researchers develop a Smart Parking Management System using Machine Learning that combines real-time monitoring through the use of cameras and machine learning algorithms. This study will improve customer satisfaction by providing real-time monitoring about available parking spaces and reducing the time and effort required to find parking by accurately directing drivers to available spaces. Parking lots are minimized by efficient parking management, which ensures that vehicles enter and exit parking facilities smoothly, reducing congestion and boosting transportation effectiveness. This will reduce traffic and maximize parking space use.

*Keywords:* Smart Parking Management, Machine learning algorithms, Real-Time monitoring, Parking lots.

# **INTRODUCTION** {#introduction}

## **Background of the Study** {#background-of-the-study}

 	Technology is making our lives easier as daily life has quickly evolved to being digital. Since we have trouble controlling situations in parking lots, we are doing research that will aid in the case's resolution. The total number of cars in use worldwide exceeded 1 billion as reported by the International Energy Agency (IEA) in 2020, with 80 million new automobiles sold in 2019, according to Abbasi and Samsudin (2017). New advancements have also been made recently. Modern vehicles are always being improved to make them more commodious, secure, and practical for one's own use. We use a variety of vehicles in daily life, including bicycles, motor vehicles, and private cars. These are all generally available and are continually improving as we travel or visit specific locations. As a more sustainable and environmentally friendly alternative to conventional gasoline-powered cars, electric vehicles were also developed. 

It is crucial to remember that the switch from internal combustion engines to electric vehicles is a gradual process that will probably take many years or even decades to complete (Baimakhanova R., & Tokhtarova M., 2019). Parking lots around the world may currently be in distinct circumstances depending on the location and level of development. In certain places, parking spaces may be numerous and well-maintained, while in others, they may be limited or in poor condition. There are a few trends that could be observed in the global parking industry, including the use of sensors and other monitoring systems to track parking availability as well as the usage of mobile applications and other digital tools to assist drivers in finding and reserving parking spaces (Huang et al., 2019\). In addition, green infrastructure and sustainable materials are being used in parking lot construction to promote sustainability (INRIX., 2017\). The promotion of alternative modes of transportation such as electric vehicles, bicycles, and public transit is becoming more common in parking management (Japan International Cooperation Agency., 2014\). 

As highlighted by Kaur and Mittal (2019), the parking sector worldwide is experiencing rapid changes driven by emerging technologies and increasing concerns about sustainability. It is evident that parking lot management systems are already in place, with traditional parking systems such as surface lots and multi-level parking garages being common examples. Municipalities, private businesses, or building owners typically administer the parking lot systems that are most frequently utilized. In contrast, valet parking systems are typically seen in fine establishments like hotels and restaurants where patrons hand over their cars to a valet who parks the vehicle in a designated location. There are also shared parking systems, which permit numerous establishments to operate in the same garage or parking lot. It can be a practical approach to increase parking availability in locations with limited space. 

Automated parking systems use technology to park and retrieve cars, reducing the amount of space required for parking. These systems are becoming more popular in urban areas where land is at a premium.(Lee  et al., 2019\)

 	Here alone in the Philippines, the number of registered vehicles was reported with  4,951,662 units in December 2021 (Li et al., 2021). This figure has been updated annually and has averaged 2,527,599 units from December 1981 to 2021, with 41 recorded observations (Nguyen et al., 2019\). Due to the substantial need for parking space, local government units and land developers/owners have begun to consider the provision of off-site parking for their properties. In developed countries like Japan, Singapore, and Europe, car stackers and mechanical garages are commonly used (Onodera et al., 2020\). In the Philippines, parking lots are typically managed by individuals known as "parking boys," or through traditional ticket systems. While there are more advanced parking systems in the country, there is a growing trend towards implementing automated parking systems, especially in urban areas where land is limited. For instance, SM Megamall unveiled the first intelligent car parking system in August of 2019, and opened the first two towers as part of a cluster of 23 towers that were set to be completed by the first quarter of 2020 (Perera et al., 2021\). The absence of an organized parking system and reliance on traditional parking management has led to an increase in time spent searching for parking spaces. 

According to a 2018 survey by “Waze”, drivers in Metro Manila spend an average of 4.9 minutes searching for parking. However, this may vary depending on factors such as time of day, location, and parking space availability. While in areas with limited parking spaces, drivers may experience even longer search times. By implementing a smart parking management system that uses machine learning, real-time information on available parking spots can be provided to drivers, and parking space allocation can be optimized, which will help to reduce the time spent searching for parking and because of this there are a lot of resources that are being used that may contribute to the environment (Shaikh and Chandurkar, 2019\). The protracted idle time vehicles spend looking for parking spots. The design of parking spots, which has not changed much over the years, is the topic under examination (Shaheen et al., 2012\).  The history of parking space design, according to Schaller, contends that many conventional parking spot layouts are ineffective and wasteful of space (Park et al., 2015\). 

According to Aijazi and Javaid (2018), The opportunities and difficulties that urban parking must face, including the requirement for better place to park designs. It suggests that new technologies and designs, such as shared parking and automated parking systems, could improve parking efficiency and reduce the need for large parking structures. The poor urbanization planning here in the Philippines also adds in the previous discussions where establishments that are built have no allotted parking spaces. 

 	The City of Angeles is becoming a highly urbanized city which leads to higher numbers of vehicles with few parking spaces which results in parking problems, the traditional parking systems usually managed by human intervention. Because the traditional system can't cope with urbanization the parking management systems are usually behind, leading to much more problems, delays, environmental issues, unforeseen expenses and congestion. The demand for an SPMS (Smart Parking Management System) that is automated and effective. A system like this can aid in maximizing the use of available parking spots, lessen human mistake and intervention, and give drivers a more convenient and effective parking experience. Overall, the statement emphasizes the need for a more technologically advanced, wiser approach to parking management in the City of Angeles which may solve the system's present parking issues and increase system efficiency.

## **Statement of the Problem** {#statement-of-the-problem}

        The primary objective of this research is to develop a smart parking management system using machine learning that will accurately display parking occupancy and availability, thus improving the efficiency and utilization of parking spaces in urban areas.

The following specific problems will be addressed in this research: 

1. The inefficiency of the traditional parking system because it lacks real-time monitoring features.   
1.  The amount of time needed to locate a parking space by a traditional parking system.  
1.   The involvement of parking lots in congested traffic caused by vehicle owners simultaneously looking for available parking space.  
   

## **Objectives of the Study** {#objectives-of-the-study}

	The main objective of this research is to design and develop a smart parking management system using machine learning techniques. This will be accomplished by utilizing advanced algorithms and real-time information analysis. Specifically, the study aims to:

1. To have efficient parking management that enhances the customer experience providing real-time information about available parking spaces.   
1. To lessen the consumption of time and effort required to find parking by accurately directing drivers to available spaces, allowing for effective parking management.   
1. To reduce congestion and optimize parking space utilization, parking lots are decreased through effective parking management, which guarantees that vehicles enter and depart parking facilities smoothly easing congestion and improving transportation effectiveness.  
   

## **Scope of the Study** {#scope-of-the-study}

The study aims to develop and evaluate the effectiveness of a smart parking system using a combination of cameras and machine learning algorithms. The primary aim is to focus on the development of an algorithm that can accurately detect the occupancy status of parking spots in real-time which will improve the efficacy and accessibility of parking facilities on the school campus specifically tailored for vehicle owners that are students and school personnels. In order to enhance traffic management and maximize parking space utilization the system will be implemented using cameras to provide comprehensive coverage of the parking lot. The study intends to evaluate the potential advantages of the machine learning model, challenges integrated into the system by the experience of users, and implications of implementing smart parking technology setting to evaluate its effectiveness in improving parking lot efficiency and reducing traffic congestion for various stakeholders.

## 

## **Delimitations of the Study** 	The study may concentrate on specific technologies used in smart parking systems  made exclusively for parking lots. Thus still has limitation that are being bounded by time and can be added in the future:  {#delimitations-of-the-study-the-study-may-concentrate-on-specific-technologies-used-in-smart-parking-systems-made-exclusively-for-parking-lots.-thus-still-has-limitation-that-are-being-bounded-by-time-and-can-be-added-in-the-future:}

	First, it will not delve into the legal and regulatory issues that may arise from the implementation of a Smart Parking Management System, including concerns related to data privacy and liability for accidents. Data availability and quality pose significant challenges. A smart parking system's complete implementation can be an expensive undertaking, involving costs for the required infrastructure, cameras, and machine learning technology. This is where cost limitations come into play. Regular maintenance is necessary to guarantee dependable performance and is crucial for the consistent operation of cameras and other equipment. And security threats are a big deal since any system that collects and stores data—especially in real time—is vulnerable to cyberattacks, which means that strong security measures are essential. Additionally, the user adoption, since it might be difficult to get drivers to accept the new parking system, particularly if it requires significant adjustments to user behavior. An additional factor to take into account is the payment mechanism. The smart parking system does not employ any form of payment method.

## **Conceptual Framework**  	The figure below displays the flow of the Smart Parking Management System using Machine learning: {#conceptual-framework-the-figure-below-displays-the-flow-of-the-smart-parking-management-system-using-machine-learning:}

	

              				       			 

Figure 1*. Flow Chart Diagram*

The figure displays the concept of the research entitled "smart parking system using machine learning". The flow chart is the representation of the process that will be followed by the system.  
The proposed system operates in real-time, which enables the instantaneous detection, analysis of vehicles and parking spots . This functionality is facilitated through the integration of advanced machine learning practices, which enhances the system's ability to detect vehicles and display real-time information on available parking spots. The system further continuously monitors the availability of parking spaces, providing real-time data updates to drivers.

To improve user experience, drivers receive prompt information on the number of available parking spots and recommendations on the most suitable parking location through the monitor. The system's flow is continuous, and data is constantly updated in real-time, ensuring optimal functionality and reliability.

## **Significance of the Study** {#significance-of-the-study}

This study determined the advances of smart parking management systems (SPMS). This study provides an in-depth understanding of the edge of machined learning technology. The findings of this study are beneficial to the following: 

1. **To the School Personnels.** The results of this study may give school personnels insights on capabilities of Smart Parking Management. This will guide them in discovering new strategies to help students in learning, practicing, and improving their skills and talents.  
1. **To the Students**. This study will give them knowledge on advances of Smart Parking Management Systems wherein they will be able to make the campus environment safer for them, especially late at night or in remote places. These features include well-lit parking lots and surveillance cameras. Also will give them a better understanding of the modern parking systems in succeeding on their journey as a student and a worker for future years.   
1. **To the Vehicle Owners (Drivers)**. This study will benefit the drivers in reducing the amount of time and frustration associated with searching for available parking spaces. Vehicle owners will also receive positive perception from the improved efficiency and enhance the parking reservation system, which can help to reduce inconvenience rather than save time and improve overall parking experience.   
1. **To the Parking Facility Operators**. The results will help to optimize parking operations by giving parking facility operators access to real-time data on parking space utilization. For the operators, this may mean higher profits, lower expenses, and increased efficiency.  
1. **To the Researchers**. The researchers themselves can benefit from the study by gaining experience in designing and implementing a Smart Parking Management System using machine learning techniques. The study can also provide opportunities for publication and dissemination of research findings.  
1. **To the Future Researchers.** Future researchers will benefit from the study's theoretical foundation and conceptual framework as they create their own or enhance this study to address parking-related issues**.**

## **Definition of Terms** {#definition-of-terms}

To facilitate the understanding of the study different terms defined herein:

1. **Smart parking management system:** A system that utilizes technology such as sensors, cameras, and machine learning algorithms to optimize parking lot utilization, improve user experience, and reduce traffic congestion.   
1. **Machine Learning Algorithms:** A field within artificial intelligence that works with algorithms to teach them how to recognize patterns and forecast outcomes from data.   
1. **Machine Learning:** A broader term that includes the application of algorithms to allow computers to learn from data and carry out operations without explicit programming.  
1. **Automated Parking Systems:** A type of parking system that uses technology, such as sensors, lifts, and conveyors, to automatically park and retrieve vehicles without the need for human intervention.   
1. **Digital Tools:** software applications, programs, and online platforms that are used for creating, editing, publishing, or sharing digital content such as text, images, audio, and video. These tools have become an integral part of modern communication, education, entertainment, and business practices.

# **METHODOLOGY** {#methodology}

In this chapter, the method employed by the researcher in developing the system is discussed. Additionally, the study's research design, participants, sampling method, instruments, development and validation of the instruments, data collection processes, and analytical tools are described.

## **Algorithms** {#algorithms}

 	Smart Parking Management System employing Machine Learning, encompassing a variety of technical models, algorithms, and analytics. The study rigorously examines the techniques, plans, and strategies employed in the planning, design, and development phases, presenting a systematic analysis and comprehensive discussion of these aspects.

Figure 2: Parking Spot Detection *(PSD) Algorithm for Detecting Available Parking spot*

* **Parking Spot Detection (PSD) Algorithm for Detecting Available Parking Spot**

The algorithm employed in the parking lot is Parking Spot Detection (PSD) as it simultaneously detects each parking spot. First, the program will use the masked image of the parking lot to draw bounding boxes around each of the connected components using the segmented image of the parking lot. After determining and creating the bounding boxes in the video feed, the model will identify whether each spot is empty or not. Subsequently, the empty bounding box is changed to the color green, and for the not-empty ones, it will be changed to red. Finally, Then the program will store the parking lot identification with the empty parking spaces indices.

EMPTY \= True  
NOT\_EMPTY \= False

MODEL \= pickle.load(open("C:/Users\\DICT\\Desktop\\SPMS\\model\\model.p", "rb"))

F  
        return EMPTY  
    else:  
        return NOT\_EMPTY

def get\_parking\_spots\_bboxes(connected\_components):  
    (totalLabels, label\_ids, values, centroid) \= connected\_components

    slots \= \[\]  
    coef \= 1  
    for i in range(1, totalLabels):

        \# Now extract the coordinate points  
        x1 \= int(values\[i, cv2.CC\_STAT\_LEFT\] \* coef)  
        y1 \= int(values\[i, cv2.CC\_STAT\_TOP\] \* coef)  
        w \= int(values\[i, cv2.CC\_STAT\_WIDTH\] \* coef)  
        h \= int(values\[i, cv2.CC\_STAT\_HEIGHT\] \* coef)

        slots.append(\[x1, y1, w, h\])

    return slots

mask \= cv2.imread(mask, 0\)  
    cap \= cv2.VideoCapture(video\_path)

    if cap.isOpened() \== True:  
        connected\_components \= cv2.connectedComponentsWithStats(mask, 4, cv2.CV\_32S)  
        spots \= get\_parking\_spots\_bboxes(connected\_components)

        \# Initialize the list to store spot status  
        spots\_status \= \[None for j in spots\]

        frame\_nmr \= 0  
        ret \= True  
        step \= 30

        while ret:  
            ret, frame \= cap.read()

            if frame\_nmr % step \== 0:  
                for spot\_indx, spot in enumerate(spots):  
                    x1, y1, w, h \= spot  
                    spot\_crop \= frame\[y1:y1 \+ h, x1:x1 \+ w, :\]  
                    spot\_status \= empty\_or\_not(spot\_crop)  
                    spots\_status\[spot\_indx\] \= spot\_status

                    \# Display spot index on the frame  
                    cv2.putText(frame, str(spot\_indx \+ 1), (x1 \+ w // 2, y1 \+ h // 2), cv2.FONT\_HERSHEY\_SIMPLEX, 0.5,  
                                (255, 255, 255), 2\)

            \# Rest of the code for visualization and updating the frame  
            for spot\_indx, spot in enumerate(spots):  
                spot\_status \= spots\_status\[spot\_indx\]  
                x1, y1, w, h \= spots\[spot\_indx\]

                \# Draw rectangles based on spot status  
                if spot\_status:  
                    frame \= cv2.rectangle(frame, (x1, y1), (x1 \+ w, y1 \+ h), (0, 255, 0), 2\)  
                else:  
                    frame \= cv2.rectangle(frame, (x1, y1), (x1 \+ w, y1 \+ h), (0, 0, 255), 2\)

            \# Generate and print empty spot indices after processing the frame  
            empty\_spots\_indices \= \[f"{lot\_segment}{index \+ 1}" for index, status in enumerate(spots\_status) if status\]  
            if empty\_spots\_indices:  
                f\_element \= (empty\_spots\_indices\[0\])  
            else:  
                f\_element \= None  
Figure 3: *Object and User Classifier (OUC) Algorithm for User Detection*

* **Object and User Classifier  (OUC) Algorithm for User Detection**

	The algorithm utilized for the Detection and Classification of Users is the Object and User Classifier (OUC) Algorithm for User Detection. Two models are employed in this algorithm: the first is the YOLOv8 pretrained model, and the second is our user classification model. Initially, we define a region of interest (ROI) where the first model identifies the type of vehicle within the ROI; our current setup focuses on detecting only 'cars.' Following this, sets of flags are established to continuously monitor whether the user falls into one of the following categories: teaching, non-teaching, or staff. We base the classification on the school premises. If the model detects that the vehicle has a classification, the flags are triggered, and the data are sent to the main program for further processing.  
yolo\_objects \= YOLO(obj\_mdl\_path)

    \# YOLO model for car and motorcycle detection  
    yolo\_vehicles \= YOLO(veh\_mdl\_path, "v8")

    \# Open the video file  
    cap \= cv2.VideoCapture(vid\_path)

    \# Define the ROI for vehicle detection  
    roi\_points \= np.array(\[\[(0, 175), (1270, 175), (1270, 816), (0, 816)\]\], dtype=np.int32)

    user\_vehicle\_classification \= None  \# Initialize the variable

    if cap.isOpened():  
        while cap.isOpened():  
            \# Read the video frame by frame  
            ret, frame \= cap.read()  
            if ret:  
                \# Draw the ROI for vehicle detection on the frame  
                cv2.polylines(frame, \[roi\_points\], isClosed=True, color=(0, 0, 255), thickness=2)

                \# Apply the YOLO model for car and motorcycle detection to the frame  
                results\_vehicles \= yolo\_vehicles.predict(source=frame)

                \# Flags to keep track of vehicle and object classification  
                car\_detected \= False  
                staff\_detected \= False  
                teaching\_detected \= False  
                non\_teaching\_detected \= False  
                car\_has\_class \= False

                \# Check if a car is Inside ROI  
                for result\_vehicle in results\_vehicles:  
                    for i in range(len(result\_vehicle.boxes.xyxy)):  
                        x, y \= int(result\_vehicle.boxes.xyxy\[i\]\[0\]), int(result\_vehicle.boxes.xyxy\[i\]\[1\])  
                        if cv2.pointPolygonTest(roi\_points, (x, y), False) \>= 0:  
                            \# Car is inside the ROI, proceed with drawing and classification  
                            class\_name\_vehicle \= yolo\_vehicles.names\[int(result\_vehicle.boxes.cls\[i\])\]

                            \# Filter only desired classes (e.g., "car" and "motorcycle")  
                            if class\_name\_vehicle in \["car"\]:  
                                car\_detected \= True

                                \# Draw bounding box for the car  
                                x1, y1, x2, y2 \= map(int, result\_vehicle.boxes.xyxy\[i\])  
                                label \= f'{class\_name\_vehicle}: {result\_vehicle.boxes.conf\[i\]:.2f}'  
                                frame \= cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2\)  
                                frame \= cv2.putText(frame, label, (x1, y1 \- 10), cv2.FONT\_HERSHEY\_SIMPLEX, 0.9, (255, 0, 0), 2\)

                                \# Extract sub-region within car bounding box  
                                sub\_roi \= frame\[y1:y2, x1:x2\]

                                \# Apply the YOLO model for staff, teaching, non\_teaching to the sub-region  
                                results\_objects \= yolo\_objects.predict(source=sub\_roi)

                                \# Check if objects are inside sub-ROI  
                                for result\_obj in results\_objects:  
                                    for j in range(len(result\_obj.boxes.xyxy)):  
                                        x\_obj, y\_obj \= int(result\_obj.boxes.xyxy\[j\]\[0\]), int(result\_obj.boxes.xyxy\[j\]\[1\])

                                        \# Convert object coordinates to global frame  
                                        x\_obj\_global, y\_obj\_global \= x\_obj \+ x1, y\_obj \+ y1

                                        if cv2.pointPolygonTest(roi\_points, (x\_obj\_global, y\_obj\_global), False) \>= 0:  
                                            \# Object is inside the ROI, proceed with drawing and classification  
                                            \# Draw bounding box  
                                            x1\_obj, y1\_obj, x2\_obj, y2\_obj \= map(int, result\_obj.boxes.xyxy\[j\])  
                                            label\_obj \= f'{yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\]}: {result\_obj.boxes.conf\[j\]:.2f}'  
                                            frame \= cv2.rectangle(frame, (x1\_obj \+ x1, y1\_obj \+ y1), (x2\_obj \+ x1, y2\_obj \+ y1),  
                                                                  (255, 0, 0), 2\)  
                                            frame \= cv2.putText(frame, label\_obj, (x1\_obj \+ x1, y1\_obj \+ y1 \- 10),  
                                                                cv2.FONT\_HERSHEY\_SIMPLEX, 0.9, (255, 0, 0), 2\)

                                            \# Check for object classifications  
                                            if yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'staff':  
                                                staff\_detected \= True  
                                                car\_has\_class \= True  
                                            elif yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'teaching':  
                                                teaching\_detected \= True  
                                                car\_has\_class \= True  
                                            elif yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'non\_teaching':  
                                                non\_teaching\_detected \= True  
                                                car\_has\_class \= True

                \#print(str(car\_has\_class))  
                \# Determine the user\_vehicle\_classification  
                if car\_detected:  
                    if staff\_detected:  
                        user\_vehicle\_classification \= 'staff'  
                    elif teaching\_detected:  
                        user\_vehicle\_classification \= 'teaching'  
                    elif non\_teaching\_detected:  
                        user\_vehicle\_classification \= 'non\_teaching'  
                    else:  
                        user\_vehicle\_classification \= None

## 

## **Research Design** {#research-design}

	In this study, Descriptive Research will be employed as the most suitable research method. Descriptive research is distinguished by its primary goal of data collection to address particular issues, allowing researchers to fully comprehend the situation at hand. In order to establish hypotheses and provide solutions, it entails outlining several situations and analyzing the behavior of a sample within a population. This approach works well for addressing queries, reaching sound conclusions, and making recommendations (Atmowardoyo, H., 2018).  
Given the nature of the study, Descriptive Research is the most appropriate approach as it allows researchers to gather essential facts relevant to the proposed study. These facts serve as the basis for making scientific judgments. The researchers aim to address existing parking issues in various areas resulting from inadequate management of parking spaces.

## **System Development Methodology** {#system-development-methodology}

The term System Development Methodology (SDM) is a systematic development process used to carry out crucial processes for software systems analysis, design, implementation, and maintenance. Adopting a systems development methodology is quite beneficial for research aimed at creating a system. It is advised to use system development approaches to improve management and control over the software development process, to streamline its structure, to make procedures clearer, and to standardize both the development process and the final product. Researchers can evaluate, design, implement, and maintain the system efficiently by using a systems development methodology, which results in a well-organized and standardized software development process and end product.  
	The Agile Methodology will be used in this study as a system development approach. Project management approaches that are incremental and iterative, like agile, facilitate rapid output and continuous development (Nolle, T., 2021).  
The agile methodology's essential elements of working in iterations and emphasizing communication allow projects to be improved continuously during their   
lifetime. Quick and responsive change makes adaptable and flexible change feasible (Statistics Canada, 2021).

Figure 4.The Agile Methodology Diagram  
**Phases of Agile Methodology**  
*Plan*   
	The project's planning phase is considered to be its most important step. Beginning with a brainstorm of potential issues that need fixing, this phase ushers in the project. The researchers then worked together to develop a workable solution. The project's requirements and scope were covered in a meeting, and specific tasks were determined. Each task was thereafter assigned and disseminated among the team members, acting as a road map or instruction manual for finishing various project components. To speed up the project's development, the gathered data will be aggregated and refined.  
*Design*  
Following the discovery and assessment of the requirements, the developer started work on creating the system's graphical user interface (GUI) during the second phase. Choosing the appropriate programming language and tools was necessary for this. Additionally, any problems that can come up during the system design phase were addressed. Informing and directing the design process, the data gathered in the first phase was of utmost importance.  
*Develop*  
	All of the requirements that were established during the design phase are implemented during this stage. To begin creating the system, the developer uses the chosen tools and programming language. To make sure the system matches with consumer pleasure and meets their needs, the researchers actively direct the development process and gather user feedback.  
*Test*   
During the testing phase, any code problems that might have gone unnoticed during development are found. The iterative process is repeated until every important problem is fixed and the system's performance stabilizes. At every level of the creation cycle, the researcher combines integration and testing to ensure thorough evaluation. The system will continue to be improved and expanded based in large part on user feedback.  
*Deploy*   
	The project moves on to the launch phase, where it is made accessible to users, following the successful conclusion of the testing phase, at which point the system is declared stable and problem-free. In order to maintain compatibility, keep systems current, and guarantee a trouble-free deployment, this phase also entails updating system components.

## **Participants** {#participants}

	Participants in the study will include students and school personnel who drive their own vehicles to and from the school each day. These participants were selected for the study because of their individual experiences and using vehicles for commuting within the school setting. the participant must be currently working or studying in City College of Angeles. The study has 47 Non – I.T. and Three I.T. Experts with a total of 50 respondents.  
	To choose participants for this study, a purposive sampling strategy will be used. Using a non-probability selection technique called "purposeful sampling," people are specifically chosen who have certain traits or experiences that are pertinent to the study's goals. In this situation, volunteers who have driving experience and are eager to take part in the study will be specifically picked.  
Purposive sampling is frequently used to gather in-depth opinions from people with specific knowledge or experiences. By focusing on participants who can offer useful and pertinent information, researchers can increase the depth and caliber of their research findings (Palinkas, et al.,(2015). Overall, we have conducted 47 participants.

## **Procedure** {#procedure}

The researcher used the following resources to get the information needed for the suggested system:

1. **Survey \-** A survey is a way of gathering data that entails asking questions to a predetermined sample of a community to elicit information (Weerdt, J. D., 2020*)*. In order to get input and understanding about the system's operation and fit with its intended purpose, the researchers in this study sent surveys to possible system users.  
1. **Web Research \-** Web research is now a common method for learning new things in the modern world (Bhat., 2019*)*. In order to obtain pertinent data and gain access to study-related papers, the researcher will use the internet to its fullest extent in this study. By examining current initiatives and studies that offer insightful information about the system, the study can broaden its knowledge base by using web research.  
1. **Evaluation Questionnaire-** In accordance with ISO-25010 standards, the produced web application's quality is evaluated using a number of product quality parameters. These desirable qualities include functionality appropriateness, performance effectiveness, compatibility, usability, dependability, security, maintenance ease, and portability. The study seeks to ensure that the created system satisfies the specified requirements for each quality element by assessing the web application against these standards.  
   1. **Functional Suitability \-** one of the factors that determines how well the system satisfies the specified requirements, such as efficient parking management, a reduction in the amount of time spent in parking lots, a reduction in traffic and an optimization of parking space use, and efficient resource use.  
   1. **Performance Efficiency \-**This characteristic evaluates whether the system operates at its best given the resources at hand. It looks at how effectively the software uses system resources to carry out its intended functions.  
   1. **Compatibility \-** The capacity of the program to use shared resources efficiently. It guarantees that the system can coexist and function without a hitch in a diverse technical environment.  
   1. **Usability \-** By efficiently and successfully attaining desired goals, usability assesses how well a program satisfies user demands. It also takes into account the system’s capacity to support users of various skill levels.  
   1. **Reliability \-**  The level of a system's capacity to continuously operate as planned and be used when necessary is known as its reliability. It evaluates the system's capacity to function even in the event that hardware or software problems occur.  
   1. **Security \-** The level of a system's capacity to continuously operate as planned and be used when necessary is known as its reliability. It evaluates the system's capacity to function even in the event that hardware or software problems occur.  
   1. **Maintainability \-** The system's maintainability serves as a gauge for how quickly faults can be fixed. In order to facilitate effective updates and alterations to support continuous functionality and improvements, it also evaluates the system's capacity to adapt to changing environments. 

## **Data Analysis** {#data-analysis}

	Data analysis, which includes the gathering, analyzing, and interpreting of conclusions drawn from raw data, is an important part of this study (*Amadebai, E., 2019\)*. Organizing, evaluating, and coming to intelligent conclusions are steps in the process that guarantee the quality and correctness of the information presented. The study's goal is to effectively meet the research objectives by identifying insights, identifying trends, and drawing reliable conclusions from the examination of the study's data.  
Several statistical methods were used to analyze the data that had been gathered during the data analysis procedure. For arranging numerical data, the following techniques were used:

**1\.**  **Arithmetic Mean** \- The technique entails averaging the numerical data gathered (*Glen, S., 2020\)*. It enables the calculation of the average value for each category of data, which can then be interpreted and condensed using descriptive ratings based on their relative rates.

**2\.**   **Percentage Distribution** – In a data representation known as a frequency distribution, the frequencies of different categories are expressed as percentages of the total frequency, which is equal to 100 (Statistics Canada., 2021). The number of observations linked to each data point or set of data points can be understood by this data visualization.  
  

       **Formula:**  
         **P= (F/N) ×100**  
         **Where:**  
                     **P \= Percentage**  
                     **F \= Frequency**  
                     **N \= No. of respondent**

**3\.**  **Likert Scale –** To gauge and measure respondents' agreement or dissatisfaction with the system, researchers will use a five-point scale. Participants can indicate their level of agreement or disagreement on a defined continuum using this scale, which acts as a measurement tool to assess how well the system is working.

*Table 1\. Likert Scale*

| Numerical Rating |                      Description |
| ----- | :---- |
|                                  5 |                        Excellent |
|                                  4 |                       Very Good |
|                                  3 |                           Good |
|                                  2 |                            Fair |
|                                  1 |                            Poor |

**2\.**   **Scale used to interpret evaluation results –** When testing a system, numerical values work best for determining its strengths and weaknesses. Numerical scales will be used to analyze the testing and assessment results in order to ascertain the corresponding magnitudes or values. This method helps in pinpointing the system's precise strengths and shortcomings by enabling a quantitative evaluation of its performance.                               

   *Table 2\. Evaluation Result Interpretation*

| Numerical Rating |                      Description |
| ----- | :---- |
|                        4.20 – 5.00 |                        Excellent |
|                        3.40 – 4 \-19 |                       Very Good |
|                        2.60 – 3.39 |                           Good |
|                        1.80 – 2.59 |                            Fair |
|                        1.00 – 1.79 |                            Poor |

## **Design and Implementation** {#design-and-implementation}

In the design and implementation of the Smart Parking Management System, a comprehensive requirement specification analysis has been undertaken of the following:

### **Requirement Specification Analysis** {#requirement-specification-analysis}

1. **Set up parking Configuration**

   After Installation:

   	Smart Parking Management System Admin will set up the parking settings.

   \-Parking for (Car and Motorcycle)  
   \- Upload parking lot segmented images

1. **Parking space Availability** 

   \- The system should continuously monitor parking spaces and provide real-time information on their availability.

   \- Users should be able to view the availability status of parking spaces before arriving at the parking lot.

### **System Design and Specifications** {#system-design-and-specifications}

From the perspective of the developer, this section describes the system requirements. These include the following:

* ***User Interface Design.*** 

  It is the graphical representation of the product to feel the appearance and interactivity.


          Figure 5: *Admin Panel*

	In the figure above, it shows the Admin Panel where you can set video source, mask, parking lot, Save, Save Configuration and Import Configuration button.

![][image2]

Figure 6: *Segment Dialog Box*  
	In the figure above, the Segment Dialog Box is a prompt where you can manage and organize specific segments, offering a convenient way to handle and make adjustments to individual parts of the parking lot.

Figure 7: *Segmentor Window*  
	In the figure above, the Segmentor Window serves as the main interface where you can visually identify distinct segments within a parking lot, providing a dedicated space for tasks and controls related to segment management.

Figure 8: *Video Stream*  
In the figure above, the Video Stream displays the available and total parking spots, providing a visual representation of the parking area's occupancy status in real-time.

      

### **Logical Specifications**  {#logical-specifications}

This section presents the different diagrams used in the study These diagrams should be discussed and explained comprehensively with proper citations and labels. The diagrams should be placed in the Appendices. These diagrams are, but not limited to:  
***Use Case Diagram***   
The use case diagram presented  provides a concise visual representation of the system's functionality, emphasizing the seamless integration of machine learning for real-time updates. As users approach the parking lot, they can conveniently access information about available parking spaces through a dedicated monitor. This not only facilitates a smoother entry process but also minimizes the time spent searching for suitable parking spots.  
The diagram showcases key user interactions, illustrating how the system dynamically updates and communicates with both the users and the parking infrastructure. Through intuitive interfaces, users gain insights into the current parking availability, allowing them to make informed decisions before entering the premises. The system's real-time capabilities ensure that the information displayed is accurate, reflecting the dynamic nature of parking space availability.([See Appendix G](\#appendix-g:-use-case-diagram))

***Flowchart***  
	In this section, it shows the overall flowchart of the study that introduces a dynamic and effective parking management system. The first step in the process is the camera system, which is quick to determine if a car approaching is owned by teaching, non-teaching, or staff. Once recognized, the system examines and analyzes the data employing real-time processing capabilities to assess the current parking availability. The outcome of this analysis is then displayed on a monitor, providing instant insights into the number of available parking spots. This real-time feedback not only streamlines the parking process but also optimizes the overall parking management system.([See Appendix H](\#appendix-h:-flow-chart))

***Sequence Diagram***   
	A Sequence Diagram is a visual representation that illustrates the dynamic interactions between various components or actors within a system. In this context, the diagram succinctly depicts the sequence of actions and communications between the User, User Interface, Machine Learning Module, and Parking Lot Sensors, providing a clear view of the system's operational workflow. ([See Appendix I](\#appendix-i:-sequence-diagram))

### **Hardware Specifications** {#hardware-specifications}

This section will include the minimal and recommended specifications for operating the application during implementation, as well as the machine requirements the researchers utilized to design the program. For development, computers with high specs are required. Table 3 presents the minimum and recommended specifications for the application's design and testing.  
Table 3: *Desktop specifications used in development and testing*

| Hardware | Minimum Specifications | Recommended Specifications  |
| :---- | :---- | :---- |
| Processor  | Intel Core i5 or equivalent  | Intel Core i7 or equivalent  |
| Memory(RAM)  | 8GB  | 16GB |
| Storage  | 256GB SSD  | 512GB SSD |
| Display  | 15.6-inch, Full HD  | 15.6-inch, 4K Ultra HD |
| Operating System |  Windows 10 or macOS  | Windows 10 or macOS  |

### **Software Specifications** {#software-specifications}

This software specification document outlines the requirements and functionality of the following software tools PyCharm an Integrated Development Environment (IDE) for Python programming utilized for developing the machine learning models and the backend of the Smart Parking Management System. Proto.io a web-based prototyping platform for crafting user-friendly, interactive prototypes for the system's user interfaces and frontend and YOLOv7 a state-of-the-art object detection model, integrated into the machine learning development process for enhancing object detection capabilities in the Smart Parking Management System.      

# **RESULTS** {#results}

The entire set of results is covered in this chapter. It contains screenshots of the system and application outputs as well as the various pieces of hardware that the researchers have used to conduct the investigation. Additionally, the IT assessment outcomes both non-IT specialists and experts. 

## **System / Application Outputs** {#system-/-application-outputs}

	In this section, the researchers will display the program's screenshot outputs. The pop-up windows that the application generates are depicted in the images below, which you can view when using the program. 

Figure 9: *Admin Panel*  
	In the figure above, it shows the Admin Panel where you can set video source, mask, parking lot, Save, Save Configuration and Import Configuration button.

	  
Figure 10: *Save Configuration*  
	In the figure above, the Save Configuration button enables users to store current settings or preferences within a system, ensuring that customized configurations can be easily preserved and retrieved from your file.

Figure 11: *Save Button*   
	In the figure above, the Save Button allows you to store your work or changes, preventing any loss and keeping the latest version for future access. 

## 

Figure 12: *Dialog Box*  
	In the figure above, the Dialog Box is a prompt that allows you to upload video segments and images for a parking lot, providing a convenient way to interact with the program.

Figure 13: *Save Dialog Box*  
	In the figure above, the Save Dialog Box is a prompt  specifically designed to store all the segments you've drawn, providing a simple way to save your progress and ensure that your edits are preserved.

![][image2]  
Figure 14: *Segment Dialog Box*  
	In the figure above, the Segment Dialog Box is a prompt where you can manage and organize specific segments, offering a convenient way to handle and make adjustments to individual parts of the parking lot.

## 

Figure 15: *Segmentor Window*  
	In the figure above, the Segmentor Window serves as the main interface where you can visually identify distinct segments within a parking lot, providing a dedicated space for tasks and controls related to segment management.

Figure 16: *Save Prompt*  
In the figure above, the Save Prompt is specifically designed to store all the segments you've drawn from the Segmentor window.

Figure 17: *No Video Feed*   
	In the figure above, the No Video Feed indicates that there is currently no live or available video stream, informing users that the system is not receiving or displaying any video data at the moment.

## 

Figure 18: *Video Stream*  
In the figure above, the Video Stream displays the available and total parking spots, providing a visual representation of the parking area's occupancy status in real-time.

## **Evaluation Results** {#evaluation-results}

	The evaluation outcomes, which include the three IT assessments, are discussed in Tables 4 and 5 of this report. professionals who employ ISO-25010 as a survey instrument for data collection. 47 Non-I.T. and Three IT Professionals, with fifty replies in all. It demonstrates that the majority of participants are experienced drivers of vehicles.

Table 4: *Evaluation Results of I.T. Experts*

| Criteria | Mean | Descriptive Rating |
| ----- | :---: | :---: |
| Functional Suitability | 4.56 | Excellent |
| Performance Efficiency | 4.44 | Excellent |
| Compatibility | 4.33 | Excellent |
| Usability | 3.93 | Very Good |
| Reliability | 4.42 | Excellent |
| Security | 4.27 | Excellent |
| Maintainability | 4.2 | Very Good |
| Portability | 4.11 | Very Good |
| **Overall Mean** | 4.24 | Excellent |

In Table 4 presents the results of the evaluation conducted by three I.T. specialists. For each criterion, the mean, ranking, and qualitative interpretation are shown in the table. The average evaluation score for software performance was **4.24**, which is considered Excellent overall. This implies that the system is user-friendly, dependable, easy to use, resource-efficient, and manageable. It also meets the needs of the user.  
The system's **Functional Suitability** was rated as **excellent** with a score of **4.56**. As evidenced by its accuracy, appropriateness, and completeness, this shows that the system has achieved its main objective.  
**Performance Efficiency** received a score of **4.44**, which is considered **excellent**. This clearly demonstrates that the system has accomplished its primary goal, as evidenced by its operational behavior, resource efficiency, and capacity.  
The **Compatibility** scored an outstanding rating of **4.33**, which is considered **excellent**. This amply illustrates the system's achievement of its main objective, which is further delineated by its appropriateness, learnability, operability, protection against user error, accessibility, and user interface aesthetics.  
**Usability** was given a **3.93** rating, which is considered **very good**. This shows that regardless of their past knowledge of computers and systems in general, both users and evaluators found the system to be easily learnable and user-friendly. This suggests that the graphical user interface (GUI) of the system is attractive and well-designed**.**  
The system's **Reliability** performance was scored **4.42**, which is an **excellent** result. This demonstrates that the system has accomplished its primary goal, which is further defined by its maturity, availability, and fault tolerance.  
The confidentiality, integrity, accountability, and authenticity of a system are all **Security** characteristics of software. This attribute received a grade of **4.27**, which is considered **excellent**.  
The **maintainability** function of the system obtained a score of **4.2,** which is considered **very good**. The qualities of a system that indicate maintainability are modularity, reusability, analyzability, modifiability, and testability.  
The **Portability** of the system was the last feature to be evaluated. With a rating of **4.11**, it achieved a **very good** score in this area. This metric is subdivided into subcategories including replaceability, compliance, simplicity of installation and configuration, and platform and environment compatibility.  
In ranking, **Functional Suitability** is ranked highest with a value of **4.56**, followed by **Performance Efficiency** at **4.44**. With ratings of **4.43** for **Reliability**, **4.33** for **Compatibility**, **4.27** for **Security**, **4.2** for **Maintainability**, **4.11** for **Portability**, and **3.93** for **Usability**, **Usability** receives the lowest ranking.  
Among the metrics that were used in ISO 25010 **Usability** has the highest score in Non – I.T. Experts while **Functional Suitability** has a highest score in I.T. Experts.

Table 5: *Evaluation Results of Non-I.T. Experts*

| Criteria | Mean | Descriptive Rating |
| ----- | :---: | :---: |
| Functional Suitability | 4.37 | Excellent |
| Performance Efficiency | 4.39 | Excellent |
| Usability | 4.44 | Excellent |
| Reliability | 4.33 | Excellent |
| **Overall Mean** | 4.38 | Excellent |

# 

Table 5 shows the Non-IT results mentioned. **Forty-seven** of the respondents were selected to participate in the expert review of the system. The system obtained an excellent rating, with an overall mean of **4.38** from the known number of system evaluators. Because the other four were difficult for non-IT experts to evaluate, only four characteristics were used.

The system's **Functional Suitability** obtained a score of **4.37**, which was considered **excellent**. This proves that the system has achieved its main goal, which is further indicated by its appropriateness, accuracy, and completeness.

The score for **Performance Efficiency** was **4.39**, which is considered as **excellent**. Based on the system's capability, resource efficiency, and operational behavior, it is evident that the main objective has been achieved.

The rating for **Usability** was **4.44**, which is considered **excellent**. This indicates that regardless of their prior computer and system-related experience, both users and evaluators found the system to be easily accessible and simple to use. This suggests that the graphical user interface of the system is visually captivating and well-designed.

The **Reliability** performance of the system earned an **excellent** rating of **4.33**. This proves that the system's primary objectives of fault tolerance, recoverability, availability, and maturity were successfully achieved.

The program has been determined to have an adequate rating based on the combined evaluations of its users and IT experts. It indicates that a high degree of program acceptability is present among the participants. The total mean needs to be at least 4.20 to 5.50 in order to quantify this **Excellent** rating.

# 

# **DISCUSSION** {#discussion}

The entire topic is covered in this chapter. Included are a synopsis of the results, conclusions, and suggestions for enhancing the system's functionality.

## **Summary of Findings** {#summary-of-findings}

In summary, drivers frequently have difficulties trying to find a parking space in a business or nearby parking garage. To address these issues, researchers developed Smart Parking Management Using Machine Learning. This technology helps drivers secure spots in advance so they don't have to worry about finding parking when they get there. The system received an overall rating from non-IT respondents of 4.38, which is comparable to an excellent rating. This indicates that the public can benefit from and find the Smart Parking Management System using Machine Learning suitable for their needs. and is appropriate for their surroundings and equipped with characteristics that allow it to function in a parking lot.  
Lastly, Smart Parking Management System using Machine Learning received an overall rating from the IT specialists of 4.24, which is considered excellent. Three experts' standards were satisfied by the system, indicating that it is suitable for general public usage.

## **Conclusions** {#conclusions}

	A major step in the right direction towards resolving the difficulties associated with parking cars in a rapidly evolving environment is the creation and deployment of a machine learning-powered smart parking management system. Numerous vehicle owners have to wait in long queues to obtain parking, and one of the main causes of this is that the facilities don't have real-time monitoring of the available spots, which leads to traffic congestion. Drivers can receive assistance in finding a parking spot by using the Smart Parking Management Using Machine Learning within the facility, saving them time from having to search for a parking space. 	Owners of vehicles will be able to drive smoothly to an available parking space without creating traffic, saving them time and effort.

## **Recommendations** {#recommendations}

	The researchers will provide recommendations for enhancing the system's features and architecture. Furthermore, the suggestions stem from the constraints of the research, participant assessment, encompassing the three I.T. specialists as well as the conclusion. The system should take into account including a parking option for visitors, according to IT experts, to make it even more user-friendly and expand the scope of the research.It should also include how well the system works in a range of weather conditions and how well it adjusts to the time of day in the event of a hot morning or a dark night. The experts advise considering the legal and constitutional ramifications before putting in place a smart parking management system. Improved data quality and cost management will also help to make the system more dependable in terms of real-time data collecting, and the researchers advise collaborating with legal professionals to guarantee compliance with data privacy and liability issues. The researchers advise financial sustainability through innovative cost-sharing arrangements, public-private collaborations, and financing exploration. In order to ensure dependable operation and extend the life of the smart parking infrastructure, suggests developing a comprehensive maintenance program for the cameras and equipment. As part of your proactive vulnerability management strategy, include stringent security controls in the system architecture, such as regular security audits, encryption, and ongoing monitoring. Ensure a successful and enduring implementation by optimizing user adoption strategies.

# **REFERENCES** {#references}

Abbasi, A. F., & Samsudin, K. A. (2017). Smart parking system using IoT technology. Procedia Computer Science, 124, 656-663.   
Retrieved from   
[https://www.semanticscholar.org/paper/Smart-Parking-System-using-IoT-ElakyaR-Seth/](https://www.semanticscholar.org/paper/Smart-Parking-System-using-IoT-ElakyaR-Seth/)  
Baimakhanova, R., & Tokhtarova, M. (2019). Smart parking system: A review. International Journal of Emerging Trends in Engineering Research, 7(6), 5556-5561. Retrieved from   
[https://www.ijert.org/Review-Paper-on-Smart-Parking-System](https://www.ijert.org/Review-Paper-on-Smart-Parking-System)  
Huang, C. C., Wu, M. S., & Chen, J. M. (2019). A smart parking management system based on IoT technology. Journal of Electrical and Computer Engineering, 2019, 1-9. Retrieved from  
 [https://www.ijeat.org/wp-content/uploads/papers/v9i1/A1963109119.pdf](https://www.ijeat.org/wp-content/uploads/papers/v9i1/A1963109119.pdf)  
INRIX. (2017). INRIX Global Traffic Scorecard. Retrieved from   
	[https://inrix.com/scorecard/](https://l.messenger.com/l.php?u=https%3A%2F%2Finrix.com%2Fscorecard%2F\&h=AT2XF-JDTBkib6LnVAhE1IFtjz8tnP6Bc5Rm49iDiJOW5Ck-cbRMKu0CKjt2Pq6OnhE5tg8dn0ll5Moq3OoHndwHDJUXOyYN7mYdp\_xLfOySpYxxzvLYj867WRZh1kMXCRnQ0w)  
Japan International Cooperation Agency. (2014). Metro Manila Transport Infrastructure Development Project (MMTIDP): Metro Manila Urban Transportation Integration Study (MMUTIS) Final Report Volume 2\. Retrieved from   
[https://openjicareport.jica.go.jp/pdf/12133855\_01.pdf](https://openjicareport.jica.go.jp/pdf/12133855\_01.pdf)  
Kaur, M., & Mittal, P. (2019). Smart parking system using IoT and machine learning. International Journal of Innovative Technology and Exploring Engineering, 8(9), 2995-3000. Retrieved from   
[https://www.ijert.org/Review-Paper-on-Smart-Parking-System](https://www.ijert.org/Review-Paper-on-Smart-Parking-System)  
Lee, M. S., Kim, J. H., & Hwang, S. W. (2019). Development of a smart parking system using IoT and machine learning. Electronics, 8(![😎][image3], 919\. Retrieved from   
[https://www.researchgate.net/publication/354234932\_Development\_of\_Smart\_Parking\_System\_using\_Internet\_of\_Things\_Concept](https://www.researchgate.net/publication/354234932\_Development\_of\_Smart\_Parking\_System\_using\_Internet\_of\_Things\_Concept)  
Li, Z., Zhang, X., & Jin, X. (2021). Design and implementation of a smart parking system based on IoT and machine learning. Journal of Ambient Intelligence and Humanized Computing, 12(5), 4823-4833.Retrieved from   
	[https://core.ac.uk/download/pdf/80720462.pdf](https://core.ac.uk/download/pdf/80720462.pdf)  
Nguyen, T. H. T., Nguyen, T. P., Nguyen, T. T., & Nguyen, D. K. (2019). Smart parking system based on IoT and machine learning. In Proceedings of the 2019 11th International Conference on Knowledge and Systems Engineering (KSE) (pp. 60-65). Retrieved from   
	[https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377](https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377)  
Onodera, N., Noda, N., & Seki, H. (2020). Implementation of a smart parking system using machine learning and IoT. Journal of Sensors, 2020, 1-10. Retrieved from   
	[https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377](https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377)  
Perera, C., Ranasinghe, W. M. R., & Sirisena, S. K. (2021). Development of a smart parking system using IoT and machine learning. In Proceedings of the 2021 8th International Conference on Electrical and Electronics Engineering (ICEEE) (pp. 1-5). Retrieved from  
[https://www.researchgate.net/publication/354234932\_Development\_of\_Smart\_Parking\_System\_using\_Internet\_of\_Things\_Concept](https://www.researchgate.net/publication/354234932\_Development\_of\_Smart\_Parking\_System\_using\_Internet\_of\_Things\_Concept)  
Shaikh, N., & Chandurkar, R. (2019). IoT based smart parking system using machine learning. In Proceedings of the 2019 3rd International Conference on Communication System, Computing and IT Applications (CSCITA) (pp. 1-5). Retrieved from   
	[https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377](https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3563377)  
Shaheen, S., Cohen, A. P., & Chu, B. (2012). Innovative Mobility Carsharing Outlook: Carsharing Market Overview, Analysis, and Trends. Transportation Sustainability Research Center, University of California, Berkeley. Retrieved from   
	[https://escholarship.org/uc/item/61q03282](https://escholarship.org/uc/item/61q03282)  
Park, J. H., Lee, J. W., & Kim, J. S. (2015). Smart parking system for smart cities. International Journal of Distributed Sensor Networks, 11(4), 1-8. Retrieved from   
	[https://www.mdpi.com/1424-8220/15/7/15443](https://www.mdpi.com/1424-8220/15/7/15443)  
Aijazi, A. K., & Javaid, A. (2018). Smart parking management system using internet of things. In 2018 International Conference on Applied Engineering (pp. 1-6). Retrieved from   
	[https://www.ijeat.org/wp-content/uploads/papers/v9i1/A1963109119.pdf](https://www.ijeat.org/wp-content/uploads/papers/v9i1/A1963109119.pdf)  
Schmitz, M. F., Kollakowski, C., Scholz, J., Hobeck, J., & Becker, J. (2018). Smart parking: a systematic literature review. In Proceedings of the 26th European Conference on Information Systems (ECIS) (pp. 1-16). Retrieved from   
	[https://www.mdpi.com/2624-6511/4/2/32](https://www.mdpi.com/2624-6511/4/2/32)  
Wu, J., & Zhang, Y. (2019). Smart parking reservation system for city application. In 2019 5th International Conference on Computing and Artificial Intelligence (pp. 185-190). Retrieved from   
	[https://www.mdpi.com/2076-3417/10/11/3872](https://www.mdpi.com/2076-3417/10/11/3872)  
Atmos Wardoyo, H. (2018). Research Methods in TEFL Studies: Descriptive. Retrieved from Journal of Language Teaching and Research:   
	[http://academypublication.com/issues2/jltr/vol09/01/25.pdf](http://academypublication.com/issues2/jltr/vol09/01/25.pdf)  
Nolle, T. (2021). What is a Data Flow Diagram (DFD)? TechTarget. Retrieved June 25, 2022, from Park Buddy: A Web Application Hassle-Free Parking Finder 47  
[https://www.techtarget.com/searchdatamanagement/definition/data-flow-diagramDFD](https://www.techtarget.com/searchdatamanagement/definition/data-flow-diagramDFD)  
Statistics Canada. (2021). Retrieved from Statistics Canada:   
	[https://www.statcan.gc.ca/en/microdata/rtra/training/programming/percent](https://www.statcan.gc.ca/en/microdata/rtra/training/programming/percent)  
Palinkas, L. A., Horwitz, S. M., Green, C. A., Wisdom, J. P., Duan, N., & Hoagwood, K. (2015). *Purposeful sampling for qualitative data collection and analysis in mixed method implementation research. Administration and Policy in Mental Health and Mental Health Services Research, 42(5), 533-544. Retrieved from*   
	*[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4012002/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4012002/)*  
*Weerdt, J. D. (2020, February). What can we learn from experimenting with survey methods? Retrieved from*  
[*https://www.annualreviews.org/doi/full/10.1146/annurev-resource-103019-105958\#\_i2*](https://www.annualreviews.org/doi/full/10.1146/annurev-resource-103019-105958\#\_i2)  
*Bhat. (2019). Online research: Definition, Methods, Types and Execution. Retrieved from QuestionsPro:*   
*https://www.questionpro.com/blog/execute-online-research/ Elsonbaty, A., & Shams, M. (2020). The smart parking management system. arXivpreprint arXiv:2009.13443.*   
*Amadebai, E. (2019). The Importance of Data Analysis in Research – Analytics forDecisions. Analytics for Decisions. Retrieved June 25, 2022, from*  
[*https://www.analyticsfordecisions.com/importance-of-data-analysis-in-research/*](https://www.analyticsfordecisions.com/importance-of-data-analysis-in-research/)  
*Glen, S. (2020). Arithmetic Mean: Definition How to Find it. Retrieved from StatisticsHowTo.com:*   
[*https://www.statisticshowto.com/arithmetic-mean/*](https://www.statisticshowto.com/arithmetic-mean/)

## **Appendix A: Evaluation Instrument for I.T Experts** {#appendix-a:-evaluation-instrument-for-i.t-experts}

**Evaluation Instrument**  
**(I.T. Experts)**

Name (Optional): \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Age: \_\_\_\_\_\_\_\_\_\_\_ Sex: \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Date Administered: 			     Time: \_\_\_\_\_\_   Administered by: 			  
Name of the Company:									  
Address: 											  
Designation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   Department: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**QUESTIONNAIRE**  
Please indicate a check mark (☑) under the column that best describes your responses for each item about the **\[name of your locale\]**.  Please use the rating below:  
**Numerical Rating				Equivalent**  
5 					Excellent  
4 					Very Good 			  
3					Good  
2					Fair  
1					Poor

| INDICATORS | 5 | 4 | 3 | 2 | 1 |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Functional Suitability** |  |  |  |  |  |
| **Functional completeness.** Degree to which the set of functions covers all the specified tasks and user objectives. |  |  |  |  |  |
| **Functional correctness.** Degree to which a product or system provides the correct results with the needed degree of precision. |  |  |  |  |  |
| **Functional appropriateness.** Degree to which the functions facilitate the accomplishment of specified tasks and objectives. |  |  |  |  |  |
| **Performance efficiency** |  |  |  |  |  |
| **Time behavior.** Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements. |  |  |  |  |  |
| **Resource utilization.** Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements. |  |  |  |  |  |
| **Capacity.** Degree to which the maximum limits of a product or system parameter meet requirements. |  |  |  |  |  |
| **Compatibility** |  |  |  |  |  |
| **Co-existence.** Degree to which a product can perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product. |  |  |  |  |  |
| **Interoperability.** Degree to which two or more systems, products or components can exchange information and use the information that has been exchanged. |  |  |  |  |  |
| **Usability** |  |  |  |  |  |
| **Appropriateness recognizability.** Degree to which users can recognize whether a product or system is appropriate for their needs. |  |  |  |  |  |
| **Learnability.** degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use. |  |  |  |  |  |
| **Operability.** Degree to which a product or system has attributes that make it easy to operate and control. |  |  |  |  |  |
| **User error protection.** Degree to which a system protects users against making errors. |  |  |  |  |  |
| **User interface aesthetics.** Degree to which a user interface enables pleasing and satisfying interaction for the user. |  |  |  |  |  |
| **Accessibility.** Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use. |  |  |  |  |  |
| **Reliability** |  |  |  |  |  |
| **Maturity.** Degree to which a system, product or component meets needs for reliability under normal operation. |  |  |  |  |  |
| **Availability.** Degree to which a system, product or component is operational and accessible when required for use. |  |  |  |  |  |
| **Fault tolerance.** Degree to which a system, product or component operates as intended despite the presence of hardware or software faults. |  |  |  |  |  |
| **Recoverability.** Degree to which, in the event of an interruption or a failure, a product or system can recover the data directly affected and re-establish the desired state of the system. |  |  |  |  |  |
| **Security** |  |  |  |  |  |
| **Confidentiality.** Degree to which a product or system ensures that data are accessible only to those authorized to have access. |  |  |  |  |  |
| **Integrity.** Degree to which a system, product or component prevents unauthorized access to, or modification of, computer programs or data. |  |  |  |  |  |
| **Non-repudiation.** degree to which actions or events can be proven to have taken place, so that the events or actions cannot be repudiated later. |  |  |  |  |  |
| **Accountability.** Degree to which the actions of an entity can be traced uniquely to the entity. |  |  |  |  |  |
| **Authenticity.** Degree to which the identity of a subject or resource can be proved to be the one claimed. |  |  |  |  |  |
| **Maintainability** |  |  |  |  |  |
| **Modularity.** Degree to which a system or computer program is composed of discrete components such that a change to one component has minimal impact on other components. |  |  |  |  |  |
| **Reusability.** Degree to which an asset can be used in more than one system, or in building other assets. |  |  |  |  |  |
| **Analyzability.** Degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change to one or more of its parts, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified. |  |  |  |  |  |
| **Modifiability.** Degree to which a product or system can be effectively and efficiently modified without introducing defects or degrading existing product quality. |  |  |  |  |  |
| **Testability.** Degree of effectiveness and efficiency with which test criteria can be established for a system, product or component and tests can be performed to determine whether those criteria have been met. |  |  |  |  |  |
| **H. Portability** |  |  |  |  |  |
| **Adaptability.** Degree to which a product or system can effectively and efficiently be adapted for different or evolving hardware, software or other operational or usage environments. |  |  |  |  |  |
| **Install ability.** Degree of effectiveness and efficiency with which a product or system can be successfully installed and/or uninstalled in a specified environment. |  |  |  |  |  |
| **Replaceability.** Degree to which a product can replace another specified software product for the same purpose in the same environment. |  |  |  |  |  |

## 

## 

## 

## 

##   

## 

## **Appendix B: Frequency Count of Distribution for I.T Experts** {#appendix-b:-frequency-count-of-distribution-for-i.t-experts}

**Evaluation Instrument**  
**(I.T. Experts)**

Name (Optional): \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Age: \_\_\_\_\_\_\_\_\_\_\_ Sex: \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Date Administered: 			     Time: \_\_\_\_\_\_   Administered by: 			  
Name of the Company:									  
Address: 											  
Designation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   Department: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**QUESTIONNAIRE**  
Please indicate a check mark (☑) under the column that best describes your responses for each item about the **\[name of your locale\]**.  Please use the rating below:  
**Numerical Rating				Equivalent**  
5 					Excellent  
4 					Very Good 			  
3					Good  
2					Fair  
1					Poor

| INDICATORS | 5 | 4 | 3 | 2 | 1 |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Functional Suitability** |  |  |  |  |  |
| **Functional completeness.** Degree to which the set of functions covers all the specified tasks and user objectives. | 2 | 1 | 0 | 0 | 0 |
| **Functional correctness.** Degree to which a product or system provides the correct results with the needed degree of precision. | 2 | 0 | 1 | 0 | 0 |
| **Functional appropriateness.** Degree to which the functions facilitate the accomplishment of specified tasks and objectives. | 2 | 1 | 0 | 0 | 0 |
| **Performance efficiency** |  |  |  |  |  |
| **Time behavior.** Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements. | 2 | 1 | 0 | 0 | 0 |
| **Resource utilization.** Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements. | 2 | 1 | 0 | 0 | 0 |
| **Capacity.** Degree to which the maximum limits of a product or system parameter meet requirements. | 1 | 2 | 0 | 0 | 0 |
| **Compatibility** |  |  |  |  |  |
| **Co-existence.** Degree to which a product can perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product. | 1 | 2 | 0 | 0 | 0 |
| **Interoperability.** Degree to which two or more systems, products or components can exchange information and use the information that has been exchanged. | 1 | 2 | 0 | 0 | 0 |
| **Usability** |  |  |  |  |  |
| **Appropriateness recognizability.** Degree to which users can recognize whether a product or system is appropriate for their needs. | 0 | 1 | 2 | 0 | 0 |
| **Learnability.** degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use. | 0 | 2 | 1 | 0 | 0 |
| **Operability.** Degree to which a product or system has attributes that make it easy to operate and control. | 1 | 1 | 1 | 0 | 0 |
| **User error protection.** Degree to which a system protects users against making errors. | 1 | 1 | 1 | 0 | 0 |
| **User interface aesthetics.** Degree to which a user interface enables pleasing and satisfying interaction for the user. | 0 | 3 | 0 | 0 | 0 |
| **Accessibility.** Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use. | 0 | 3 | 0 | 0 | 0 |
| **Reliability** |  |  |  |  |  |
| **Maturity.** Degree to which a system, product or component meets needs for reliability under normal operation. | 1 | 1 | 1 | 0 | 0 |
| **Availability.** Degree to which a system, product or component is operational and accessible when required for use. | 1 | 2 | 0 | 0 | 0 |
| **Fault tolerance.** Degree to which a system, product or component operates as intended despite the presence of hardware or software faults. | 1 | 1 | 1 | 0 | 0 |
| **Recoverability.** Degree to which, in the event of an interruption or a failure, a product or system can recover the data directly affected and re-establish the desired state of the system. | 0 | 3 | 0 | 0 | 0 |
| **Security** |  |  |  |  |  |
| **Confidentiality.** Degree to which a product or system ensures that data are accessible only to those authorized to have access. | 1 | 2 | 0 | 0 | 0 |
| **Integrity.** Degree to which a system, product or component prevents unauthorized access to, or modification of, computer programs or data. | 1 | 2  | 0 | 0 | 0 |
| **Non-repudiation.** degree to which actions or events can be proven to have taken place, so that the events or actions cannot be repudiated later. | 0 | 2 | 1 | 0 | 0 |
| **Accountability.** Degree to which the actions of an entity can be traced uniquely to the entity. | 2 | 1 | 0 | 0 | 0 |
| **Authenticity.** Degree to which the identity of a subject or resource can be proved to be the one claimed. | 1 | 2 | 0 | 0 | 0 |
| **Maintainability** |  |  |  |  |  |
| **Modularity.** Degree to which a system or computer program is composed of discrete components such that a change to one component has minimal impact on other components. | 1 | 1 | 1 | 0 | 0 |
| **Reusability.** Degree to which an asset can be used in more than one system, or in building other assets. | 2 | 1 | 0 | 0 | 0 |
| **Analyzability.** Degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change to one or more of its parts, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified. | 1 | 2 | 0 | 0 | 0 |
| **Modifiability.** Degree to which a product or system can be effectively and efficiently modified without introducing defects or degrading existing product quality. | 1 | 1 | 1 | 0 | 0 |
| **Testability.** Degree of effectiveness and efficiency with which test criteria can be established for a system, product or component and tests can be performed to determine whether those criteria have been met. | 1 | 1 | 1 | 0 | 0 |
| **H. Portability** |  |  |  |  |  |
| **Adaptability.** Degree to which a product or system can effectively and efficiently be adapted for different or evolving hardware, software or other operational or usage environments. | 1 | 1 | 1 | 0 | 0 |
| **Install ability.** Degree of effectiveness and efficiency with which a product or system can be successfully installed and/or uninstalled in a specified environment. | 1 | 1 | 1 | 0 | 0 |
| **Replaceability.** Degree to which a product can replace another specified software product for the same purpose in the same environment. | 1 | 2 | 0 | 0 | 0 |

## 

## 

## 

## 

## 

## **Appendix C: Frequency Count Distribution and Percentage of I.T Experts** {#appendix-c:-frequency-count-distribution-and-percentage-of-i.t-experts}

Table 6: *Accuracy of the system* *in terms of functional suitability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent	 | 2 | 66.67% |
| Very Good | 0.66 | 22.22% |
| Good | 0.33 | 11.11% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 7: *Accuracy of the system* *in terms of performance efficiency*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 1.67 | 55.55% |
| Very Good | 1.3 | 44.44% |
| Good | 0 | 0 |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 8: *Accuracy of the system* *in terms of compatibility*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 1 | 33.33% |
| Very Good | 2 | 66.67% |
| Good | 0 | 0 |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 9: *Accuracy of the system* *in terms of usability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 0.33 | 11.11% |
| Very Good | 1.83 | 61.11% |
| Good | 0.83 | 27.77% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 10: *Accuracy of the system* *in terms of reliability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 0.75 | 25% |
| Very Good | 1.75 | 58.33% |
| Good | 0.5 | 16.67% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 11: *Accuracy of the system* *in terms of security*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 1 | 33.33% |
| Very Good | 1.8 | 60% |
| Good | 0.2 | 6.67% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

Table 12: *Accuracy of the system* *in terms of maintainability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 1.2 | 40% |
| Very Good | 1.2 | 40% |
| Good | 0.6 | 20% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

 Table 13: *Accuracy of the system* *in terms of portability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 1 | 33.33% |
| Very Good | 1.33 | 44.44% |
| Good | 0.67 | 22.22% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 3 | 100% |

## 

## **Appendix D: Evaluation Instrument for Non-IT Experts** {#appendix-d:-evaluation-instrument-for-non-it-experts}

**Evaluation Instrument**  
**(NON- I.T. Experts)**

Name (Optional): \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Age: \_\_\_\_\_\_\_\_\_\_\_ Sex: \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Date Administered: 			     Time: \_\_\_\_\_\_   Administered by: 			  
Name of the Company:									  
Address: 											  
Designation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   Department: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**QUESTIONNAIRE**  
Please indicate a check mark (☑) under the column that best describes your responses for each item about the **\[name of your locale\]**.  Please use the rating below:  
**Numerical Rating				Equivalent**  
5 					Excellent  
4 					Very Good 			  
3					Good  
2					Fair  
1					Poor

| INDICATORS | 5 | 4 | 3 | 2 | 1 |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Functional Suitability** |  |  |  |  |  |
| **Functional completeness.** Degree to which the set of functions covers all the specified tasks and user objectives. |  |  |  |  |  |
| **Functional correctness.** Degree to which a product or system provides the correct results with the needed degree of precision. |  |  |  |  |  |
| **Functional appropriateness.** Degree to which the functions facilitate the accomplishment of specified tasks and objectives. |  |  |  |  |  |
| **Performance efficiency** |  |  |  |  |  |
| **Time behavior.** Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements. |  |  |  |  |  |
| **Resource utilization.** Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements. |  |  |  |  |  |
| **Capacity.** Degree to which the maximum limits of a product or system parameter meet requirements. |  |  |  |  |  |
| **Usability** |  |  |  |  |  |
| **Appropriateness recognizability.** Degree to which users can recognize whether a product or system is appropriate for their needs. |  |  |  |  |  |
| **Learnability.** degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use. |  |  |  |  |  |
| **Operability.** Degree to which a product or system has attributes that make it easy to operate and control. |  |  |  |  |  |
| **User error protection.** Degree to which a system protects users against making errors. |  |  |  |  |  |
| **User interface aesthetics.** Degree to which a user interface enables pleasing and satisfying interaction for the user. |  |  |  |  |  |
| **Accessibility.** Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use. |  |  |  |  |  |
| **Reliability** |  |  |  |  |  |
| **Maturity.** Degree to which a system, product or component meets needs for reliability under normal operation. |  |  |  |  |  |
| **Availability.** Degree to which a system, product or component is operational and accessible when required for use. |  |  |  |  |  |
| **Fault tolerance.** Degree to which a system, product or component operates as intended despite the presence of hardware or software faults. |  |  |  |  |  |
| **Recoverability.** Degree to which, in the event of an interruption or a failure, a product or system can recover the data directly affected and re-establish the desired state of the system. |  |  |  |  |  |

## **Appendix E: Frequency Count of Distribution for Non- I.T Experts** {#appendix-e:-frequency-count-of-distribution-for-non--i.t-experts}

**Evaluation Instrument**  
**(NON- I.T. Experts)**

Name (Optional): \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Age: \_\_\_\_\_\_\_\_\_\_\_ Sex: \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Date Administered: 			     Time: \_\_\_\_\_\_   Administered by: 			  
Name of the Company:									  
Address: 											  
Designation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   Department: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**QUESTIONNAIRE**  
Please indicate a check mark (☑) under the column that best describes your responses for each item about the **\[name of your locale\]**.  Please use the rating below:  
**Numerical Rating				Equivalent**  
5 					Excellent  
4 					Very Good 			  
3					Good  
2					Fair  
1					Poor

| INDICATORS | 5 | 4 | 3 | 2 | 1 |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Functional Suitability** |  |  |  |  |  |
| **Functional completeness.** Degree to which the set of functions covers all the specified tasks and user objectives. | 29 | 12 | 6 | 0 | 0 |
| **Functional correctness.** Degree to which a product or system provides the correct results with the needed degree of precision. | 20 | 22 | 5 | 0 | 0 |
| **Functional appropriateness.** Degree to which the functions facilitate the accomplishment of specified tasks and objectives. | 20 | 21 | 6 | 0 | 0 |
| **Performance efficiency** |  |  |  |  |  |
| **Time behavior.** Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements. | 23 | 18 | 6 | 0 | 0 |
| **Resource utilization.** Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements. | 24 | 20 | 3 | 0 | 0 |
| **Capacity.** Degree to which the maximum limits of a product or system parameter meet requirements. | 19 | 26 | 2 | 0 | 0 |
| **Usability** |  |  |  |  |  |
| **Appropriateness recognizability.** Degree to which users can recognize whether a product or system is appropriate for their needs. | 25 | 17 | 5 | 0 | 0 |
| **Learnability.** degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use. | 23 | 21 | 3 | 0 | 0 |
| **Operability.** Degree to which a product or system has attributes that make it easy to operate and control. | 25 | 17 | 5 | 0 | 0 |
| **User error protection.** Degree to which a system protects users against making errors. | 24 | 17 | 6 | 0 | 0 |
| **User interface aesthetics.** Degree to which a user interface enables pleasing and satisfying interaction for the user. | 28 | 15 | 4 | 0 | 0 |
| **Accessibility.** Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use. |  |  |  |  |  |
| **Reliability** |  |  |  |  |  |
| **Maturity.** Degree to which a system, product or component meets needs for reliability under normal operation. | 20 | 20 | 7 | 0 | 0 |
| **Availability.** Degree to which a system, product or component is operational and accessible when required for use. | 16 | 27 | 4 | 0 | 0 |
| **Fault tolerance.** Degree to which a system, product or component operates as intended despite the presence of hardware or software faults. | 25 | 15 | 7 | 0 | 0 |
| **Recoverability.** Degree to which, in the event of an interruption or a failure, a product or system can recover the data directly affected and re-establish the desired state of the system. | 22 | 20 | 5 | 0 | 0 |

## 

## 

## **Appendix F: Frequency Count Distribution and Percentage of Non- I.T Experts** {#appendix-f:-frequency-count-distribution-and-percentage-of-non--i.t-experts}

Table 14*: Accuracy of the system* *in terms of functional suitability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent	 | 23 | 48.94% |
| Very Good | 18.33 | 39% |
| Good | 5.66 | 12.06% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 47 | 100% |

Table 15*: Accuracy of the system* *in terms of performance efficiency*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 22 | 46.81% |
| Very Good | 21.33 | 45.39% |
| Good | 3.66 | 7.80% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 47 | 100% |

Table 16*: Accuracy of the system* *in terms of usability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent	 | 25 | 53.19% |
| Very Good | 17.4 | 37.02% |
| Good | 4.6 | 9.79% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 47 | 100% |

Table 17*: Accuracy of the system* *in terms of reliability*

| Factors | Frequency | Percentage |
| ----- | :---: | :---: |
| Excellent | 20.75 | 44.15% |
| Very Good | 20.5 | 43.61% |
| Good | 5.75 | 12.23% |
| Fair | 0 | 0 |
| Poor | 0 | 0 |
| Total | 47 | 100% |

## 

## 

## **Appendix G:  Use Case Diagram**  {#appendix-g:-use-case-diagram}

## **Appendix H:  Flow Chart**  {#appendix-h:-flow-chart}

	

## **Appendix I: Sequence Diagram** {#appendix-i:-sequence-diagram}

## **Appendix J: I.T Experts Resume** {#appendix-j:-i.t-experts-resume}

**RICO PEARSON CELEDIO**  
**Address:** Blk.12, Lot 24, Phase 4, Greenville Homes,   
                 Gov. Remulla Dr., Sahud – Ulan, Tanza, Cavite          
**Email Address:** [pearson.rico@gmail.com](mailto:pearson.rico@gmail.com)  
**Cell phone \#:** 0908 – 814 \- 4029

**WORK EXPERIENCE**

**Position**: **PRODUCTION ASSISTANT MANAGER**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: December 01, 2020 \- present

**JOB DESCRIPTION**

* Overall in charge in Production (SMT, DIPPING , PCBA \- BOL and MECHANICAL ASSEMBLY).  
* Daily Check production schedule vs. Actual production output if meet the base on customer daily and shipment requirement.  
* Monitor material delivery from supplier and coordinate to PIC if there are changes to Production Plan to make sure that shipping schedule are meet.   
* Conduct Weekly meeting with Section Head and Senior Supervisor for status of Production line and discuss other issue’s  
* Generate weekly report and report during Management Weekly Meeting Production result and status  
* Make Monthly Cost Reduction Result and report to Operations Manager, Factory Manager and President   
* Oversees production monthly inventory and check if monthly target for inventory loss was meet.

**Position**: **PRODUCTION SECTION HEAD**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: January 01, 2019 – December 01, 2020

**JOB DESCRIPTION**

* Acts as the head of Production area (PCBA \- BOL and Mechanical Assembly).  
* Make sure that the production process runs efficiently.  
* Daily Check production schedule vs. Actual production output if meet the base on customer daily and shipment requirement.  
* Monitor material delivery from supplier and coordinate to PIC if there are changes to Production Plan to make sure that shipping schedule are meet.   
* Conduct Weekly meeting with Senior Supervisor for status of Production line and discuss other issue’s  
* Make Monthly Cost Reduction Result and report to Plant Manager and President   
* Oversees production monthly inventory and check if monthly target for inventory loss was meet.




**Position**: **PRODUCTION SENIOR SUPERVISOR**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: June 01, 2015 – January 01, 2019

**JOB DESCRIPTION**

* Over all In charge on Control Panel Assembly for Slot Machine Line Project and Bill Validator / Bill Acceptor Mechanical Assembly.  
* Assumes Responsibility for the Project from start to finish  
* Creates Team that will oversee the project. Team Consist of Process Engineer, Equipment Engineer, Production Engineer and operators    
* Responsible for designation of Engineers for their individual task for project preparation  
* Responsible for planning of activities in preparation of the project and implement plan base on customers plan schedule.   
* Study new Product with the team, create Process Flow Procedure, generate Work Standard, get Standard time, Make table set – Up and floor plan, study tool and jigs to be use, submit proposal to management for approval and if Plan approve, execute plan as per Schedule.  
* Compute manpower to be use base on required output of Costumer  
* Responsible for hiring operator base on computed manpower  
* Responsible for Line monitoring during process. Make sure that line running smoothly  
* Monitor material to be used on production to ensure that no downtime will happen due to material shortage  
* Responsible for daily meeting of operators during end of Shift and discuss problems encountered during process, process rejects, output target etc.  
* Send daily report to Manager, Assistant Manager, Section Head for update of last days Production


  

**Position**: **PRODUCTION SUPERVISOR**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: November 10, 2014 – June 01, 2015

**JOB DESCRIPTION**

* **Planning and Verification of Scheduled and Actual Production Result.** Communicate production results, issues, decisions made, and directions taken effectively with shift preceding and following.  
    
  * **Training and Validation of Operators.** Monitors and develops operators’ skills and capabilities.  
      
  * **Line Productivity and Efficiency Monitoring and Support.** Hourly monitoring of output and downtime hence ensuring that assembly line meet its daily target requirement.

  * **Manpower Allocation and Planning.** Ensures enough and proper allotment of manpower in every process and explain shift production through metric-driven presentations by means of manpower.

  * **Process Improvements.** Improve process capability and production volume while maintaining and improving quality standards.

  * **Implementation of Work Standards, One- Point Lessons and Corrective Actions.** Establish procedures and make revisions for the product process improvements.

  * **Production Report, Engineering Report and Production History.** Ensures that accurate and day-to-day data are presented regarding all the production and process-related occurrences.

**Position**: **PRODUCTION ENGINEER**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: February  2013 – November  2014

**Position**: **PROCESS AND EQUIPMENT ENGINEER**  
**Department**: Manufacturing and Engineering  
**Company Name**: M.A. Technology, Inc.  
**Address**: Blk. 15 Lot 6 Phase 3, CEZ, Rosario, Cavite  
**Date**: January 2010  –  February 2013

**Position: EQUIPMENT MENTAINANCE ENGINEER**  
**Department**: Manufacturing and Engineering  
**Company Name**: Everlight Electronics Corp. Ltd..  
		Address: No. 37 Lane Guoguang, Yutian Village , 

		Yuanli Township Miaoli County 35874,   
                             Taiwan R.O.C   
**Date**: February 2006  – Decemeber 2008

**Position: TECHNICAL SUPPORT STAFF (PRODUCT TESTER)**  
**Department**: Research and Development  
**Company Name**: Lexmark Research and Development Corp.

**Address**: Innove Plaza, Samar Loop Corner Pasay Road  
               Cebu Business Park, Cebu City                                
**Date**: November  2004 – January 2006

**Awards and Achievements**

* **2012 MA Technology Employee of the Year Supervisory Category**

**SKILL/S**

* Computer Proficient (MS Word, MS Excel, MS Power point, etc)  
* Basic Knowledge in Electronics (Circuitry, Logic Circuits, etc)  
* Basic Knowledge in Programmable Logic Controller (PLC)  
* Knowledgeable on Failure Mode and Effects Analysis (FMEA) , Fault Tree Analysis (FTA), Statistical Process Control (SPC)  
* Managerial Skills (Organizing, Directing, Leading and Controlling)  
  


**MACHINE / HARDWAREHANDLED**  
						

* WIT In-Circuit Tester Inspection Pro IP-5800ST  
* Nihon-Garter Auto Tester (NCS) / Auto Taping (NCT)

	(NCS-1100 / 1100I/ 1100II / 1700/ 1680S / 1005\)

	(NCT-3100 / 3700 / 3800 / 3100I)

* Nihon-Garter Auto Tester NUS \- 0076	  
* AUTEC (Auto Tester/Auto Taping)					   
* Daitron Breaking Machine DBM 402R  
* KOTOBUKI Breaking Machine (BKM001K/BKM003K)  
* Carrier Tape Peel Force Tester  
* HIOS Electronic Screw Driver

* HIOS Automatic Screw Feeder 




**EDUCATIONAL BACKGROUND**

***College***	        		**CEBU INSTITUTE OF TECHNOLOGY**  
				N. Bacalso Avenue, Cebu City  
				Bachelor of Science in Computer Engineering   
Engineering (BS CpE)  
					October 2004

**PERSONAL INFORMATION**

**Date of Birth**		:	18 March 1980  
**Age**			:	42 years old  
**Height**			:	5’6”/175 cm  
**Weight**			:	70 kgs  
**Nationality**		:	Filipino  
**Language Spoken**	:	Tagalog and American English  
**Civil Status**		:	Married  
**Spouse** 			:	Jinnefer T. Celedio  
**Religion**			:	Roman Catholic

   

**AFFILIATION/S**

* **CEBU INSTITUTE OF TECHNOLOGY ALUMNI ASSOCIATION**  
* Member (October 2004- present)


  


  


  
**SEMINARS ATTENDED**

* **ISO 9001 : 2015 Awareness Seminar**  
  M.A. Technology Inc.   
  December 18 – 19, 2015  
    
  * **SPC (Statistical Process Control) Level 2**  
    M.A. Technology, Inc.  
    January 22, 2015  
      
  * **Keyence KV(PLC) Skills – Up Training Seminar**  
    Eagle Ridge and Country Club  
    Brgy. Amadeo, Gen. Trias, Cavite  
    March 26, 2014  
    

  * **Pokayoke Seminar**  
    M.A. Technology, Inc.  
    November 09, 2012  
      
  * **SPC (Statistical Process Control) Level 1**  
    M.A. Technology, Inc.  
    July 14, 2012  
      
      
      
      
  * **FAILURE MODE AND EFFECTS ANALYSIS**  
    M.A. Technology, Inc.  
    December 09, 2010  
      
* **ESD ( Electro Static Discharge Awareness Seminar** 

  M.A. Technology, Inc.

  January 29, 2011


  


  





  




 **Kervin Jumar D. Lopez**  
0999 – 494 – 4253

617 Sandra St., Nepo Subd., Angeles City, Pampanga Email Address: [kervinjumar.kj@gmail.com](mailto:kervinjumar.kj@gmail.com)

OBJECTIVE

To work in an established company that would help me to  
grow professionally, contribute skills and knowledge from work experience while achieving a high level of personal fulfillment.

EDUCATIONAL ATTAINMENT

2016-2020	**CITY COLLEGE OF ANGELES**

Arayat Blvd. Pampang, 2009 Angeles City Bachelor of Science Major in Computer Science Dean’s Lister  
1st year – 2nd year, 3rd year 2nd sem and 4th year

WORK EXPERIENCE

July 2023 – up to present **Servo IT Solutions**  
Associate Software Engineer II  
Olympus	Building,	11-11	Ramon	Dizon	Street. Diamond Subd. Balibago, Angeles City [consult@servoitsolutions.ph*.*](mailto:consult@servoitsolutions.ph)

May 3 2021 – July 2023	**Trackerteer Web Dev Corporation**  
Mobile App Developer  
Unit 1F Business Center 9, Philexcel Business Park, 2023, Clark Freeport, Pampanga

[hr@trackerteer.com](mailto:hr@trackerteer.com)

*Designing and developing advanced applications for the Android platform.*  
*Bug fixing and improving application performance.*

May 7 2019	GAME DEVELOPMENT, 6TH ALCUCOA REGIONAL SKILLS COMPETITION

Bulacan State University Participant

SEMINARS ATTENDED

December 1 2019	**WEB DEVELOPMENT 101**  
City College of Angeles  
Speaker: Jonathan James Castro

November 24 2019	**ARDUINO: A HANDS-ON INTRODUCTORY**  
WORKSHOP

City College of Angeles Speaker: Mhel Handrian Pineda

November 24 2019	**ARDUINO: INTRODUCTION AND PROGRAMMING**  
City College of Angeles Speaker: Mhel Handrian Pineda

RESEARCH PAPERS PREPARED

November 2018	**CHEMIX: AN ANDROID-APP AUGMENTED**  
REALITY OF THE PERIODIC TABLE OF THE ELEMENTS

A mobile application made in Unity that has a complete periodic table of elements which you can study and augment in real world. Each element shows you the augmented 3D objects that provides chemistry lessons, information and mind games which you can play.

				

## 

## 

## 

## 

## 

## **Appendix K: Researcher’s Resume** {#appendix-k:-researcher’s-resume}

**CUNANAN, CYJAY M.**  
017 SandraSt. Nepo Subd. Brgy. Sto. Rosario Angeles City, Pampanga 2009  
[cyjycnnn@gmail.com](mailto:cyjycnnn@gmail.com)   
\+63991-556-6068

**OBJECTIVES**

To achieve experience in a professional setting and to maximize my abilities for God's glory to demonstrate my skills and do more novel things with my work. That I’m constantly engaged in all assigned work and receptive to new experiences in order to advance as a professional and to establish rapport and collaborate as a professional worker with my team.

**PERSONAL INFORMATION**

**Age** 	        	:       	21 years old  
**Birthday**	:       	December 20, 2001  
**Gender**		:       	Male  
**Civil Status** 	:       	Single

**EDUCATIONAL BACKGROUND**

**Elementary**  
Sto. Rosario Elementary School  
2007 – 2013

**Secondary**  
Angeles City National Trade School(**SHS**)  
2018 – 2020

Angeles City National Trade School(**JHS**)  
2013 – 2018 

**Tertiary**  
Bachelor of Science in Computer Science  
City College of Angeles  
2020 – Present 

**TRAININGS ATTENDED**  	

ScrumStudy Targeting Success  
Scrum Fundamentals Certified Passer  
June 8, 2022

   
**PROFESSIONAL SKILLS**

* Troubleshooting  
* Programming using Different Languages  
  - Microsoft Visual Studio(VB)  
  -   HTML and PHP  
  - Java  
  - Python

   
**SEMINARS ATTENDED**

International Lecture Forum 2023  
“Information Technology as a Sustainable Channel to Knowledge Society”  
May 25, 2023

Empowering Innovations  
“Nurturing your capstone/thesis project for success”  
June 24, 2023

Introduction to Salesforce  
July 19, 2023

Train to Hire  
October 13, 2023

 

 

 

   
     CUNANAN CYJAY M.	      
    
 

**Garcia, Kurt Ryan C.**  
Brgy. Pampang Purok 5 Angeles City, Pampanga  
09756989705  
kurtryan43@gmail.com

**OBJECTIVE:**  
To showcase my ability and to explore more new things in work. Always active to every task that has been given and open for more learning experience to improve as a professional. To gain trust and coordinate with my team as a professional worker.

**PERSONAL INFORMATION:**

**Date of Birth		:**     November 27, 2001  
**Place of Birth		:**     Ormoc City , Leyte  
**Age			:**     22 years old   
**Gender		:**     Male  
**Civil Status		:**     Single  
**Nationality**        	**:**     Filipino  
**Religion		:**     Roman Catholic  
**Languages Spoken    :**     English, Tagalog, Pampango

|  |
| :---- |

**EDUCATIONAL BACKGROUND**  
City College of Angeles 						2020 \- Present  
Bachelor of Science in Computer Science  
Barangay Pampang, Angeles City

**Angeles City National Trade School (SHS)**           			2018 \- 2020  
**Angeles City National Trade School (JHS)**            			2013 \- 2018  
Angeles City, Pampanga

**M. Nepomuceno Elementary School** 				2007 \- 2013  
Angeles City, Pampanga

**ACHIEVEMENTS:**

* National Certificate II,

  Specialized in Electrical Installation and Maintenance

        April 17, 2018 \- April 17, 2023\.	  


* Scrumstudy

                  Scrum Fundamental Certified   
	      June 8, 2022

* Cisco Networking Academy 

                 Enterprise Networking, Security, and Automation Badge  
	     July 27, 2023 

* Cisco Networking Academy 

                  Linux Essential Certificate   
	      August 20, 2023                               

**WORK EXPERIENCE**

* McDonalds,

  Crew Trainer 

        May 29, 2018 \- January 15, 2023\.	   

                                  

**PROFESSIONAL SKILLS**

* Dedicated, determined and willing to learn and be trained  
* Working well in a team  
* Always having the initiative  
* Verbal and personal communication skills

* Troubleshooting  
* Programming using Different Languages

* Microsoft Visual Studio(VB)  
* HTML and PHP  
* Java  
* Python     
                                  

**SEMINAR ATTENDED**

* Empowering Innovations

  Nurturing your capstone/thesis project for success

        City College of Angeles, Angeles City Pampanga

        June 24, 2023


  





* International Lecture Forum 2023   
      Information Technology as a Sustainable Channel to Knowledge Society  
      City College of Angeles, Angeles City Pampanga,  
      May 25, 2023  
    
* Introduction to Salesforce  
     City College of Angeles, Angeles City Pampanga,  
     July 19, 2023  
  




**REFERENCES**  
**Fortunato C. Mesina**  
**Electrical teacher** 

**Bernardo B. Bonifacio**  
**Electrical teacher**

***I hereby declare that the above written particulars are true to the best of my knowledge and belief.***

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   
   **Kurt Ryan C. Garcia**     

## 

## 

## **Appendix L: Source Code** {#appendix-l:-source-code}

**SPMS\_Main.py**

from three\_obj\_classifv2 import obj\_classifier  
from segment import \*  
from customtkinter import \*  
import cv2  
from tkinter import \*  
import threading  
from queue import Queue  
import subprocess  
from PIL import ImageGrab, Image  
import os  
from CTkMessagebox import CTkMessagebox  
from CTkToolTip import \*  
from tktooltip import ToolTip

\#variables  
\#obj detection model  
user\_classif\_model \= r'C:\\Users\\DICT\\Desktop\\Entrance vid\\3\_class\_data\_set\\3\_classification\_weights\_v2.1\\best.pt' \# teaching, non\_teaching, staff

yolo\_pretrained\_model \=r"C:\\Users\\DICT\\Desktop\\SPMS\\weights\\yolov8n.pt" \#for vehicle classification  
video\_pathD \=r'C:\\Users\\DICT\\Desktop\\Entrance vid\\3\_class\_data\_set\\3class\_vid.mp4'

\#parking detection  
maskA \= 'C:/Users/DICT/Desktop/SPMS/Images/SAM.png'

video\_pathA \=r'C:/Users/DICT/Desktop/SPMS/Vid/SA\_vid\_loop.mp4'

maskB \= 'C:/Users/DICT/Desktop/SPMS/Images/SBM.png'  
video\_pathB \='C:/Users/DICT/Desktop/SPMS/Vid/SB\_vid\_loop.mp4'

maskC \= 'C:/Users/DICT/Desktop/SPMS/Images/SCM.png'  
video\_pathC \='C:/Users/DICT/Desktop/SPMS/Vid/SC\_vid\_loop.mp4'

parking\_lot\_1 \='Parking Lot A'  
parking\_lot\_2 \='Parking Lot B'  
parking\_lot\_3 \='Parking Lot C'

frame\_w \= 600  
frame\_h \= 500

data\_queue \= Queue()

data\_queue\_spot \= Queue()  
data\_q\_class \= Queue()  
data\_q\_has\_class \= Queue()  
def save\_configuration():  
    \# Ask the user for the file path to save the configuration  
    file\_path \= filedialog.asksaveasfilename(defaultextension=".ini", filetypes=\[("INI files", "\*.ini"), ("All files", "\*.\*")\])

    if file\_path:  
        \# Set the values in the ConfigParser  
        config \= {  
            'Paths': {  
                'video\_pathA': video\_pathA,

                'video\_pathB': video\_pathB,  
                'video\_pathC': video\_pathC,  
                'video\_pathD': video\_pathD,  
                'maskA': maskA,  
                'maskB': maskB,  
                'maskC': maskC  
            },  
            'ParkingLots': {  
                'parking\_lot\_1': parking\_lot\_1,

                'parking\_lot\_2': parking\_lot\_2,  
                'parking\_lot\_3': parking\_lot\_3  
            }  
        }

        \# Save the configuration to the selected file path  
        with open(file\_path, 'w') as configfile:  
            for section, values in config.items():  
                configfile.write(f'\[{section}\]\\n')  
                for key, value in values.items():

                    configfile.write(f'{key} \= {value}\\n')

        CTkMessagebox(title="Success\!", message='Successfully Saved Configurations', icon="check", option\_1='okay')

        print(f"Configuration saved to {file\_path}")

def save(cam1\_path, cam2\_path, cam3\_path, cam4\_path, mask1\_path, mask2\_path, mask3\_path, parking\_name1, parking\_name2, parking\_name3):  
    global video\_pathA, video\_pathB, video\_pathC, video\_pathD  
    global maskA, maskB, maskC  
    global parking\_lot\_1, parking\_lot\_2, parking\_lot\_3

    video\_pathA \= str(cam1\_path.get())  
    video\_pathB \= str(cam2\_path.get())  
    video\_pathC \= str(cam3\_path.get())  
    video\_pathD \= str(cam4\_path.get())

    maskA \= str(mask1\_path.get())  
    maskB \= str(mask2\_path.get())  
    maskC \= str(mask3\_path.get())

    parking\_lot\_1 \= str(parking\_name1.get())  
    parking\_lot\_2 \= str(parking\_name2.get())  
    parking\_lot\_3 \= str(parking\_name3.get())

    \# Print the values for checking  
    print("Video Paths:", video\_pathA, video\_pathB, video\_pathC, video\_pathD)  
    print("Mask Paths:", maskA, maskB, maskC)  
    print("Parking Lot Names:", parking\_lot\_1, parking\_lot\_2, parking\_lot\_3)

    CTkMessagebox(title="Info", message='New settings saved\!\\n But it wont save if you restart', option\_1='OK')

def open\_directory(cam\_entry):

    directory \= filedialog.askopenfilename()  
    cam\_entry.delete(0, 'end')  
    cam\_entry.insert(0, directory)

def open\_setting():  
    window \= CTkToplevel(app)  
    window.title('Admin Panel')  
    window.geometry('500x900')  
    window.resizable(False,False)  
    window.wm\_attributes('-topmost', True)

    \#widgets  
    setting \= CTkLabel(window, text="Settings")

    cam\_setting \= CTkLabel(window, text="Camera")

    parking \= CTkLabel(window, text="Parking Lot")  
    save\_button \= CTkButton(window, text='Save', command=lambda: save(  
        cam1\_path\_entry, cam2\_path\_entry, cam3\_path\_entry, cam4\_path\_entry,  
        mask1\_path\_entry, mask2\_path\_entry, mask3\_path\_entry,  
        parking\_section\_name1, parking\_section\_name2, parking\_section\_name3  
    ))  
    save\_conf\_button \= CTkButton(window, text='Save Configuration', command=save\_configuration)

    vid\_source\_text1 \= CTkLabel(window, text="Video Source:")  
    vid\_source\_text2 \= CTkLabel(window, text="Video Source:")

    vid\_source\_text3 \= CTkLabel(window, text="Video Source:")  
    vid\_source\_text4 \= CTkLabel(window, text="Video Source:")

    mask\_text1 \= CTkLabel(window, text="Mask:")  
    mask\_text2 \= CTkLabel(window, text="Mask:")  
    mask\_text3 \= CTkLabel(window, text="Mask:")

    parking\_lot\_text1 \= CTkLabel(window, text="Parking Lot 1:")  
    parking\_lot\_text2 \= CTkLabel(window, text="Parking Lot 2:")

    parking\_lot\_text3 \= CTkLabel(window, text="Parking Lot 3:")

    \#vidsource path entry  
    cam1\_path\_entry \= CTkEntry(window, width=350, placeholder\_text="Camera 1 path or number")

    directory1 \= CTkButton(window, width=30, text='...',command=lambda: open\_directory(cam1\_path\_entry))

    cam2\_path\_entry \= CTkEntry(window,width=350, placeholder\_text="Camera 2 path or number")

    directory2 \= CTkButton(window, width=30, text='...', command=lambda: open\_directory(cam2\_path\_entry))

     
 cam3\_path\_entry \= CTkEntry(window,width=350, placeholder\_text="Camera 3 path or number")  
    directory3 \= CTkButton(window,  width=30, text='...', command=lambda: open\_directory(cam3\_path\_entry))

    cam4\_path\_entry \= CTkEntry(window,width=350, placeholder\_text="Camera 4 path or number")  
    directory4 \= CTkButton(window, width=30, text='...', command=lambda: open\_directory(cam4\_path\_entry))

    \#mask source path  
    mask1\_path\_entry \= CTkEntry(window, width=395, placeholder\_text="Mask path cam 1")

    directory5 \= CTkButton(window, width=30, text='...',command=lambda: open\_directory(mask1\_path\_entry))

    mask2\_path\_entry \= CTkEntry(window,width=395, placeholder\_text="Mask path cam 1")  
    directory6 \= CTkButton(window, width=30, text='...', command=lambda: open\_directory(mask2\_path\_entry))

    mask3\_path\_entry \= CTkEntry(window,width=395, placeholder\_text="Mask path cam 1")  
    directory7 \= CTkButton(window,  width=30, text='...', command=lambda: open\_directory(mask3\_path\_entry))

 

   \#Parking Lot segment/section naming entry

    parking\_section\_name1 \= CTkEntry(window,width=250, placeholder\_text="Parking Lot section/segment name")  
    parking\_section\_name2 \= CTkEntry(window,width=250, placeholder\_text="Parking Lot section/segment name")  
    

parking\_section\_name3 \= CTkEntry(window,width=250, placeholder\_text="Parking Lot section/segment name")

    \#initialize widgets  
    setting.pack()

    cam\_setting.place(x=10, y=50)  
    cam1\_path\_entry.place(x=95, y=80)  
    cam2\_path\_entry.place(x=95, y=120)  
    cam3\_path\_entry.place(x=95, y=160)  
    cam4\_path\_entry.place(x=95, y=200)

    vid\_source\_text1.place(x=10, y=80)  
    vid\_source\_text2.place(x=10, y=120)  
    vid\_source\_text3.place(x=10, y=160)  
    vid\_source\_text4.place(x=10, y=200)

    directory1.place(x=450, y=80)  
    directory2.place(x=450, y=120)  
    directory3.place(x=450, y=160)  
    directory4.place(x=450, y=200)

    mask\_text1.place(x=10, y=250)  
    mask\_text2.place(x=10, y=290)  
    mask\_text3.place(x=10, y=330)

    mask1\_path\_entry.place(x=50, y=250)

    mask2\_path\_entry.place(x=50, y=290)  
    mask3\_path\_entry.place(x=50, y=330)

    directory5.place(x=450, y=250)  
    directory6.place(x=450, y=290)  
    directory7.place(x=450, y=330)

    parking.place(x=10, y=420)

    parking\_lot\_text1.place(x=10, y=460)  
    parking\_lot\_text2.place(x=10, y=500)  
    parking\_lot\_text3.place(x=10, y=540)

    parking\_section\_name1.place(x=90, y=460)

    parking\_section\_name2.place(x=90, y=500)

    parking\_section\_name3.place(x=90, y=540)

    save\_button.place(x=185,y=700)  
    save\_conf\_button.place(x=185, y=750)  
def capture\_label\_content(widget, ss\_spot, count=\[0\]):  
    x, y, width, height \= widget.winfo\_rootx(), widget.winfo\_rooty(), widget.winfo\_width(), widget.winfo\_height()  
    image \= ImageGrab.grab(bbox=(x, y, x \+ width, y \+ height))

    save\_path \= r'D:\\screen capture'  
    os.makedirs(save\_path, exist\_ok=True)

    filename \= f"label\_content\_{count\[0\]:04d}.png"

    count\[0\] \+= 1

    image.save(os.path.join(save\_path, filename))  
    print(f"Content of {widget.cget('text')} captured and saved at {save\_path}/{filename}\!")  
    CTkMessagebox(title="Info", message='Screen Capture {}'.format(ss\_spot))  
def run\_segment():  
    \# Replace with the absolute path to your virtual environment's activate script  
    venv\_activate\_script \= r"C:\\Users\\DICT\\Desktop\\SPMS\\venv\\Scripts\\activate.bat"

    \# Replace with the absolute path to your Python script  
    script\_to\_run \= r"C:\\Users\\DICT\\Desktop\\SPMS\\image\_segmentor\_two.py"

    \# Construct the command to activate the virtual environment and run the script  
    command \= f'call "{venv\_activate\_script}" && python "{script\_to\_run}"'

    \# Run the command  
    subprocess.call(command, shell=True)

\#continuously access and display available spot  
def access\_spots\_status(avail\_spot\_label,proceed\_to\_label):  
    spot\_A\_len \= 0

    spot\_A\_ava \= 0

    spot\_B\_len \= 0

   

 spot\_B\_ava \= 0

    spot\_C\_len \= 0  
    spot\_C\_ava \= 0

    spot\_display\_A \= ""  
    spot\_display\_B \= ""  
    spot\_display\_C \= ""

    while True:  
        user\_class \= data\_q\_class.get()  
        user\_has\_class \= data\_q\_has\_class.get()  
        f\_spot \= data\_queue\_spot.get()  
        print(f\_spot)

        print(user\_class)  
        print(user\_has\_class)

        spots\_status \= data\_queue.get()

        \#total spot  
        spots\_status\_len \= len(spots\_status)

        \#available spot  
        spots\_status\_sum \= sum(spots\_status)

        if spots\_status\_len \== 69:  
            spot\_A\_len \= spots\_status\_len  
            spot\_A\_ava \= spots\_status\_sum  
        elif spots\_status\_len \== 76:  
            spot\_B\_len \= spots\_status\_len  
            spot\_B\_ava \= spots\_status\_sum  
        elif spots\_status\_len \== 72:  
            spot\_C\_len \= spots\_status\_len  
            spot\_C\_ava \= spots\_status\_sum

   

     total\_avail \= spot\_A\_ava \+ spot\_B\_ava \+ spot\_C\_ava  
        total\_spot \= spot\_A\_len \+ spot\_B\_len \+ spot\_C\_len

        if f\_spot\[0\] \== "A":  
            spot\_display\_A \= f\_spot  
        elif f\_spot\[0\] \== "B":

            spot\_display\_B \= f\_spot  
        elif f\_spot\[0\] \== "C":  
            spot\_display\_C \= f\_spot

        if user\_class \== 'teaching' and user\_has\_class \== True:  
            spot\_to\_proceed \= spot\_display\_A  
            proceed \= 'PROCEED TO:'  
        elif user\_class \== 'non\_teaching' and user\_has\_class \== True:  
            spot\_to\_proceed \= spot\_display\_B

            proceed \= 'PROCEED TO:'  
        elif user\_class \== 'staff' and user\_has\_class \== True:  
            spot\_to\_proceed \= spot\_display\_C  
            proceed \= 'PROCEED TO:'  
        else:

            spot\_to\_proceed \= '' \#spot\_display\_A  
            proceed \= ''

        avail\_spot\_label.config(  
            text="{}\\n Available: {}/{}\\n\\n{}\\n Available: {}/{}\\n\\n{}\\n Available:{}/{}\\n\\n total:{}/{}".format(  
                parking\_lot\_1, spot\_A\_ava, spot\_A\_len,

                parking\_lot\_2, spot\_B\_ava, spot\_B\_len,

                parking\_lot\_3, spot\_C\_ava, spot\_C\_len,  
                total\_avail, total\_spot  
            )  
        )

        proceed\_to\_label.config(text='{} {}'.format(proceed,spot\_to\_proceed))

\#GUI  
app \= CTk()

\#getting screen width and height of display  
width \= app.winfo\_screenwidth()  
height \= app.winfo\_screenheight()

\#setting tkinter window size  
app.geometry("%dx%d" % (width, height))

app.title("Video Stream")

screen\_cap\_icon \= CTkImage(dark\_image=Image.open(r"D:\\white\_icon\_1.png"), size=(25,25))

setting\_icon \= CTkImage(dark\_image=Image.open(r"D:\\white\_user.png"), size=(30,30))

\#Widgets

settings\_button \= CTkButton(app,text='', image=setting\_icon, command=open\_setting, width=25)  
buttonA \= CTkButton(app, image=screen\_cap\_icon, text='', width=25, 

font=("Helvetica", 24), command=lambda: capture\_label\_content(label0,"A"))  
buttonB \= CTkButton(app, image=screen\_cap\_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture\_label\_content(label1,"B"))

buttonC \= CTkButton(app, image=screen\_cap\_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture\_label\_content(label2,"C"))  
buttonD \= CTkButton(app, image=screen\_cap\_icon, text='', width=25, font=("Helvetica", 24), command=lambda: capture\_label\_content(label3,"D"))

label0 \= Label(app, text="video 1", anchor='center')  
label1 \= Label(app, text="Video 2", background="red", anchor='center')  
label2 \= Label(app, text="Video 3", background="blue")  
label3 \= Label(app, text="Video 4", background="yellow")  
label4 \= Label(app, font=("CrashNumberingGothic", 20),fg='white')  
label5 \= Label(app, font=("LED BOARD REVERSED", 20, "bold"),fg='yellow', background="black")

label6 \= Label(app, text="Label 6", background="white")

\#define grid

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

\#place a widget  
settings\_button.grid(row=0, column=5)

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
label4.grid(row=1, column=4, sticky='nsew', padx=10, pady=10)  
label5.grid(row=2, column=4, sticky='ew')

\#Configuration  
label0.config(width=100, height=100)  
label1.config(width=100, height=100)  
label2.config(width=100, height=100)  
label3.config(width=100, height=100)  
label4.config(width=5, height=5, relief=RAISED, borderwidth=2, background="\#2b2b2b")  
label5.config(width=5, height=5, relief=RAISED, borderwidth=3)

\#tip message  
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

\#Menu bar cofigurations

menubar \= Menu(app, background='blue', fg='white')  
option\_menu \= Menu(menubar, tearoff=0)

menubar.add\_cascade(label="Option", menu=option\_menu)  
option\_menu.add\_command(label="Segment", command=run\_segment)  
app.config(menu=menubar)

\#access spots\_status value  
access\_thread \= threading.Thread(target=access\_spots\_status, args=(label4,label5))

\#Run access thread  
access\_thread.start()

\#Main threads  
segment\_A\_thread \= threading.Thread(target=segment\_vid, args=(maskA, video\_pathA, label0, frame\_w, frame\_h, data\_queue, data\_queue\_spot , "A"))

segment\_B\_thread \= threading.Thread(target=segment\_vid, args=(maskB, video\_pathB, label1, frame\_w, frame\_h, data\_queue, data\_queue\_spot , "B"))  
segment\_C\_thread \= threading.Thread(target=segment\_vid, args=(maskC, video\_pathC, label2, frame\_w, frame\_h, data\_queue, data\_queue\_spot , "C"))  
segment\_D\_thread \= threading.Thread(target=obj\_classifier, args=(label3, user\_classif\_model, yolo\_pretrained\_model, video\_pathD, 

frame\_w, frame\_h, data\_q\_class, data\_q\_has\_class))

\#start threads  
segment\_A\_thread.start()  
segment\_B\_thread.start()  
segment\_C\_thread.start()

segment\_D\_thread.start()

app.mainloop()  
cv2.destroyAllWindows()

**Segment.py**  
from tkinter import \*  
import cv2  
from PIL import Image, ImageTk  
from util import get\_parking\_spots\_bboxes, empty\_or\_not

def segment\_vid(mask, video\_path,label,frame\_w,frame\_h,data\_queue,data\_queue\_spot,lot\_segment):

    mask \= cv2.imread(mask, 0\)  
    cap \= cv2.VideoCapture(video\_path)

    if cap.isOpened() \== True:

        connected\_components \= cv2.connectedComponentsWithStats(mask, 4, cv2.CV\_32S)  
        spots \= get\_parking\_spots\_bboxes(connected\_components)

   

     \# Initialize the list to store spot status  
        spots\_status \= \[None for j in spots\]

        frame\_nmr \= 0  
        ret \= True  
        step \= 30

        while ret:  
            ret, frame \= cap.read()

            if frame\_nmr % step \== 0:

                for spot\_indx, spot in enumerate(spots):  
                    x1, y1, w, h \= spot  
                    spot\_crop \= frame\[y1:y1 \+ h, x1:x1 \+ w, :\]  
                    spot\_status \= empty\_or\_not(spot\_crop)  
                    spots\_status\[spot\_indx\] \= spot\_status

                    \# Display spot index on the frame  
                    cv2.putText(frame, str(spot\_indx \+ 1), (x1 \+ w // 2, y1 \+ h // 2), cv2.FONT\_HERSHEY\_SIMPLEX, 0.5,

                                (255, 255, 255), 2\)

            \# Rest of the code for visualization and updating the frame  
            for spot\_indx, spot in enumerate(spots):

                spot\_status \= spots\_status\[spot\_indx\]  
                x1, y1, w, h \= spots\[spot\_indx\]

                  
\# Draw rectangles based on spot status  
                if spot\_status:  
                    frame \= cv2.rectangle(frame, (x1, y1), (x1 \+ w, y1 \+ h), (0, 255, 0), 2\)  
                else:

                    frame \= cv2.rectangle(frame, (x1, y1), (x1 \+ w, y1 \+ h), (0, 0, 255), 2\)

            \# Generate and print empty spot indices after processing the frame

            empty\_spots\_indices \= \[f"{lot\_segment}{index \+ 1}" for index, status in enumerate(spots\_status) if status\]  
            if empty\_spots\_indices:  
                f\_element \= (empty\_spots\_indices\[0\])

            else:  
            

    f\_element \= None

            \# Visualization of the frame  
            frame\_resized \= cv2.resize(frame, (frame\_w, frame\_h))  
            frame\_rgb \= cv2.cvtColor(frame\_resized, cv2.COLOR\_BGR2RGB)  
            image \= Image.fromarray(frame\_rgb)  
            image\_tk \= ImageTk.PhotoImage(image)

            label.config(image=image\_tk)

            label.image \= image\_tk

            \# Send the current spots\_status to the main thread

      

      data\_queue.put(spots\_status)  
            data\_queue\_spot.put(f\_element)

    else:  
        img \= Image.open(r'C:\\Users\\DICT\\Desktop\\SPMS\\Images\\no\_video.png')  \# Replace with the path to your image  
        image\_resize \= img.resize((frame\_w, frame\_h))

        image\_tk \= ImageTk.PhotoImage(image\_resize)

        label.config(image=image\_tk)  
        label.image \= image\_tk

**image\_segmentor\_two.py**  
import tkinter as tk  
from tkinter import messagebox  
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageTk  
import customtkinter as ctk

class ImagePointDrawer:  
    def \_\_init\_\_(self, root):

        self.root \= root  
        self.canvas \= ctk.CTkCanvas(root)  
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)  \# Set weight of column 0 to 1  
        self.root.rowconfigure(0, weight=3)     \# Set weight of row 0 to 3

      

  self.shapes \= \[\]  
  self.current\_shape \= \[\]  
        self.is\_drawing \= False  
        self.image \= None

        self.create\_menu()

        self.draw\_button \= ctk.CTkButton(root, text="Draw Points", command=self.toggle\_drawing)  
        self.draw\_button.grid(row=1, column=0, pady=10)  \# Button in row 1, column 0, sticky to all sides

        self.save\_button \= ctk.CTkButton(root, text="Save", command=self.save\_images)

        self.save\_button.grid(row=2, column=0, pady=10)  \# Button in row 2, column 0, sticky to all sides

        self.canvas.bind("\<Button-1\>", self.on\_canvas\_click)

    def create\_menu(self):  
        menubar \= tk.Menu(self.root)  
        file\_menu \= tk.Menu(menubar, tearoff=0)  
        file\_menu.add\_command(label="Open Image", command=self.open\_image)  
        menubar.add\_cascade(label="File", menu=file\_menu)  
        self.root.configure(menu=menubar)

 

   def open\_image(self):  
        file\_path \= filedialog.askopenfilename(  
            filetypes=\[("Image files", "\*.png \*.jpg \*.jpeg \*.gif \*.bmp \*.ppm \*.pgm \*.pbm \*.xbm")\])  
        if file\_path:  
            self.load\_image(file\_path)

    def load\_image(self, image\_path):

        self.image \= Image.open(image\_path)  
        self.ctk\_image \= ImageTk.PhotoImage(self.image)  
        self.canvas.configure(width=self.image.width, height=self.image.height)  
        self.canvas.create\_image(0, 0, image=self.ctk\_image, anchor=tk.NW)

    def toggle\_drawing(self):  
        if self.is\_drawing:  
            if self.current\_shape:  
                self.close\_current\_shape()  
        else:  
            self.start\_new\_shape()

    def start\_new\_shape(self):  
        self.current\_shape \= \[\]  
        self.is\_drawing \= True  
        self.draw\_button.configure(text="Stop Drawing")  
        self.canvas.configure(cursor="plus")

    def on\_canvas\_click(self, event):  
        if not self.is\_drawing:  
            return

        x, y \= event.x, event.y  
        self.current\_shape.append((x, y))

        self.canvas.create\_oval(x \- 2, y \- 2, x \+ 2, y \+ 2, fill="red")

        if len(self.current\_shape) \> 1:  
            self.canvas.create\_line(self.current\_shape\[-2\], self.current\_shape\[-1\], fill="blue")

        if len(self.current\_shape) \> 2:  
            if self.is\_close\_to\_start(x, y):  
                self.prompt\_save\_shape()

    def is\_close\_to\_start(self, x, y):  
        if self.current\_shape:  
            start\_x, start\_y \= self.current\_shape\[0\]  
            return abs(x \- start\_x) \< 5 and abs(y \- start\_y) \< 5  
        return False

    def close\_current\_shape(self):  
        if self.current\_shape:

            self.shapes.append(self.current\_shape)  
            self.current\_shape \= \[\]  
            self.is\_drawing \= True  
           self.draw\_button.configure(text="Stop Drawing")  
            self.canvas.configure(cursor="plus")

    def prompt\_save\_shape(self):  
        result \= messagebox.askyesno("Save Shape?", "Do you want to save and close the shape?")  
        if result:  
            self.close\_current\_shape()

    def clear\_canvas(self):  
        self.canvas.delete("all")  
        self.shapes \= \[\]  
        self.current\_shape \= \[\]  
        self.is\_drawing \= False  
        self.draw\_button.configure(text="Draw Points")  
        self.canvas.configure(cursor="arrow")

    def save\_images(self):  
        save\_path \= filedialog.asksaveasfilename(defaultextension=".png", filetypes=\[("PNG files", "\*.png")\])  
        if not save\_path:  
            return  \# User canceled the file dialog

        self.save\_canvas\_image(save\_path)  
        self.save\_filled\_shape\_image(save\_path)

    def save\_canvas\_image(self, save\_path):  
        if self.image:  
            image \= self.image.copy()  
            draw \= ImageDraw.Draw(image)

            for shape in self.shapes:

              

  draw.polygon(shape, outline="black", fill="white")

            image.save(save\_path)

    def save\_filled\_shape\_image(self, save\_path):  
        if self.image:  
            image \= Image.new("L", (self.image.width, self.image.height), 0\)  \# Black background  
            draw \= ImageDraw.Draw(image)

            for shape in self.shapes:  
                draw.polygon(shape, outline="white", fill="white")

            image.save(save\_path)

root \= ctk.CTk()

app \= ImagePointDrawer(root)  
root.mainloop()  
**Util.py**  
import pickle

from skimage.transform import resize  
import numpy as np  
import cv2

EMPTY \= True  
NOT\_EMPTY \= False

MODEL \= pickle.load(open("C:/Users\\DICT\\Desktop\\SPMS\\model\\model.p", "rb"))

def empty\_or\_not(spot\_bgr):

    flat\_data \= \[\]

    
  img\_resized \= resize(spot\_bgr, (15, 15, 3))

    flat\_data.append(img\_resized.flatten())  
    flat\_data \= np.array(flat\_data)

    y\_output \= MODEL.predict(flat\_data)

    if y\_output \== 0:  
        return EMPTY  
    else:  
        return NOT\_EMPTY

def get\_parking\_spots\_bboxes(connected\_components):  
    (totalLabels, label\_ids, values, centroid) \= connected\_components

    slots \= \[\]  
    coef \= 1  
    for i in range(1, totalLabels):

       \# Now extract the coordinate points  
        x1 \= int(values\[i, cv2.CC\_STAT\_LEFT\] \* coef)  
        y1 \= int(values\[i, cv2.CC\_STAT\_TOP\] \* coef)

        w \= int(values\[i, cv2.CC\_STAT\_WIDTH\] \* coef)  
        h \= int(values\[i, cv2.CC\_STAT\_HEIGHT\] \* coef)

        slots.append(\[x1, y1, w, h\])

    return slots

**Three\_obj\_classifv2.py**

import cv2  
from ultralytics import YOLO  
import numpy as np  
from PIL import Image, ImageTk

def obj\_classifier(ui\_label, obj\_mdl\_path, veh\_mdl\_path, vid\_path, frame\_w, frame\_h, data\_q\_class, data\_q\_has\_class):  
    \# YOLO model for general object detection  
    yolo\_objects \= YOLO(obj\_mdl\_path)

    \# YOLO model for car and motorcycle detection

    yolo\_vehicles \= YOLO(veh\_mdl\_path, "v8")

    \# Open the video file  
    cap \= cv2.VideoCapture(vid\_path)

    \# Define the ROI for vehicle detection  
    roi\_points \= np.array(\[\[(0, 175), (1270, 175), (1270, 816), (0, 816)\]\], dtype=np.int32)

    user\_vehicle\_classification \= None  \# Initialize the variable

    if cap.isOpened():  
        while cap.isOpened():  
            \# Read the video frame by frame  
            ret, frame \= cap.read()  
            if ret:  
                \# Draw the ROI for vehicle detection on the frame  
                cv2.polylines(frame, \[roi\_points\], isClosed=True, color=(0, 0, 255), thickness=2)

                \# Apply the YOLO model for car and motorcycle detection to the frame  
                results\_vehicles \= yolo\_vehicles.predict(source=frame)

                \# Flags to keep track of vehicle and object classification

                car\_detected \= False  
                staff\_detected \= False  
                teaching\_detected \= False  
                non\_teaching\_detected \= False  
                car\_has\_class \= False

                \# Check if a car is Inside ROI  
                for result\_vehicle in results\_vehicles:  
                    for i in range(len(result\_vehicle.boxes.xyxy)):  
                        x, y \= int(result\_vehicle.boxes.xyxy\[i\]\[0\]), int(result\_vehicle.boxes.xyxy\[i\]\[1\])  
                        if cv2.pointPolygonTest(roi\_points, (x, y), False) \>= 0:  
                            \# Car is inside the ROI, proceed with drawing and classification  
                            class\_name\_vehicle \= yolo\_vehicles.names\[int(result\_vehicle.boxes.cls\[i\])\]

                            \# Filter only desired classes (e.g., "car" and "motorcycle")  
                            if class\_name\_vehicle in \["car"\]:  
                                car\_detected \= True

                                \# Draw bounding box for the car  
                                x1, y1, x2, y2 \= map(int, result\_vehicle.boxes.xyxy\[i\])  
                                label \= f'{class\_name\_vehicle}: {result\_vehicle.boxes.conf\[i\]:.2f}'  
                                frame \= cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2\)

                                frame \= cv2.putText(frame, label, (x1, y1 \- 10), 

cv2.FONT\_HERSHEY\_SIMPLEX, 0.9, (255, 0, 0), 2\)

                                \# Extract sub-region within car bounding box  
                                sub\_roi \= frame\[y1:y2, x1:x2\]

                                \# Apply the YOLO model for staff, teaching, non\_teaching to the sub-region  
                                results\_objects \= yolo\_objects.predict(source=sub\_roi)

                                \# Check if objects are inside sub-ROI  
                                for result\_obj in results\_objects:  
                                    for j in range(len(result\_obj.boxes.xyxy)):  
    

                                    x\_obj, y\_obj \= 

int(result\_obj.boxes.xyxy\[j\]\[0\]), int(result\_obj.boxes.xyxy\[j\]\[1\])

                                        \# Convert object coordinates to global frame  
                                        x\_obj\_global, y\_obj\_global \= x\_obj \+ x1, y\_obj \+ y1

                                        if cv2.pointPolygonTest(roi\_points, (x\_obj\_global, y\_obj\_global), False) \>= 0:  
                                            \# Object is inside the ROI, proceed with drawing and classification  
                                            \# Draw bounding box  
                                            x1\_obj, y1\_obj, x2\_obj, y2\_obj \= map(int, result\_obj.boxes.xyxy\[j\])

                                       
       label\_obj \= f'{yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\]}: {result\_obj.boxes.conf\[j\]:.2f}'  
                                            frame \= cv2.rectangle(frame, (x1\_obj \+ x1, y1\_obj \+ y1), (x2\_obj \+ x1, y2\_obj \+ y1),  
                                                                  (255, 0, 0), 2\)  
                                            frame \= cv2.putText(frame, label\_obj, (x1\_obj \+ x1, y1\_obj \+ y1 \- 10),  
                                                                cv2.FONT\_HERSHEY\_SIMPLEX, 0.9, (255, 0, 0), 2\)

                                            \# Check for object classifications  
                                            if yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'staff':  
                                                staff\_detected \= True  
                    

                            car\_has\_class \= True  
                                            elif yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'teaching':  
                                                teaching\_detected \= True  
                                                car\_has\_class \= True  
                                            elif yolo\_objects.names\[int(result\_obj.boxes.cls\[j\])\] \== 'non\_teaching':  
                                                non\_teaching\_detected \= True  
                                                car\_has\_class \= True

                \#print(str(car\_has\_class))  
                \# Determine the user\_vehicle\_classification  
                if car\_detected:  
                    if staff\_detected:  
                    

    user\_vehicle\_classification \= 'staff'  
                    elif teaching\_detected:  
                        user\_vehicle\_classification \= 'teaching'  
                    elif non\_teaching\_detected:  
                        user\_vehicle\_classification \= 'non\_teaching'  
                    else:  
                        user\_vehicle\_classification \= None  
                frame\_resized \= cv2.resize(frame, (frame\_w, frame\_h))  
                frame\_rgb \= cv2.cvtColor(frame\_resized, cv2.COLOR\_BGR2RGB)  
                image \= Image.fromarray(frame\_rgb)  
                image\_tk \= ImageTk.PhotoImage(image)    
   ui\_label.config(image=image\_tk)  
                ui\_label.image \= image\_tk

                data\_q\_has\_class.put(car\_has\_class)             data\_q\_class.put(user\_vehicle\_classification)  
    else:  
        img \= Image.open(r'C:\\Users\\DICT\\Desktop\\SPMS\\Images\\no\_video.png')  \# Replace with the path to your image  
        image\_resize \= img.resize((frame\_w, frame\_h))  
 image\_tk \= ImageTk.PhotoImage(image\_resize)

   

     ui\_label.config(image=image\_tk)  
        ui\_label.image \= image\_tk

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHsAAACQCAYAAAAoRBQ+AAAnjklEQVR4Xu1dB3gUx9l2nMTJH3dMU++9IITK6dR7770gCRXUG0UUCWQ62GDAphuwA6aDC90t7iVuSezYsWPHNe4Yd3DD7//NSnNazeqkO+lOSETv87zP7c5O2Z33Zuab3SmXXTaKUYxiFKMYxcXFCy+88PvYObnWfhVxWS6FIccuU4376DL1BAyKFIdTQdAJ96KQ6NDaZPuTJ0/+QUx3FEaEqjxmjHN+0EmFMBeJ6XOnLXHMnzJWvM9RDAC/DTJ9jTL1VzGThy0DJvx6RYjpP8XnGIWA5Xesibsi2PyMIgP1ZGRjFvY+cDfe/+S/OPvNV/jll1+gL879cB5nv/4Sb3/4HprWtSvS0Ie/CzZ7V3zW/ym4FQWrLwsYq7Ow18U4Im9BFX786SdRl2GDtDkluCbaXnHvvVI17sPxiR62Yr5cMqi5eaav4qG18E/h1mJe6oSff/4J585/hxdeeQJb969Cao23gjsOrdH4b187XXGds3BmGO68ez2+/f5r+pP9IEtFN7z/yQe6ia8a+9mEaM8rxfwacejo6Lj8soDxFxQP2AtZ1akr3nz3n6hoS0RmvZ9CpP6oq9j9MbsxAC+9+ozsrrTjwq+/4smXn1M8s8gJ8W4Pink4bLHq3u1Xk7gfiw8hp1WGD9764B0xPxTYe2yzIoMNQUOJ3R+ffPEhXLjQt72weu8mRf7IGVybXC/m8UWHT2n0ZvFG5bwq0hZvvPeW+Kw9cNd9GxUZZgwOldgiP/viY9nTKqGqTFDkm4aqcV+KeT7ksErzflBxYzLOuLVDfCYNfqWqTcyQoeDFElvON95+WZYTPfHcqy8p8lHOjjs6/ijqYFR4FIXuEG9CTiZkbzj/4znkzwhRPPxQcjiILef3576V5VBPiPnKebl6wg+iJoZFH68gv/ruG/E+Jfz404+Kh7vYHG5ii/z87CeyHOyGY26AIt81NBTyFlaWKCJXs5cFpuL9aDBzZbHiIYYLh7vYnDULU2U52o01+zYrtODMamn5P1E/3dFLhIyfnj0j3oOEjDpfxU0PN44UsTnzm4NlOdyNqyJtFLowjolzelyUUSv+GGb1thgBY294/6O3FTc33DnSxJZzensSdecuyBTohKgVp0dh6EpR3270EmDXqYNi3Dj/w/eKGxkpfPLFBzTPkVY7RXF9JHDfia0yNbpxeeBEhX6XqW/4hyhzJ2SeLg8yEePCN999qUh4pPFSEJtzwbpqmTqdMEmepJ/Yvb26FBMaqbyUxObsravLDGidxOaoWpiiiHik05hiZ9cHYMWcpB5uhZVBqJ8To/BrLHIUL67XT2wxokuBxhSbMaPOD4/taMTfji7DzttqkFrtjcn2ZkhR2aOtPBjNLXGKMIYkx7AU+7+fvIuHnzmmU3pvf/A6CmaEKtz1obHFZkyc5g2videiOsoJp25OJMEnI0LlALXDBEn8XcsLFWEMRY4hF7vj1jqFmzbqAzGsPhwKseWMshmL/XMDsaYxEEnRHtg2IxBNNVOQ7mKC22erUTIjShFmMOQYcrH1iUMfiGH14VCLnUrC5nuZ4+CcIJSXeKHY2xJ3tqhQXhGKhlgnyU9N0+BqKzk5hlzsV998SeGmjRwHT21H09I8zTlHbUe65oWCGFYfDoXYdeWhUnXNzzM9TFEV7oB7FkSgLtARzQnOmJbogRZ/S+SlOGJ2QQCyqiYr4hkIOYZU7BdffUrhVtGWoDVehgeeurfHuRxy9wXrqhThdeVQiM2YWRWA/e1pKKoPlM5zJltgS40/VlHpnhlkjeZwO9xO1ntDuD2Sp3uhPsRF8ldSFqyISx9yDKnYF3690OP8jsNrceLRA9LxOx+8ofAvpidHZXtndyanSa1xE8PryqESmzHM3wlJVKr3zo1DWV0EKtQ2OLk4BJuLvVFLxzVxTphFVfnUUBtsKo1AXIQtZlTHK+LRhxxDKva2AzdpjlfvmId1dy7EO//9t3TeW/zi+WPPnZR+H3jyHoU/0a8+HEqxOVNcTbGrUYXiABvcO8sfG+oCUeJvgwIfK8xNcEVzrDNuq4xFrusEyf+y4oHfF8eQif2grDqetapYE9eXX5+RfvkbH3kYhsefv7/HOfttWpqr8CeG1YcXQ+ycbDWyJlmgJsoRJ9uCsCTXAyupezYn0hH1YY5YlOaONUWTMT3IFinUTZudMAkJpZ6KeHQhx5CJ/fW33e/QGRauq5aOz/9wTnqfK/rn/qoXpmrOF29oUPjh/hiWbGxWXNOFxhY7vdanx3nN/AR4mlyHoBhnZPlYI4VEX5PpidNLY9GgtkV1qD1a41xwqD0MzRGOKEudgs25k+Blc4Mibl3IMWRi1y/K0hx/cuZD6ffVN/+Gl994Hj/93D16RZ4Gw6dnPlLEJVIO8ZouNLTY6dXdcdy4fCqmBFtrzv+8fT5KIztL6HNH1iNysg3yplijNdwJ91JXbFaYA2rDHdER74xjHSGoDLRHlp8NtpV6wWPCtdixqlKRXn/kGDKx5Tx0agemzoqQjt//6D+ootL7/sed38HlaXD09YZMhHhdFxpabM47t8yDvXVnaSxqCcUjd7Qh3H48TG+4GquXTUO8lyXuvTEGUdR+NwXbY1OJD+aTJd4U744lic54cEk4KoPssaXBDwuzPeBnci1OrJ2G5PJJirT6IseQiN1bOO627/hW/OWZY9JxVoMKh++/o4cfOcTwvaGkNVqRVn80hthP7l0Je4sxyK73x5O7FiPScQLiPM2xrtAXJWpHyUDLpOp7arAdlqe4SsdzIp1QFWiD5kR3tEY44/j8ENSFOuL+m+KRTtfdxl2DB3bMRNEkU0V6fZFjSMT+5cIvCrenX3oIH332vuY8tzlIGlUp9yOCTblh7g2Ls8VLGrz06tOKtPqjocReW5uKHPrDnt5UjUxPM9y6ug6756YgydkUtxZ5oTXRFWnuZpiV4Iz1hVPQQILGu5hIQpZTW10WaIepvjaoI9Fbwh1welEYVeHWOLIwEtm+1nAfdzUe21SOWIdxirT7IofRxa4nYVbdPkfhznjmy09x74O7pePvvv8Gn5/9tMf13tC4JEfqr/cFMZ3+aAixD6ysQ1KFF/bMT0SqmynSqORupu5UKgldT8ZWoocZsrwtsb1ChVQPc8Q6TYDH2KthfdWVCKVSf6hRjbTJlsjzssK0IDtke1thFRllu+tVSKY/QxoZcon+FrhvUQSSXSYq0u+LHEYXu78wfIy06M7DHji5XfrVNoGgN4h++uNgxX6IegHeZtfhmX03IsaJhHA1wbY6NVKp1O6uUaM+2hGNEQ6YprJFvJsZklxI+JruOWlNdck4Oi8Uh1pDkeRpiewpVliU7oUCbwscawtFqdoOTWSh31gwBZXRLohzGKu4h77IYXSxv/jqM4WbrmR49K8nNWlzLN3U3cViONj1h+AQ4+mPn5/tnoaTVqO72NvaKnHfimLpo8au2ZE4OC8MhZPMsWXaFGRSSd40dbLUFteTdR1LJX1WgjtZ17aYbHkDzP/0J1hefSWcyVibNPE63Fbqi9MrE6kL5o4UDwvcmOKOVApbTCW6mqr3xfmeOHFjFDKpWi9RWWPLbS2K+9FGDqOLzaa5im66kmPuzWWaYxFsGq4IMZ7+OBCxC5qCEOJwA5qSXVFE1fLBeSGI8zBFdZQjVbuW1PZaQe04EQV+VvC3N0GQzVhMvP4qxBV7KOJinJk0CaeWxuCetkhEU+mPpT9LW7I7yqmtzqE4ji2IQH6ALSqoa1YV7YR97Z29GV3IYVSxp9K/XXTTh3Kw/jbH0y89LP2yPnpvEOPpjwMRe0V5EjKqfZBPQmRRad5Y7oMsEmhGvCtinCdiJrXTviRyKYnTQOLYjbtWEYecmX4O2FkXgOPUFUulfneMqxn9WiGd2vnDzWrkk+FWSW358gIvHCHhdzR3fkzRhRxGFTuj3k8TTl988eXAq399qa/YJ6kKbYt3RnNOMDLIus4lUfJIjGSqqqOozU6i/nPeFEtE07GaDLE8EmwCWdJiPHLGZLihIcYR98wPR7XKBmHu5kiiP1FzmhcqAuxQG+yI04sjsKs1DAU+NjC75kpFHNrIYVSx5Qnpi4GKvXnfCoVbf9RX7K0NcWQw2SHF3wal/tZIo2o8xt0EwWRVh5LAzWSQbS71hvWEa+FP/WYbHYVJqfRGhNN4dKR6IIOEzlPbSzVHQ5QTjraFYWOlP0r8bJBA/fW8WrUivDZyXHSxf9XSjRqo2AyiW3/UVWx2rS7WEatLAlEbYY+Vyc6YGmCDSGqbw0lkN9sJmBnvgv1UHSf5WCrC68J89q2b2vws6oaFu5rjLrLmd06fgjx/O2RSdyzDywJVsU44uTJBEVYbOS662GxZjN4gis38yZfQEM/l6Ylu/VFXsVOne2NvaxTSfWxRSCWald4kKmVRzibwc5iAlenu2DMzEH+u9pP60IrwOnB9XQ52lUxGETUN9SGOKAuwpy6bDbJ9WS1ig4Ozw/DAzQm4Z2GENMBBDN8bOYwudk5j9+AChpt3zMNLrz0jGVnsOrPW1+yYj3PnO6cPcbz57quKuBjk50f/sof6xd1flFg8M1boP0pTZ7GJU1X22EeCzktxRhGVtAZ/K7KczTGHqto7p6uwt1kFR7K6xXC6cG1DIY4ujcZ9FH8k/YmYVV8a6IhtVX7Y1+CPI3NCkUj2QA51x/zMr1OE10YOo4stT0weh4jHnzstfc7k6E3sJ198EGXzOsdYf/Rp56vW008c0Vxnn0vFMLpQV7Fz6gMwO0WFIqpK1xR64+Y0D6S4myLL0wLRZIFnkBBm1/ddopvaMhRujLn1QYgko+zhpRHYUzVFemtWRd2udUmuWJk7GQUqWxT72aI62AGFPlaIKXJXxKGNHEMi9pmzn2rC94WqBSmaY1HsluUF0u8nn/9X+n3u5cekXwbu55dfflakrQt1FfuxHbMxN8sXLWH2SCaRw0ngYhI+gtrsFDdTbC72Qd3UvgcJHllVhsVFSj9lRVE4sSQSp1eEY3uxF7XXZsimdruSqvBm6r7VhzhgOgmdSiW+kSz3DTUqRRzayDEkYvMExcQZTjxyoMc5uz5vTYVCbH6Nf1Rh+PTMhzj+yD7pfP4t+n/n5dRV7FRqq0tiXLBnRjBWUH83k6rTLC9zRLuYIJHEPtQShEdXx2FVQe8jSrYsbUTcJDOkeZkprmVmqHFicTjuXxqFMhI2i/5E06jdXp/thQNNKpxeEoOTSyNxz+JobJ8RArvxfffb5eQYUrE/+OhtvPjq05q4vvnuK5TOjcHbH7whnbMlOFjJZWBis5cya+9cgPufvBunHjusiSu3KRCrtrX2iP/b779RpKkrdRa72pv6vLYo8Lcli9gVO6j7c3heuDTSJJH627urfHCCquEjbaHKsMTiSA8E0p/Cx2EiKvN7/iF2rmnCsbZgnOqIgJ+LKSLcTKibZYuGWDfUJ3oiboo1GYMWyKGmwsfsekXcfZFjSMXuD2yQAgcv2ev/3IGZK4o08bDzukWZmvP/vP8v6c/y8DNHFWnqSp3FJlakhmBmlDOqw+2lAYLJJJ6v/Tj42I7HjuJJ2NkUjONLY9Cc1DOetcuK0ZTsgYOLIrF3QQQiZd+knz25EeurgnCoNQR3t0UgkKrwTC/2yrXTAq8JskcZVecF1McOcZqAqAI3xX31RY4hE5sZUgx8LNrGPUs1cW7as0zjj0OsxjlvvK1eus4GMH72ReeQJT6seKDUVeyZOYHYUOWLXVSzHFsUjj0tatw7NxQ3USmd6m2DBDcq3U1q7J4VirVlfji8IAoZBZ2jSo5RM1MX44wNDUHIp2o6zdsSSfmdRtaexnCUhzthW4UKCxJdEEFizwi1x8YCbxyguNjYtGNUjR9sC8PxJWGYNTtIcW99kWPIxOaJsrU/OZ7+28NYfFuD5vyRv57QHGsTm5F9FmXtNbe+f/jxvMKPPtRVbFaNsxEm030tke9L3a4wJ6nUlYc6IpNKYSSJtDrXC9tJ0PXlarQmuWDfnHAp7PJpwcgmizrCzRye9iYIdDJFkp+FdG1ZiisSJ1thaYYnUug3jUp1sS81FWoq0dSfZ12tXKrGs5kV7jIB9k7DdPBCb4nKkUdGTW/oS2yR2w+uVrjpQ53FJiaWeqKYqtTpwXaYprZFKglTR0bbrgayI/KnIMTFjPraQdhaG4wEEv8wVc33rSwka9oek0hk9m17YY4nfJzN0JavxnN3TsfcZE/qdpmhPtIJKvoTrE5xx9aiKdLXrjwy0soD7FDuZ41yEj4iy1lxT/2RY0jF/vLrLzTxcLBS2Rv0EXuw1Edsxq3T/bB92hQcmRuCO0p9sSzbGw3hzijyt0M0+xhCItdHO6PAywo7K/xRTdX3E+tTqHo2RU2gPW6bHoAGKsXPbUnH7nmRSKFSnOxphWyq2oNdLZBGpbgl0hkPUvV9cnEUDswJwpKpXvRHGK+4F13IMaRiyxPuD8NV7JgcV2kkyYxIB1RRv3caVePFVIUXUSncU6dCnIc5cqkq9nc0lT6QtEQ5IY+s6odItKduTcOyHC/4U6l+bkMyHloWS9a9PTKpvV9R6IdID0vkkhG2pdAbefSnKKASPS3Ekdp3aiKoX+9jrV/1zckx4sXevHe5wk1f6iM2Y3iqE8JtbkAutaFsNMnehgAcnhlM1rkVZkW6IJfEqfCxoT+FLTInWSKNeLg6AA+2R1DXKhKbM93w1KoozM6cjAq1I6oinLG+LBCeTubIJ7Hbsj3w8M0p1OdOQBbZBoH2Y+GpMlfch67kGHKxX//Py1I8b7//OuatKe9xbeNd3RY6E5uNIn3qpYfwE/W/2ZwwNhqVT9Fl/XMW5udfflKkoS/1FZvz4NwIbC7zxfQIRzSH2lEJt0YGibM6jww5KqWz4pwR5mGGmEnWyPK2RiZVz5upZOf72iFlig2qQp0Q42EhvQqNoN8WiqeOqu/yQKoxAh3RmOKBQ/PCUBwysC9onBxDLrYh2b6uSqLori+/+qbblhCvaWNysSf8La6XXrKUU1XOxpjdQW35VBKqOoi6VtRes3Y4h9rjXGrLZ5OB1hLuiCLWRSP3TdTWL453Q12gHRqo3z6ZSnUiWd1JVBscmh2MWcluCHYYh4hcV0Xa+pJjRIttKA5EbM6oTGfcUjgJ28hgy6NqfToJz74976xVI9Gdqt7J1thY6od5kY442h6FZzekYla0Kx5ZlYgNZSqEuVsgnkp8dZgj1lYE0J/FHukqO6ynPndlhI0ivYGQY1TsmsGJ3TI/GfOT3JDvY4ksT3PEelpib2MAdZtspMEGxcRYarPjPC2QT4YbewvGqvR8Pzuk0fmKRDeEuZEFTjXAnY3BODwvFL6WY2A67hpE5g2+VDNyjIpdMzixGcOzneE52Qw+9uOwd04o5qe6UVfMAUUhDqijkh7jZoZAN3MsT/PEYytj0BrhhOOL41BFpTibRO9I9pBmcxao7bF4qq8i/sGSY1TsmsGLLaev2XVwGXOVNL12N1Xl7GOGn6MJqiNcUEClvIa6UhmTOwcoJlItEOZuhigy5jrSDFOKeyPHqNg1hhVbTpcxV8PPnxledigMdkS4iyluy5mE2mA77KimPwJV3Wn0B/CwGIPrx+g2KHEg5BgVu8Z4YjMWNYbhzzPDpC5aNHXDNk71QbmfFWYneSKZSjRrtz1MdR9iNBByjIpdY1yx5xQm466WAKSThR5Fhlg2WefJZMiVh9iiLcwOSzMmSWPYErI6V0YyBjlGxa4xnthZ9f4o8nPAnpYgMtAsqN12QnumJ47ODcUOKum7qV/+0IoY6p5ZItzZRBHeUOQYtNhsW4iSOdH9smpBMpqX5ffLtlsqsWhDfb9cd+cC3Lrrxn555P47+iX7VKrt+QbD29rrEE0ismU0kqnrVRpohzgq2XsrfJHuZYUjbRG4qzUcoS5maEtwRr6RjDQO5/wg/cS+1CFm1GDYnKCWPlHWBjmgxMeKDDIbqXTfmuYuWeRLCnywNN5F+radSH3xlnB7RRyGIIdNpq+kZWhdxkZR5k6Mij0g5tSrMM3LQhL75mxPVFCpbo1wxIZCbxSS6GxAwoZsVqWH4MC8CBQH2GJhkiuWpxu+dHNc27Xp64MvPGEpyizhjyGWb8nFZlsKyvnx5//Fa2/9rV/+7bVn8Pjzp/vl6ccPU9V6Z7/cemCVNJypPy5cX9Mv2a65HGJGDZR7OqqQ7m6ObKq+t1UHoJm6W4sT3dCR5E5i2yLU1RyPLI/C/SsS8MzGFBT726Ihxgk3ZXsgr7D30akDJQcvuKLGGqjKE0v6arMvBRraQJvWEoG2JA8UUh86j6rrQ3MjJbE7Ej0Q5W6JeOpysZkdj6+Ox183p+Khm+KRQe16pLuFNGlvUYILMsqU8Q6UHP2KveHgwavkYuuzXvhIoSHFzqj2g5fJGHiOvUaaeltO1fPh+WHoiHZGI1sig62P4mWNQj8bPLEmHo/dkohH1iZJ87DZ+3Praw3/coWjX7ElkIet9+6SArAqWYxspNOQYsuZPcUGSe5mONIajPmRTlhE1Xi6tzUayWAr8rPFPbOC8ezGdBxf3LkaUoTTBCRV6jZZTx9y6Cz2H0ItpADDcS/NwdJYYkdPtsU0P2ucXBaDGWH2WECWd4CjCeKpLU+m6r0uyglP3ZaC/S2BSKFq3MGtc1FaQ5IN8uDQWWxjtNscK7fNklY95GDLSot+uf9FGxqkGSIMRx/eq/AzEBpLbMZif3tsr/ZHDRvkr7KTulysfQ53M5N+jy+Lxx1Vfgh3Mc5LlX+/80/pueZtWa6b2A456lPGErs3N23ubAVE0V/rTaUKv/rSmGJn53hiRY4XqqiEJ1BfOp26Y/Ee5khha54F2GNFqhsaA2yQ2sv8L0OQD+NiNbNOYo+Jszdnnn7+5WcpYGa9vyLSgZCvNS4nxxMvPKBxe+rFBxVCNC3J1fgV49CXxhQ7s9oXpYH2KKE2OczVDJHU5com0TOp7Q7zsEAsid6e7o7mBOO8G+fQCB0w/mNRXyXI4wuv/0MK+O6HbykiHQiLZnfOlpBTDtFNm1/RXV9++53h+9lyZvjYYyoZZGxiXp6PNbIns7FpNsghA45Z4HuozS6PcFCEMwQ5uNh+FdHlorRKGKndFsnx1IsPKdy0+RXd9aV8J3rxmiGYqJ6EACcTLEvzkEaTZlA/u5Daa2aUZagdsL9RJc3v8nYe2CQAbeSL+LOtNXWqwjUYYrH5+ZodbQo3Tj69V3TXl8YU+/jOZfCyM0VRgIM0Po2NS2NThHL9bZFApfru5kBMZS9U2AcT/+51yQ1BthYsw6Ida/QTu33rsrShEpuvPsz48NNHtab5xjuv9OquL40ldn5jEKbHe6Es3Amx1N9mgw3ZUhlRZIlnsyk/JPy9JHZTmB1dN6c/QudEP0ORQyO0rmJLkIk90CUt+uKFC7/0EJpx77HNmjRF/8Nd7I3La6lPbYZkEjKLhA10MSWr2wpT2foo1GbHT7LC7vpgVAU5IJe6ZrlksUfrOfe6L3Jwocclu9qLkmqHTGwGMfLBcO+xLb3G2bI8X2t6X3ZZ0aK7vjSW2CVhbPYHG1JsjXiqsuPcLZBO1ne12g5l1FZn+9hI78Ez6XdWrDOKA+0QmmQYQ23V7a2aZ9K/VBN+EzT+Xf/KeINnzOybOg2JmSu7V1iQU1t62tz1pTHEPrSqCaHhbmiId8cUexPUBNhKL1QaguxQROJn+Ngim6r0BVFOyKBu2do8L0yjP0FIkqMiroGQrT3DMSCx33nnnT8aut1m2zYx6LIPiK7u+tLQYrP5Yr6WN0jHhxeVIsjZFIuiHaV35Q0kegkZZGxeWC612wtj3VBG/fDtlX4oUtkhOt8w1TjH9+fPdYk99l1Rz/4hE3vr/pWKRPQh2x9k/4mtaFyaI/GWne048sCd+Prbs1L8cr8Mx//SuTISI9t2mUGfiXjaaGixC6cFoyDIEY0VGcicbI1wV1OszXBHabAj8qlUV5DIbFJAPrXf0eybN5X4/Q0qZFC7Hj/AvbtEcvw2yFT/Uq0BBZxcGilFxAwqMRFd+a//dL6g6Qty/+XzO/fsfO4fj2HGykLpeNrcWEW8A6GhxV7fXoo4srhrQ+ylseLB1MfemuOJ2wu9kevDJvZZSuPFc6l0sxWMQ50n4mhbKJI9Bj4tVyTHgKpwDboCGzJz9CHb4nHDXYsV7oOhocW+tS4FphOvwxTzMVA7TJRemLBlM47UqZFJVfl0fztp7ZRSssorA+ypmjfB6WWRSJk0uKm5nE++0LkNxtfffStp9Rv12JdFGXXCdVH2oXKxX9Nji+ThSkOL3ZoTBFerG1DcHCktYsv2Bdle5IW7Z4Zib70aOWScxZGwbDpQEVtInkr/geYAJHhZINkA2yhzDK5Uc1AElweZGDSDLiYNLXZteQhSqKvVPKNY+pSZ4GGGncXeuKs2APe1hmJWgqv02jRxkoX0vrwyygEnOkJREeEwaGucLdTLYTCxL2ZVbmgaWux57cXSFotzUzwRSO11GHFn6RTsqfXHvbNCcPfcMER7Wkk7BcS5meLg3BA8sCQKW+pVmDTIAQw//fyT9BwlSxsNI3bSrMIYudhffXNWkehIoiHFrp4RizBHU6h8rBBEv2oSOsbVhEq1Cve0BmNfSyAJG4MUH0skuJtRFW+K44si8OjqeJxaEQc/i8HN++LgQl8f7fCiqJ/+oIhW7d5gsEy6mDSk2HJGu5oj2G48Aq1vwJoSb2yu8sGqfA/cRFV6VqANwuzpmu04bKMSvZdK966ZgdLmbmI8uvL8D99rnsMgpZrDNNnzcXnpZjvuiYmPFBpL7KEmx4eff9wl9rgvRN0GDpnYDGLiI4WXgths/XWO34eYSWKnzJ59tSjZwGFAQ40tYKstjo8//0C6ltcSLL0xe+TZ49I5M0ZEvwPhpSA2x4uvv9xZqlXjPhTlGhxUYz+Tiy3fNVdXVi3s3j2AQbzO+Mq/X0BR137bnBy9jWPTl5eS2LwAdnR0XC7KNSisOXDg/1jEvx1gn7vuxkys+3NHj5sV/TDy/bXl5J83tYXRh2xRPUPFdTH4/kdvae7foIaZiDFxzn9nka/eu0lKTNtuuP2RQ3TXxoeevk/vMNo4ksVmuy1wcKGvCLV4T9TJcBDa7uzG3gf590UO0V0bP/j4bb3DaKM2sUvndC6ZefDU9p7uXUtpsi2r5O6vClOjxNE8fDMbzrmry1C3KEM6zmsOkrazZIsbyP30R46Ft99k3FKtQcDYM3KxB1K6OUR3beTYf3yb4pq+1CY2pyi2nEwgfiyKzWa23HFkrea8L7HZhnT6blU1a9VUzX1rhFaN/1KUx6A4ePDgb1lCi3au6TPT+qK+4fT13xf1EbuvCRKi2I89d6pHnH2JzePWdg+9UQ4utqSFsdFwy7wseenWdwIgh+jeG5944X6d/erC/sQWRWKDK9gWF2xLZ7k7m2qT1eCP9FofTVxsYzq2aAE7ZvuOsu0uPj/7iXR+6vFD0uID7Pjx509JcT5KfxAx/d7IuqEcXGibZHdPURfjQWi72WpB4k1qI4foLnLq7Aid/OnD/sQejuR45KWnh6itFtGV6POv/V3vzNPVPwMbwCC6D4Z9ic3b3Fkrp2qO+S9rr8X9xbSxuDVKc8xWhapfnKXwc/vBm6S46xcpr8l56HT3jFee51sPbr1WlMP4EEq3rsYah+jOWTgzVHrRL7obgn2J/fd/Pas55td788fdzp3/Dks3NUvHn3/RuWg9O67pSMPZr88ohlK9++GbVO13WuBzbp7WY8+y3rhmZ3vnjWKgg/8NCJ+yqCaW+N2PndTclC5bO3CI7oxta6dL1z789D0N+etVbWH04WDFZkOgp7cn4ebb50rnr3aN3rnljnaceGS/dLxkY5P0++NP5zWbxzKywQbcCudis6ZKHr+ccnChAyriI0Qdhg5C6WYQb5qTCcm+h3PsObqpx8PuPHyLLJbeIcapLwcr9sNdb/i4u7jPGKuRuNiMX3z1ufTLdwr+/tx30i8Xe4GW3RGKZoVr7tMibXKn2AGG/LI1AHgWRV/JbmRCkrvm5kq6XlAMR/YlNi+FGfW+PUpkO/1JazrSe/jhrGhL7LGLILvOyFZ65G5sYQEejlnW7Ji11ey3uDVScR+MHO9+/IGmVBN+I+b/0KPrZq6MsNHc5OxVJYoHGA7sS+zhQo6X//MveTs9DIS+rPtFC+PRJzuHtg7XzBzuYrPXrhwaoTvFHj6YmOS5UGy/L/x6QfEwF5vDWWw+U5XhH2++qhE6tCnVWszviw6/qoRUdnO/CZyouennX3lC8VAXk8NV7GnUfnM0r2vXCL1+/fo/iPk8fKAa9xG7ybiWPM3Ny63Ti83hKjbHma/OaoRWVca3itk7/NB1s8/+80XNQ7D3yOIDXgwOR7HlGLbttDZcEWr5vth+M4gPeTE43MSWQy50QHVimZivwxbuhSEzhqPgw0ls9nqZ4/JAk26DrKPjd2J+DntcEWrx7nATfLjcB1+NkOGqSFuN0AUdtV5iPo4cdD3E74LNZNl88TJ6ONyDXOjrYhw1QjsXqCvF7Bt5kLVFcoiZMBQcTumzLirPF/NUr+Nito1cdD0UWwpCDjEzjM3hkjZ7tczz5IZYp2fF7Br56Ho4+UsXhqnCpABjUg7xmrHInk+O3wd3TtlhHBt3KQrNETD+V/6gcmt0/4nBjxzVhXKI14zBZ//xqCY99vpY3qRNSHa9W8yeSw+yB5aDdYvEzDI05RCvGZry9cnO//hDD6Enpni0i9ly6aJr/Dnj6Wf/IpPAuCIMRTqZDZ3DhDnW7NvSQ+j8BdMDxOy49CHLgJ9/6S4FDGIGGorGTiOta2gxxxeyd92MfoVx14jZ8D8DdVVyqTwz5O04g5iZg6Wx4i6cGdYj7u/Ofd9DZMNOlh/BCC0JlZbO5Fx/4PYeGSdm7GBojHir2pN7xOuSH9xDaKe8gO3iM/9PI6w5J1CeQaee6dmOv/x6zxkZA6Uc4rWB8OeuFYs4fMpiewj9xwirV8RnHUUX2retdJNnlndpdI/M/Pc7rygyXB/KIV7TlWzCgAj5PTNapnnvF59tFNogy7jfBfd868Zw2+5FChF0oRziNV3I1nAVIQp92XAZHDiioBr/rTwT1x/s2ZYziGL0x4GGnbemvEdYhmtjHHqKzO53FAOHf0mstTxDnfMDxTyX1kkRxdFGOcRrvXHHoe6pyRzfdC0KK6dNlreHeO+jGAxkr1oZk2d3T1CXI61W+7rkcojXOMvmdS6BLUIU+LKACRfEWxyFIaEe+46Y6d98370CkhyiiP2JXTave5sMOVhtIqZ5edDEN8VbG4WRcHnQhPdEAbThPdmug3Jwt0+/+KiHO8fW+3YpRJ6Y5PageC+jGEqox/8oiqKq7L0q7g9iPIxXhFhcwp8hRyqENp3z23PfiZr2wBdff6kIIzGAmoxRDG/YZvrepxCOOCbOCZ9+eUYjclxLvsIPCXxuQrTneDHOUQxzmKdSd6hrhkp/VFcnbhHDj+ISwO9DzJ4S3UYxilGMYmTi/wEHOWU4ZTcyMgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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8+6779omsTfeeMN2JH799dezChD27bHHHqm4r732mh0A8bnnnrNNaOgEjWYxjDSNwRYxLhDe6MLbZdmawACawNCH6NRTT02Bdf0WGL6nvXv3NkceeaQ56qij7GePHj0oQAyxz2cKECFFIkoBAh269PaJj7DlWSN88csNLTphFFKApKZEgjQZ/fvf/87YJ9sRconKcccdF3gcPh9++OGMDsyyHduyiRXA9y0ozUmTJmUcu2TJklTaEj777DOzwQYb+NIU4l4wulCAwkPc85kCREiRiFqAKh0tOmEUSoCAlhEErI8bN863XfblEiCM9xN2LMRKn1OWdTouEBx8v3TAseis7V4TBEhL0hdffGHvm05XiHvB6EIBCg9xz2cKECFFggIULVp0wiiUAEEqrrzySjuVhAYDGeLNKbxijiYq9AnC2EAYMDFbUxLYYYcd7BtemLwUb3ehj84jjzxiHnvsMfOPf/zDzguGJjW8dYaBCufPn2/HIMomVvJ2GZrVcCymtsDozkgDabs1QGh+Q5Me+v0gXYBmPQoQQ9zzmQJESJGgAEWLFp0wCiVAEA63NkZqTTBuDiYRdWtRJGA9V1PV73//e18Nj6SLSUpl7CG9P1u62IfvXNBxECr3FXepAXLD559/bjbaaCNfukLcC0YXClB4iHs+U4AIKRIUoGjRohNGoQQIUhE0ECJA7Y2WCIR8+urst99+vvRkOUisRI6ypQvBwWzw+pqwjo7W7rGo+cF292/76quvTPv27X3pCnEvGF0oQOEh7vlMASKkSFCAokWLThiFEiBw0UUXmfPPP9++9XXuuefasXYA8hmvnWNAxDPPPNOcccYZZuDAgeb000/PKirY165dO/u6OyYpxSea0DD+D5rb8EYW0qurq7PnxPnR1IaBC3VaGtTgXHDBBbYZ7cILL7TzlOHtMVyne01nnXWWbcbDeTGidUNDgx14sUOHDr40hbgXjC4UoPAQ93ymABFSJChA0aJFJ4xCCZBbA6QDhCQsZOurA7baait9SCqgBigsZBMrsMsuu+hDbEB/Hzfee++9p6PY6TF23XVXX5pC3AtGFwpQeIh7PlOACCkSFKBo0aITRiEFSDcpIWAbalfCQrYpJQDOFRSQLvoABQXs0+losgmQK0+YzgPB/du+//57s/vuu/vSFOJeMLpQgMJD3POZAkRIkaAARYsWnTAK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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACN0lEQVR4XnWTX0hTURzHb3+kIIhW0hY1a74sy1mtiNUaLCJYjGJRUAiJ4xa1BJVyT1mtWpYbyHwYE3zSgfRgL/bSiMRRROvJlCJFAmk0EqoXH4zR/Xa/v7VLu9CBL+fH7/v9nHMu51xFMY3JWHudNmzZj7wzgldNSZFes0fPnK8ZyGx04vWeDN65i3jvQ43Yo6dnzJwMTO3y4a1rVsKfAsDnC9AW20SspUePGT1rgDzWs+GIu5Q7PvO9EMTyhwqIpc4asbf88SKYKeX8M2TkkwLt6efnrqQWw1djWiQ6gBu9CfQl7+Pp+APkJxMi1uzRY4ZZMmQVz6nuFX+zFwHHIXS2PYIaisJvd+HokVYEL93RdVdq9ugxwywZsso+T2iE5mWXFz2BsMznN9ULEH+oili3NjaLHz18wvDJKrfDLckzuw/gZlOLmD0OB67ZrLJDPtclYl31OdMnQ1aZT9sS6ll3ZQcdpmTB6yfxc6FLxLq6CX1myZBVyiOWSCHVUGYjeMwjIjA/FTKukTV7VZ/ZwuDOMlmFL+xXdsuX0hM7Rm85RD/yByt3zrv/e//sTWedoq9jdpAhW3m66Q0ZjFow3W9Dh2crxrp3YGnCCbzZa+j3i0aRNm4Fs2SMpy1PeGDdLI25vu1Ind6GXq9V5qxqE3HxKixZ85NGfI1PjMH12spQvSz0ssOOCbVB5m+JzaAnGT1bA1eHnCS+egiP1xYl/K/664rimXc2D+N3jikR3FuVFOn1/37nP3j88P8aDcEUAAAAAElFTkSuQmCC>