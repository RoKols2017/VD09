# 🖱️ Flask Clicker Game

Простое Flask-приложение с возможностью регистрации, входа в аккаунт и нажатия на кнопку-кликер.  
Количество кликов сохраняется на сервере и доступно только авторизованным пользователям.

## 🚀 Возможности

- Регистрация и авторизация пользователей
- Хэширование паролей (bcrypt)
- Подсчёт количества кликов
- Ограничение доступа: только авторизованные пользователи могут кликать
- Инструкция по деплою в общем UI-стиле

## 🔧 Установка

```bash
git clone https://github.com/yourusername/flask-clicker.git
cd flask-clicker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🛠 Создание базы данных

```bash
python create_db.py
```

Создаст SQLite базу и добавит тестового пользователя:

- Логин: **admin**
- Пароль: **admin123**

## ▶️ Запуск

```bash
python run.py
```

## 🌐 Деплой на PythonAnywhere

Зайди в раздел **/Deploy/** в приложении, чтобы увидеть пошаговую инструкцию по загрузке на PythonAnywhere:

- создание виртуального окружения
- загрузка файлов
- конфигурация WSGI
- перезапуск

Ссылка: `/deploy` (только для авторизованных пользователей)

## 🗂 Структура проекта

```
clicker_app/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── user.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── game_routes.py
│   ├── forms/
│   │   ├── login_form.py
│   │   └── register_form.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── deploy_instructions.html
├── run.py
├── create_db.py
├── config.py
├── requirements.txt
└── instance/
    └── config.py
```

## 🧠 Автор

**🧑‍💻 RoKols2017**😎

---
