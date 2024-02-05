from domain.base import db
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(db.UUID, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)