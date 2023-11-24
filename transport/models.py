
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
    Float,
)

from transport.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

line_stops = db.Table('LineStop',
                    Column('line_id', Integer, ForeignKey('lines.id'), primary_key = True),
                    Column('stop_id', Integer, ForeignKey('stops.id'), primary_key = True),
                    Column('time_from_start', DateTime, nullable=False),
                    Column('order', Integer, nullable=False)
                    )

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

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def save(self):
        db.session.expunge_all()
        db.session.add(self)
        db.session.commit()
        db.session.expunge_all()

class Stop(db.Model):
    __tablename__='stops'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class Line(db.Model):
    __tablename__='lines'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    connections = relationship('Connection', backref='lines')
    line_stops = relationship('Stop', secondary=line_stops, backref='lines')

class Vehicle(db.Model):
    __tablename__='vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(100), nullable=False)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    specs = Column(String(150), nullable=False)
    connections = relationship('Connection', backref='vehicles')

class Connection(db.Model):
    __tablename__='connections'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    direction = Column(String(20), nullable=False)
    days_of_week = Column(String(100), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    line_id = Column(Integer, ForeignKey('lines.id'), nullable=False)

class Maintenance(db.Model):
    __tablename__='maintenance'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)