import sqlalchemy as sa
import sqlalchemy.orm as orm
from main import db

class User(db.Model):
        __tablename__ = 'users'
        id = sa.Column(sa.Integer, primary_key=True)
        name = sa.Column(sa.String(255), nullable=True, unique=True, index=True)
        password = sa.Column(sa.String(255), nullable=False)
        # name2=sa.Column(sa.)