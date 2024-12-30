from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template(template_name_or_list="home.html")

@views.route("/todo-list")
def todo_list():
    return render_template(template_name_or_list="todo_list.html")

