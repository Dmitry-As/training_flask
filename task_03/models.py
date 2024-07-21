from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    usersurname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)


    def set_passwd(self, passwd: str):
        self.password = generate_password_hash(passwd, method='pbkdf2:sha512')
        
    
    def check_passwd(self, passwd: str):
        return check_password_hash(self.psw, passwd)


    def write_data(self):
        db.session.add(self)
        db.session.commit()
        
    
    def __repr__(self):
        return f'User({self.username}, {self.usersurname}, {self.email})'