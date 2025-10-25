from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greenstamp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    certified_at = db.Column(db.DateTime, nullable=True)
    background_image = db.Column(db.String(500), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'certified_at': self.certified_at.isoformat() if self.certified_at else None
        }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    # Get all certified projects
    certified_projects = Project.query.filter_by(status='approved').all()
    return render_template('results.html', projects=certified_projects)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit_project', methods=['POST'])
def submit_project():
    try:
        data = request.get_json()
        
        # Create new project
        project = Project(
            name=data['name'],
            location=data['location'],
            description=data['description'],
            status='pending'
        )
        
        db.session.add(project)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Project submitted successfully! Our team will review it soon.',
            'project_id': project.id
        })
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error submitting project: {str(e)}'
        }), 400

@app.route('/api/projects')
def api_projects():
    """API endpoint to get all projects"""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@app.route('/api/projects/<int:project_id>')
def api_project(project_id):
    """API endpoint to get a specific project"""
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())

@app.route('/admin')
def admin():
    """Admin panel to manage projects"""
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('admin.html', projects=projects)

@app.route('/admin/approve/<int:project_id>')
def approve_project(project_id):
    """Approve a project"""
    project = Project.query.get_or_404(project_id)
    project.status = 'approved'
    project.certified_at = datetime.utcnow()
    db.session.commit()
    flash(f'Project "{project.name}" has been approved!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/reject/<int:project_id>')
def reject_project(project_id):
    """Reject a project"""
    project = Project.query.get_or_404(project_id)
    project.status = 'rejected'
    db.session.commit()
    flash(f'Project "{project.name}" has been rejected.', 'warning')
    return redirect(url_for('admin'))

def create_tables():
    """Initialize database tables and add sample data"""
    # Drop all tables first to handle schema changes
    db.drop_all()
    db.create_all()
    
    # Add some sample data
    sample_projects = [
        Project(
            name="Mangrove Restoration Initiative",
            location="Palawan, Philippines",
            description="This comprehensive project restores degraded mangrove forests along the coast, protecting vital coastal ecosystems and supporting local biodiversity. The initiative involves community participation and sustainable fishing practices.",
            status="approved",
            certified_at=datetime(2025, 3, 1),
            background_image="https://images.unsplash.com/photo-1544551763-46a013bb70d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80"
        ),
        Project(
            name="Solar Village Project",
            location="Cebu, Philippines",
            description="Provides renewable solar energy solutions to rural communities, significantly reducing carbon footprint while promoting sustainable development. The project includes education programs and maintenance training for local residents.",
            status="approved",
            certified_at=datetime(2025, 4, 1),
            background_image="https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?ixlib=rb-4.0.3&auto=format&fit=crop&w=2074&q=80"
        ),
        Project(
            name="Community Reforestation Program",
            location="Bukidnon, Philippines",
            description="Empowers local farmers to plant native tree species, restoring degraded upland areas and supporting watershed health. The program includes sustainable agriculture training and biodiversity conservation education.",
            status="approved",
            certified_at=datetime(2025, 2, 1),
            background_image="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=2071&q=80"
        ),
        Project(
            name="Urban Green Spaces Initiative",
            location="Metro Manila, Philippines",
            description="Transforms urban areas into green spaces through vertical gardens, rooftop farming, and community parks. This project improves air quality and provides fresh produce to urban communities while promoting environmental awareness.",
            status="approved",
            certified_at=datetime(2025, 1, 1),
            background_image="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80"
        ),
        Project(
            name="Marine Conservation Program",
            location="Bohol, Philippines",
            description="Protects marine ecosystems through coral reef restoration, sustainable fishing practices, and marine education programs. The initiative involves local fishermen and marine biologists working together to preserve ocean biodiversity.",
            status="approved",
            certified_at=datetime(2024, 12, 1),
            background_image="https://images.unsplash.com/photo-1559827260-dc66d52bef19?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80"
        ),
        Project(
            name="Waste-to-Energy Facility",
            location="Davao, Philippines",
            description="Converts organic waste into clean energy through innovative biogas technology. The facility serves as a model for sustainable waste management while providing renewable energy to local communities and reducing landfill dependency.",
            status="approved",
            certified_at=datetime(2024, 11, 1),
            background_image="https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80"
        )
    ]
    
    for project in sample_projects:
        db.session.add(project)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
