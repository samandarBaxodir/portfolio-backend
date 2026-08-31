from app.database import SessionLocal
from app.models.admin_user import AdminUser
from app.core.security import hash_password

db = SessionLocal()

username = input("Admin username kirit: ")
password = input("Admin parol kirit: ")

existing = db.query(AdminUser).filter(AdminUser.username == username).first()
if existing:
    print("Bu username allaqachon mavjud!")
else:
    new_admin = AdminUser(username=username, hashed_password=hash_password(password))
    db.add(new_admin)
    db.commit()
    print(f"Admin '{username}' muvaffaqiyatli yaratildi!")

db.close()