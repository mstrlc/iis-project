
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Time,
    Date,
    Enum,
    Text,
    Boolean,
    Float,
)
import datetime

from transport.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

lines_stops = db.Table('LineStop',
                    Column('line_id', Integer, ForeignKey('lines.id'), primary_key = True),
                    Column('stop_id', Integer, ForeignKey('stops.id'), primary_key = True),
                    Column('time_from_start', Time, nullable=False, default=datetime.datetime.min),
                    Column('order', Integer, nullable=False, default=0),
                    )


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    deleted = Column(Boolean, default=False)
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
    latitude = Column(String(20), nullable=False)
    longitude = Column(String(20), nullable=False)
    deleted = Column(Boolean, default=False)
    stop_lines = relationship('Line', secondary=lines_stops, backref='stops')

    def save(self):
        db.session.expunge_all()
        db.session.add(self)
        db.session.commit()
        db.session.expunge_all()

class Line(db.Model):
    __tablename__='lines'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    connections = relationship('Connection', backref='lines')
    deleted = Column(Boolean, default=False)
    line_stops = relationship('Stop', secondary=lines_stops, backref='lines')

    def save(self):
        db.session.expunge_all()
        db.session.add(self)
        db.session.commit()
        db.session.expunge_all()

class Vehicle(db.Model):
    __tablename__='vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(100), nullable=False)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    specs = Column(String(150), nullable=False)
    status = Column(String(100), nullable=False)
    deleted = Column(Boolean, default=False)
    connections = relationship('Connection', backref='vehicles')

    def save(self):
        db.session.expunge_all()
        db.session.add(self)
        db.session.commit()
        db.session.expunge_all()

class Connection(db.Model):
    __tablename__='connections'
    id = Column(Integer, primary_key=True)
    time = Column(Time, nullable=False)
    direction = Column(String(20), nullable=False)
    days_of_week = Column(String(100), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    deleted = Column(Boolean, default=False)
    line_id = Column(Integer, ForeignKey('lines.id'), nullable=False)

class Maintenance(db.Model):
    __tablename__='maintenance'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    description = Column(Text(2048), nullable=False)
    deleted = Column(Boolean, default=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)