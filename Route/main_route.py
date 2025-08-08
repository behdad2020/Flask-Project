from flask import Blueprint , request , jsonify
from Model.users import db , User
from App import bcrypt

main = Blueprint('main' , __name__)

@main.route('/create_db')
def create_db():
    db.create_all()
    return 'Database tables created'


@main.route('/register' , methods = ['POST'])
def register():
    data = request.get_json()
    common_fields = {
        'fullName': data['fullName'],
        'email': data['email'],
        'phone': data['phone'],
        'userType': data['userType'],
        'university': data['university'],
        'fieldOfStudy': data['fieldOfStudy'],
    }

    if data['userType'] == 'domestic':
        if data['password'] == data['confirmPassword']:
            common_fields['country'] = 'IRAN'
            common_fields['passportNumber'] = 'IRANPassportnumber'
            common_fields['password'] = bcrypt.generate_password_hash(data['password'])
    elif data['userType'] == 'international':
        if data['password'] == data['confirmPassword']:
            common_fields['country'] = data['country']
            common_fields['passportNumber'] = data['passportNumber']
            common_fields['password'] = bcrypt.generate_password_hash(data['password'])
    else:
        return jsonify({'error': 'Invalid user type'}), 400
    
    try:
        user = User(**common_fields)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}) , 500
    
    return jsonify({'message': 'User registered successfully'}) , 201