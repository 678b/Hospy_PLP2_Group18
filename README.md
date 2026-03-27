Hospital Appointment Booking System (Hospy)
Overview
Hospy is a Command-Line Interface (CLI) Python application designed to manage hospital appointments efficiently. This program addresses common healthcare scheduling issues, such as long queues, missed appointments, and poor record tracking. It allows hospitals and patients to be registered, appointments to be booked, viewed, and cancelled, using a SQLite database for persistent storage.
The project is implemented using Python 3 and only relies on basic Python concepts such as functions, loops, conditionals, lists, and simple database operations with the built-in sqlite3 module. No GUI or web frameworks are used, making it a lightweight, terminal-based solution suitable for academic projects.

Features and How They Work
1. Register Hospital
This feature allows a user to register a new hospital.
 Code explanation:
The program prompts for hospital_name and location.
It checks the database to prevent duplicate hospital names.
If the hospital does not already exist, it inserts a new record into the hospitals table.
2. Register Patient
This feature allows a new patient to be added.
 Code explanation:
The program prompts for patient_name and phone.
It prevents duplicate patient names in the database.
If valid, the patient is added to the patients table.
3. Book Appointment
This feature schedules an appointment between a patient and a hospital.
 Code explanation:
Lists all patients and hospitals to choose from.
Prompts the user to enter the appointment date in YYYY-MM-DD format.
Inserts the appointment into the appointments table after validating IDs.

4. View Appointments
This feature displays all booked appointments in a readable format.
 Code explanation:
The program joins the appointments, patients, and hospitals tables.
Displays appointment ID, patient name, hospital name, and appointment date.
5. Cancel Appointment
This feature removes an existing appointment.
Code explanation:
The program first lists all current appointments.
The user enters the appointment_id to cancel.
The selected appointment is deleted from the database.
Database Description
The program uses a SQLite database (appointments_data.db) to store all data persistently. It has three main tables:
hospitals
hospital_id (Primary Key)
hospital_name
location
patients
patient_id (Primary Key)
patient_name
phone
appointments
appointment_id (Primary Key)
patient_id (Foreign Key)
hospital_id (Foreign Key)
appointment_date
Why appointments_data.db Is in the Repository
The repository includes a pre-populated sample database (appointments_data.db) to:
Demonstrate program functionality immediately.
Allow the facilitator or any tester to see sample hospitals, patients, and appointments without creating them manually.
Avoid errors that occur when the program tries to access a database that does not exist.
Note: The program will use this file automatically. Any new data added during testing will be saved to this database.
How to Test the Program
Ensure no other program (PyCharm, DB Browser, etc.) is currently using appointments_data.db.
Open Command Prompt (CMD) in the project folder.
Run the program with:
python hospy.py
Use the menu to test features:
Register Hospital – add a new hospital and check for duplicate prevention.
Register Patient – add a new patient and ensure duplicates are rejected.
Book Appointment – select a patient and hospital, set a date, and confirm the appointment appears in the view list.
View Appointments – check all appointments, including newly added ones.
Cancel Appointment – delete an appointment and confirm it no longer appears.
The program will keep running until you select Exit.
Important Notes for Testing with the Included Database
If you are using the downloaded appointments_data.db, do not delete it initially; it contains sample data necessary for testing.
Ensure no other program locks the file. If you encounter a database access error, close all programs using it and try again.
You can start with a fresh database by deleting appointments_data.db and running hospy.py. The program will create a new empty database automatically.
Project Setup
Requirements:
Python 3.x installed
No additional libraries required
SQLite3 is included in Python by default
Steps:
Clone the repository:
git clone <repo-url>
cd <repo-folder>
Run the program:
python hospy.py
Follow the menu prompts to use all features.

