from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# 1. The User Table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    role = Column(String, default='student')
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    slots = relationship('Slot', back_populates='volunteer')
    bookings = relationship('Booking', back_populates='student')

# 2. The Slot Table
class Slot(Base):
    __tablename__ = 'slot'

    id = Column(Integer, primary_key=True, index=True)
    volunteer_id = Column(Integer, ForeignKey('users.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    is_booked = Column(Boolean, default=False)

    # Relationships
    volunteer = relationship('User', back_populates=('slots'))
    booking = relationship('Booking', back_populates='slot')

# 3. The Booking Table
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey('slot.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    google_event_id = Column(String, nullable=True)
    booked_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    slot = relationship('Slot', back_populates='booking')
    student = relationship('Users', back_populates='bookings')

