from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username == username).count():
        print('Пользователь уже существует')
        sys.exit(0)

    password1 = getpass('Введите пароль')
    password2 = getpass('Введите повторно пароль')

    if not password1 == password2:
        print('Пароли разные!')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password=password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Создан пользователь с ID: {new_user.id}')