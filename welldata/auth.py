from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import current_user, login_user

from .models import User
from .forms import LoginForm


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ User login page. """

    # Bypass login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))
    login_form = LoginForm(request.form)

    # POST: Create user and redirect them to the dashboard
    if request.method == 'POST':
        if login_form.validate():
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(username=username).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    return redirect(url_for('main_bp.dashboard'))
        flash('Invalid username password pair.')
        return redirect(url_for('auth_bp.login'))

    # GET: Serve login page
    return render_template(
        'login.html',
        form = LoginForm(),
        title = 'Login',
    )


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'logout'
