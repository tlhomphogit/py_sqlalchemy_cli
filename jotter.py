# ---------------------------------------------------------- CONNECT TO SQLITE -

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the Database File Location
DATABASE_URL = 'sqlite\\\bookings.db'

# Create the Engine
engine = create_engine(DATABASE_URL, connect_args=('check_same_thread': False)

# Create the Session Factory
SessionLocal = sessionmaker(autocconect=False, authoflush=False, bind=engine)

# Create the Base Class
Base = declarative_base()

# ------------------------------------------------------------------------------

