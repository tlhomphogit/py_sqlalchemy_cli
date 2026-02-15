from database import engine, Base
from models import User, Slot, Booking

def init_db():
    '''
    Creating database based on models
    '''

    print('Creating database tables...')

    Base.metadata.create_all(bind=engine)

    print('Table created successfully: "booking.db" should now exi exist.')

if __name__ == '__main__':
    init_db()