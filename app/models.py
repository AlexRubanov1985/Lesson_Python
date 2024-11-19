import sqlalchemy as sa
from main import db, app


class User(db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    password = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    admin = sa.Column(sa.Boolean, default=False)


class Tovar(db.Model):
    __tablename__ = 'tovars'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    url_photo = sa.Column(sa.String(255), nullable=True)
    price = sa.Column(sa.Integer, nullable=False)
    ostatok=sa.Column(sa.Integer, default=0)


db.init_app(app)

with app.app_context():
    db.create_all()
