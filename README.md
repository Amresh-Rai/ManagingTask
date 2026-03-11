# Task Manager Application

This is a lightweight Task Management web application built with Python and Flask. This project strictly follows MVC pattern requirements for creating, reading, updating, deleting, and searching task records.

## Assignment Objectives Met
1. **Create**: Ability to create records from the web front end.
2. **Read**: Ability to read records from the web front end.
3. **Update**: Ability to update records from the web front end.
4. **Delete**: Ability to delete records from the web front end.
5. **Search**: Ability to search records from the web front end.

## Data Structure
The application fulfills the requested data structure by capturing:
- Task Title
- Task Description
- Task Due Date
- Task Status ("Pending", "In Progress", or "Completed")
- Task Remarks
- Created On (Time Stamp generated automatically)
- Last Updated on (Time Stamp generated automatically)
- Created By (Name and Id of the user who created the task - entered manually during creation)
- Last Updated By (Name and Id of the user who created/updated the task - entered manually during creation/update)

## Technologies Used
*   **Backend**: Python, Flask, Flask-SQLAlchemy (for ORM), Flask-WTF (for form handling)
*   **Database**: SQLite (local File-based database)
*   **Frontend**: HTML, Jinja2 Templates, Tailwind CSS (via CDN)

## Project Structure (MVC)
*   `app.py`: Application initialization and configuration.
*   `models.py`: Database models (The **Model**).
*   `routes.py`: Endpoint definitions and business logic connecting views to data (The **Controller**).
*   `forms.py`: WTForms class definitions for structured data intake.
*   `templates/`: HTML Jinja2 templates for the UI (The **Views**).

## Installation and Execution Requirements

### 1. Requirements
Ensure you have Python installed on your system. 

### 2. Setup the Environment
It is highly recommended to run this within a Python virtual environment to avoid dependency conflicts. 

Open your terminal in this directory (`TaskManager`) and run the following commands:

**Create the Virtual Environment:**
```powershell
python -m venv venv
```

**Activate the Virtual Environment:**
```powershell
.\venv\Scripts\activate
```

### 3. Install Dependencies
While the virtual environment is active, install the required packages:
```powershell
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```powershell
python app.py
```

### 5. Access the Web App
Open your web browser and navigate to:
`http://127.0.0.1:5000/`
