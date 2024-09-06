Scope of the project 🚀

Facial recognition is becoming more prominent in our society. It has made major progress in the field of security. It is a very effective tool that can help low enforcers to recognize criminals and software companies are leveraging the technology to help users access the technology. This technology can be further developed to be used in other avenues such as ATMs, accessing confidential files, or other sensitive materials. This project servers as a foundation for future projects based on facial detection and recognition. This project also convers web development and database management with a user-friendly UI. Using this system any corporate offices, school and organization can replace their traditional way of maintaining attendance of the employees and can also generate their availability(presence) report throughout the month.

The system mainly works around 2 types of users

    Employee
    Admin

Following functionalities can be performed by the admin:
• Login
• Register new employees to the system
• Add employee photos to the training data set
• Train the model
• View attendance report of all employees. Attendance can be filtered by date or employee.

Following functionalities can be performed by the employee:
• Login
• Mark his/her time-in and time-out by scanning their face
• View attendance report of self
Face Detection

Dlib's HOG facial detector.
Facial Landmark Detection

Dlib's 68 point shape predictor
Extraction of Facial Embeddings

face_recognition by Adam Geitgey
Classification of Unknown Embedding
using a Linear SVM (scikit-learn)
