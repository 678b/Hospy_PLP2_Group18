import sqlite3
from datetime import datetime

DB_FILE = "appointments_data.db"

# ---------- DATABASE SETUP ----------
def create_tables():
    """Initialize database tables."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS hospitals (
                hospital_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hospital_name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                hospital_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
                FOREIGN KEY(hospital_id) REFERENCES hospitals(hospital_id)
            )
        """)

# ---------- HOSPITAL MANAGEMENT ----------
def register_hospital():
    """Register a new hospital."""
    name = input("Enter hospital name: ").strip()
    location = input("Enter hospital location: ").strip()
    if not name or not location:
        print("All fields are required.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()

        # Check for duplicate hospital name
        c.execute("SELECT * FROM hospitals WHERE hospital_name = ?", (name,))
        if c.fetchone():  # if a row is returned, it already exists
            print(f"Hospital '{name}' is already registered.\n")
            return

        c.execute("INSERT INTO hospitals (hospital_name, location) VALUES (?, ?)", (name, location))
        print(f"Hospital '{name}' registered successfully!\n")

def list_hospitals():
    """Return all hospitals as a list."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM hospitals")
        return c.fetchall()

# ---------- PATIENT MANAGEMENT ----------
def register_patient():
    """Register a new patient."""
    name = input("Enter patient name: ").strip()
    phone = input("Enter phone number: ").strip()
    if not name or not phone:
        print("All fields are required.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()

        # Check for duplicate patient name
        c.execute("SELECT * FROM patients WHERE patient_name = ?", (name,))
        if c.fetchone():
            print(f"Patient '{name}' is already registered.\n")
            return

        c.execute("INSERT INTO patients (patient_name, phone) VALUES (?, ?)", (name, phone))
        print(f"Patient '{name}' registered successfully!\n")

def list_patients():
    """Return all patients as a list."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM patients")
        return c.fetchall()

# ---------- APPOINTMENT MANAGEMENT ----------
def book_appointment():
    """Book a new appointment."""
    patients = list_patients()
    if not patients:
        print("No patients registered yet.\n")
        return

    print("\nPatients:")
    for p in patients:
        print(f"{p[0]}. {p[1]} (Phone: {p[2]})")
    patient_id = input("Enter patient ID: ").strip()
    if not patient_id.isdigit() or int(patient_id) not in [p[0] for p in patients]:
        print("Invalid patient ID.\n")
        return

    hospitals = list_hospitals()
    if not hospitals:
        print("No hospitals registered yet.\n")
        return

    print("\nHospitals:")
    for h in hospitals:
        print(f"{h[0]}. {h[1]} (Location: {h[2]})")
    hospital_id = input("Enter hospital ID: ").strip()
    if not hospital_id.isdigit() or int(hospital_id) not in [h[0] for h in hospitals]:
        print("Invalid hospital ID.\n")
        return

    date_str = input("Enter appointment date (DD-MM-YYYY): ").strip()
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO appointments (patient_id, hospital_id, appointment_date) VALUES (?, ?, ?)",
                  (patient_id, hospital_id, date_str))
        print("Appointment successfully booked!\n")

