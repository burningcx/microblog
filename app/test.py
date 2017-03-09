from app.models import User
from app import db


u = User()
u.username = 'admin'
u.email = 'admin@burning.com'
u.password = 'admin'
print(u.password_hash)
db.session.add(u)
db.session.commit()
