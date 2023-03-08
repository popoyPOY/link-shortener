from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def log_out():
    return "<p>Log out</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign Up</p>"