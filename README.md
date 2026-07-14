#  Hospital Management System

A full-stack Hospital Management System built using **Python (Flask)**, **SQLite**, **HTML**, **CSS**, and **JavaScript**. The system streamlines hospital operations by providing separate dashboards for **Admin**, **Doctor**, and **Patient**, enabling appointment management, doctor scheduling, online payments, reviews, and profile management.

---

##  Features

### Patient Module
- User Registration & Login
- Forgot Password & Change Password
- Edit Profile
- View Available Doctors
- Book Appointments
- Prevent Booking for Past Dates/Times
- Prevent Double Booking
- Online Appointment Payment
- Cancel Appointments
- Automatic Refund Status for Paid Appointments
- View Appointment History
- Submit Reviews

---

### Doctor Module
- Secure Doctor Login
- Personal Dashboard
- View Assigned Appointments
- View Patient Details
- Accept/Reject/Pending Appointment Requests
- View Working Shift Timings

---

### Admin Module
- Admin Dashboard
- Add New Doctors
- Edit Doctor Information
- Delete Doctors
- Manage Doctor Availability
- View All Appointments
- Manage Hospital Data

---

### Authentication
- Role-Based Login
  - Admin
  - Doctor
  - Patient
- Session Management
- Password Reset
- Logout Functionality

---

### Payment System
- Appointment Payment Status
- Pending/Paid Payment Tracking
- Refund Status Management
- Prevent Payment for Cancelled Appointments

---

### Review System
- Patients can submit reviews
- Reviews displayed on Home Page
- Patient names shown with reviews

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| SQLite | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Client-side Interactivity |
| Jinja2 | Template Engine |

---

## Project Structure

```
Hospital-Management-System/
│
├── app.py
├── init_db.py
├── update_db.py
├── hospital.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── patient.html
│   ├── doctor.html
│   ├── admin.html
│   ├── edit_profile.html
│   ├── edit_doctor.html
│   ├── forgot_password.html
│   ├── change_password.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## Database

### Users Table
- User ID
- Name
- Email
- Password
- Role
- Age
- Gender
- Specialization
- Phone
- Experience
- Description
- Start Time
- End Time

### Appointments Table
- Appointment ID
- Patient ID
- Doctor ID
- Date
- Time
- Status
- Payment Status
- Refund Status

### Reviews Table
- Review ID
- Patient ID
- Review Message

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Hospital-Management-System.git
```

### 2. Navigate into Project

```bash
cd Hospital-Management-System
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Initialize Database

```bash
python init_db.py
```

### 5. Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Default Admin Login

Email

```
admin@gmail.com
```

Password

```
admin123
```

---

## Validation Implemented

✔ Duplicate Email Check

✔ Duplicate Phone Number Check

✔ Password Validation

✔ Appointment Time Validation

✔ Past Date Booking Restriction

✔ Appointment Slot Clash Detection

✔ Role-Based Authorization

✔ Session Authentication

✔ Payment Validation

✔ Refund Handling

---

## 📸 Screenshots

You can add screenshots here:

- Home Page
- Login Page
- Registration Page
- Patient Dashboard
- Doctor Dashboard
- Admin Dashboard
- Appointment Booking
- Payment Page

Example:

```
screenshots/home.png
screenshots/admin_dashboard.png
```

---

## 🔮 Future Enhancements

- Email Notifications
- OTP Verification
- Online Video Consultation
- Medical Reports Upload
- Prescription Management
- QR Code Based Appointment
- Payment Gateway Integration
- SMS Notifications
- Search & Filter Doctors
- Admin Analytics Dashboard

---

## Learning Outcomes

This project helped in understanding:

- Flask Web Development
- CRUD Operations
- SQLite Database Design
- Authentication & Authorization
- Session Management
- Form Validation
- Role-Based Access Control
- Database Relationships
- Appointment Scheduling Logic

---

## Author

**Ahana Gupta**

MCA Student

---

## License

This project is developed for educational and learning purposes.# Hospital-Management-System
