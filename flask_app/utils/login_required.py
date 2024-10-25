from flask import session , redirect, url_for

def login_required():
    if not session.get('user', False):
        return redirect(url_for('auth.login'))