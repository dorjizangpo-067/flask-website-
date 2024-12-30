from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template(template_name_or_list='login.html')


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/sign-up')
def signup():
    return "<h1>Signup</h1>"