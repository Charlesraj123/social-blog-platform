from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    admin_user = User.query.filter_by(username='admin').first()
    if admin_user is None:
        admin_user = User(username='admin', email='admin@example.com', is_admin=True)
        admin_user.set_password('admin123')
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
