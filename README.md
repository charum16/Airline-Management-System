# Airline-Management-System
A command-line-based Airlines Management System developed in Python using MySQL for database management. This system provides core functionality for passengers, employees, and administrators, supporting tasks like booking tickets, managing flights, and employee duty scheduling.

📌 Features <br>
👤 Passengers
View flight schedules

Sign up/login using mobile number

Book tickets with seat selection

View, update, or cancel booked tickets

👷 Employees
Login with employee ID

View assigned flight duties

View full flight schedule

👨‍💼 Admin
Highly secure access

Add or cancel flights

Update flight status

Manage employee records

Assign or change employee duties

🛠️ Technologies Used
Language: Python 3

Database: MySQL

Library: pymysql

🗂️ Database Structure
flights – Stores flight information

user_data – Stores passenger data

emp_data – Stores employee credentials and details

ticket_record – Records ticket info and mappings

duty – Maps employees to flights

<flight_code> (e.g., IG5882) – Individual tables for each flight storing seat and passenger info

⚙️ Setup Instructions
1. Install Required Package
bash
Copy
Edit
pip install pymysql
2. Setup MySQL
Start your MySQL server

Update host, user, and password in the script if needed:

python
Copy
Edit
pymysql.connect(host='localhost', user='root', passwd='your_password')
3. Run the Script
bash
Copy
Edit
python "OSP Project (Airlines Management System).py"
The script will:

Automatically create the Airlines_Management_System database if it doesn’t exist

Populate tables with sample flight, employee, and ticket data

🔐 Default Admin Access
Password: 12345678

Use only if you have authorized access.

📝 Sample Data
Flights: 5 sample flights added during initial run

Employees: 3 sample employees with different roles

Tickets: 50 tickets initialized with auto-generated IDs

