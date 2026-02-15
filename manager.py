from database import SessionLocal, engine, Base
from models import User, Slot, Booking

# --- DATABASE SETUP ---
def init_db():
    '''Creating database based on models'''
    print('Creating database tables...')
    Base.metadata.create_all(bind=engine)
    print('Table created successfully: "booking.db" should now exist.')

# --- UTILITY: GET SESSION ---
def get_session():
    return SessionLocal()

# --- USER FUNCTIONS ---
def add_user(username: str, email: str, role: str='student'):
    db = get_session()
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f'Error! User with email {email} already exists.')

        new_user = User(username=username, email=email, role=role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f'User {new_user} created with ID {new_user.id}')
        return new_user

    except Exception as e:
        print(f'An error occured {e}')
        db.rollback()
    finally:
        db.close()

def get_user_by_email(email: str):
    db = get_session()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    return user

if __name__ == '__main__':
    init_db()