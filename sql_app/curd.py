from . import models, schemas
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.CreateUserRequest):
    fake_password_hashed = user.password + "fake"
    db_user = models.User(email=user.email, hashed_password=fake_password_hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user