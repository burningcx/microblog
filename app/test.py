from app.models import User
from app import db


u = User()
u.username = 'admin1'
u.email = 'admin1@burning.com'
u.password = 'admin'
print(u.password_hash)
db.session.add(u)
db.session.commit()
