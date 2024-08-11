# frc-attendance


**Project Setup and Initial Challenges**

I devoted four class sessions to the process of downloading a single library required for this project, followed by an additional class dedicated to establishing the foundational elements of the program. Despite the challenges encountered, I made significant progress.


**System Upgrade**

To optimize performance, I transitioned to using an Alienware system, known for its superior computational power.


**Software Compatibility and Support**

I also updated to a different version of Python to ensure compatibility, yet I still required assistance from Mr. Cloos to successfully download the library, as initial attempts were unsuccessful.


**Library Implementation**

The implementation of the library itself proved to be straightforward. The primary task involved comparing known face encodings with video footage.


**Detection Accuracy**

The system effectively detects multiple individuals within the same frame; however, it encounters difficulties when distinguishing people with prominent beards.


**Confidence Calculation and Data Recording**

For confidence assessment, I calculated the confidence score by measuring the difference between the face index and a baseline value of 1. If the confidence score exceeded 61, the information was recorded in a text file along with the timestamp of detection, enabling accurate tracking of individuals. Each face could only be recorded once per program session, with subsequent detections requiring a program restart for re-recording.


**Practical Application**

To apply this technology in practical scenarios, it will be necessary to capture photographs of individuals under similar lighting conditions and upload these images to the database.



