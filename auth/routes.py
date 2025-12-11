from flask import Blueprint, render_template
auth_bp=Blueprint("auth",__name__)
@auth_bp.route("/login")
def login():
    username="Sarfraz"
    return render_template("home.html",name=username)