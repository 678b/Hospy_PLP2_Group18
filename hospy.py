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

# ---------- HELPER VALIDATION FUNCTIONS ----------
def is_valid_name(name):
    """Check if name contains only letters and spaces."""
    return all(char.isalpha() or char.isspace() for char in name)

def is_valid_phone(phone):
    """Check if phone contains only digits."""
    return phone.isdigit()

# ---------- HOSPITAL MANAGEMENT ----------
def register_hospital():
    """Register a new hospital."""
    name = input("Enter hospital name: ").strip()
    location = input("Enter hospital location: ").strip()

    # Empty validation
    if not name or not location:
        print("All fields are required.\n")
        return

    # Name validation
    if not is_valid_name(name):
        print("Hospital name must contain only letters and spaces.\n")
        return

    if not is_valid_name(location):
        print("Location must contain only letters and spaces.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()

        # Check for duplicate hospital name
        c.execute("SELECT * FROM hospitals WHERE hospital_name = ?", (name,))
        if c.fetchone():
            print(f"Hospital '{name}' is already registered.\n")
            return

        # Insert new hospital
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

    # Empty validation
    if not name or not phone:
        print("All fields are required.\n")
        return

    # Name validation
    if not is_valid_name(name):
        print("Patient name must contain only letters and spaces.\n")
        return

    # Phone validation
    if not is_valid_phone(phone):
        print("Phone number must contain only digits.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()

        # Check for duplicate patient name
        c.execute("SELECT * FROM patients WHERE patient_name = ?", (name,))
        if c.fetchone():
            print(f"Patient '{name}' is already registered.\n")
            return

        # Insert new patient
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

def view_appointments():
    """View all appointments."""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
            SELECT a.appointment_id, p.patient_name, h.hospital_name, a.appointment_date
            FROM appointments a
            JOIN patients p ON a.patient_id = p.patient_id
            JOIN hospitals h ON a.hospital_id = h.hospital_id
            ORDER BY a.appointment_date
        """)
        appointments = c.fetchall()

    if not appointments:
        print("No appointments booked yet.\n")
        return

    print("\nAppointments:")
    for a in appointments:
        print(f"ID: {a[0]} | Patient: {a[1]} | Hospital: {a[2]} | Date: {a[3]}")
    print()

def cancel_appointment():
    """Cancel an appointment by ID."""
    view_appointments()
    appointment_id = input("Enter appointment ID to cancel: ").strip()
    if not appointment_id.isdigit():
        print("Invalid input.\n")
        return

    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM appointments WHERE appointment_id = ?", (appointment_id,))
        if c.rowcount == 0:
            print("Appointment ID not found.\n")
        else:
            print("Appointment cancelled successfully.\n")

# ---------- MAIN MENU ----------
def main_menu():
    """Main program menu."""
    create_tables()
    while True:
        print("=== Hospital Appointment Booking System ===")
        print("1. Register Hospital")
        print("2. Register Patient")
        print("3. Book Appointment")
        print("4. View Appointments")
        print("5. Cancel Appointment")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        print()
        if choice == "1":
            register_hospital()
        elif choice == "2":
            register_patient()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            view_appointments()
        elif choice == "5":
            cancel_appointment()
        elif choice == "6":
            print("Exiting system. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

# ---------- RUN APPLICATION ----------
if __name__ == "__main__":
    main_menu()

