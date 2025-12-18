from flask import Blueprint,render_template,request
from models.user import User
from extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        uname = request.form.get('username')
        uemail = request.form.get('email')
        
        new_user = User(username=uname, email=uemail)
        db.session.add(new_user)
        db.session.commit()
        return "User added successfully!"
    return render_template('add_user.html')