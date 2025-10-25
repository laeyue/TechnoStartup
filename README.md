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
