from functools import wraps

from flask import flash, redirect, url_for, current_app
from flask_login import current_user


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):

        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()

        elif not current_user.is_admin:
            flash("Это для админов")
            return redirect(url_for("news.index"))

        return func(*args, **kwargs)
    return decorated_view