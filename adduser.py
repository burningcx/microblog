from app.models import User
from app import db


u = User(username='admin', email='admin@burning.com', password='admin')
print(u.password_hash)
db.session.add(u)
u = User(username='admin1', email='admin1@burning.com', password='admin')
print(u.password_hash)
db.session.add(u)
db.session.commit()
