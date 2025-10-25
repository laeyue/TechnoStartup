# Green Stamp Flask Application

A Flask web application for managing environmental project certifications with a modern, responsive design.

## Features

- **Project Management**: Submit, review, and approve environmental projects
- **Admin Panel**: Manage project submissions and approvals
- **Modern UI**: Responsive design with professional styling
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **API Endpoints**: RESTful API for project data

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Pages

- **Home** (`/`): Landing page with project overview
- **Projects** (`/projects`): View all certified projects
- **Register** (`/register`): Submit new projects for certification
- **Admin** (`/admin`): Manage project submissions and approvals

## API Endpoints

- `GET /api/projects` - Get all projects
- `GET /api/projects/<id>` - Get specific project
- `POST /submit_project` - Submit new project

## Database

The application uses SQLite with the following model:

- **Project**: Stores project information including name, location, description, and certification status

## Admin Features

- View all submitted projects
- Approve or reject projects
- Track certification dates
- Manage project status

## Development

To run in development mode:

```bash
export FLASK_ENV=development
python app.py
```

This will enable debug mode and auto-reload on file changes.



## Preview

Home
<img width="1919" height="942" alt="image" src="https://github.com/user-attachments/assets/7150bf85-67c8-46e8-b4b0-2cf399a1db5b" />
Projects
<img width="1919" height="941" alt="image" src="https://github.com/user-attachments/assets/4eb87144-b671-4c89-ab05-4492cd582e8d" />
Registration
<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/c4f62d0c-0a3b-45a0-8c24-b63a3699eb1d" />
Admin Panel
<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/5aa44f8c-dd87-4552-bb63-e1f11e82d5dc" />




