# Career Opportunity – Placement Portal

A web-based **Career and Placement Management System** developed using Django. The platform connects students, placement officers, and alumni in one centralized system to manage placement opportunities, student profiles, companies, applications, and interview experiences.

## 📌 Project Overview

**Career Opportunity** is designed to simplify the college placement process by providing separate functionalities for students, placement officers, and alumni.

The system helps students discover job opportunities, maintain their profiles, apply for on-campus/off-campus opportunities, and access interview experiences. Placement officers can manage companies, job opportunities, and student placement information. Alumni can contribute interview experiences to help current students prepare for recruitment.

## 🚀 Features

### 👨‍🎓 Student Module

* Student registration and login
* Student profile management
* View placement opportunities
* View company/job details
* Apply for on-campus opportunities
* Explore off-campus opportunities
* View placed students
* View placement statistics
* Access interview experiences
* Career roadmap and preparation resources
* Resume/profile management

### 🏢 Placement Officer Module

* Placement officer registration and login
* Add and manage companies
* Add on-campus job opportunities
* View student details
* Manage student applications
* View company information
* Manage placement-related information

### 🎓 Alumni Module

* Alumni login
* Share interview experiences
* Provide useful recruitment experiences and guidance to students

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend programming       |
| Django     | Web application framework |
| SQLite     | Database                  |
| HTML       | Web page structure        |
| CSS        | Styling and UI            |
| JavaScript | Client-side functionality |

## 📂 Project Structure

```text
career-opportunity/
│
├── Alumni/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── PlacementOfficer/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── Student/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── ppGECW/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
├── media/
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/prajwalcn27/career-opportunity.git
```

### 2. Open the project

```bash
cd career-opportunity
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔐 Security

Sensitive information such as database files, environment files, virtual environments, and Python cache files are excluded using `.gitignore`.

> For production deployment, configure Django `SECRET_KEY`, `DEBUG`, allowed hosts, database credentials, and other sensitive settings using environment variables.

## 🎯 Project Objectives

* Centralize college placement activities.
* Provide students with easy access to career opportunities.
* Help placement officers manage recruitment activities.
* Allow alumni to share interview experiences.
* Improve communication between students and placement administrators.
* Provide useful placement statistics and career resources.

## 🔮 Future Enhancements

* Email notifications for new job opportunities
* Automated resume analysis
* AI-based career recommendations
* Advanced placement analytics dashboard
* Online aptitude and coding tests
* Company-wise placement analytics
* Cloud deployment
* REST API integration
* Role-based access control improvements

## 👨‍💻 Developer

**Prajwal C N**

MCA Student
Presidency University, Bengaluru

## 📄 License

This project is developed for academic and educational purposes.
