from app import create_app, db, bcrypt
from app.models.user import User

app = create_app()

with app.app_context():
    print("📁 Создание базы данных...")
    db.create_all()

    if not User.query.filter_by(username='admin').first():
        print("➕ Добавляю тестового пользователя...")
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        admin = User(username='admin', password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        print("✅ Пользователь admin создан: пароль 'admin123'")
    else:
        print("⚠️ Пользователь admin уже существует")

    print("🎉 База готова!")
