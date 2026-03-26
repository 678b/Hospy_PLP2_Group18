Hospital Appointment Booking System (Hospy)
Overview
Hospy is a Command-Line Interface (CLI) Python application designed to manage hospital appointments efficiently. This program addresses common healthcare scheduling issues, such as long queues, missed appointments, and poor record tracking. It allows hospitals and patients to be registered, appointments to be booked, viewed, and cancelled, using a SQLite database for persistent storage.
The project is implemented using Python 3 and only relies on basic Python concepts such as functions, loops, conditionals, lists, and simple database operations with the built-in sqlite3 module. No GUI or web frameworks are used, making it a lightweight, terminal-based solution suitable for academic projects.
Features and How They Work
Register Hospital
This feature allows a user to register a new hospital.
Code explanation:
The program prompts for hospital_name and location.
It checks the database to prevent duplicate hospital names.
If the hospital does not already exist, it inserts a new record into the hospitals table.
Register Patient
This feature allows a new patient to be added.
Code explanation:
The program prompts for patient_name and phone.
It prevents duplicate patient names in the database.
If valid, the patient is added to the patients table.
This feature schedules an appointment between a patient and a hospital.
Code explanation:
Lists all patients and hospitals to choose from.
Prompts the user to enter the appointment date in DD-MM-YYYY format.
Inserts the appointment into the appointments table after validating IDs.
4. View Appointments
This feature displays all booked appointments in a readable format.
Code explanation:
The program joins the appointments, patients, and hospitals tables.
Displays appointment ID, patient name, hospital name, and appointment date.
