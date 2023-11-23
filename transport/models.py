from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Date,
    Enum,
    Text,
    Boolean,
    FLOAT,
)

from transport.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    _password = Column("password", String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()