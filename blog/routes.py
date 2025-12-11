from flask import Blueprint, render_template
blog_bp=Blueprint("blog",__name__)
@blog_bp.route("/login")
def login():
    username="Amir"
    return render_template("home.html",name=username)