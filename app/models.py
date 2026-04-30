from . import db
from werkzeug.security import generate_password_hash, check_password_hash


# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")  # admin / user

    # password hash
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # password check
    def check_password(self, password):
        return check_password_hash(self.password, password)


# TASK MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    # user link
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)