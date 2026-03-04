# JobSearch - Job Portal Application

A modern, responsive Job Portal application built with Django, featuring a clean user interface and interactive components.

## 🚀 Features

- **Job Listing & Details**: Dual-pane layout showing a list of jobs on the left and full details on the right.
- **Advanced Search**: Filter jobs by type (Job or Internship), location, or specific keywords.
- **Interactive UI**: Micro-animations on job cards and smooth transitions.
- **Login Modal**: Modern, centered login popup triggered by the "Apply Now" button with a blurred background (Glassmorphism).
- **Social Login Options**: Integrated UI for Google and LinkedIn login.
- **Combined Data Sources**: Displays jobs from both the Django admin database and static code-defined entries.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript
- **Database**: SQLite (SQL)
- **Design**: Premium Inter font, Blue theme, HSL tailored colors.

## 📦 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sony142004/job-portal.git
   cd job-portal
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   ```

3. **Install Django**:
   ```bash
   pip install django
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Open the browser**:
   Visit `http://127.0.0.1:8000/` to find your dream job!

## 📸 Preview

The portal features a premium blue design with interactive job cards. When selecting a job and clicking "Apply Now", a beautiful login popup appears to guide users forward.

---
Built with ❤️ by Sowmya
