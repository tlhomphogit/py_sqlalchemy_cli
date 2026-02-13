from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

'''
engine: The actual physical connection to the bookings.db file.

SessionLocal: The tool to start a conversation with the database.

Base: The foundation the tables.

'''

# 1. Define the Database File Location
DATABASE_URL = 'sqlite:///bookings.db'

# 2. Create the Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)

# 3. Create the Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the Base Class
Base = declarative_base()

# --remove me