import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from flask import Flask
from extensions import db
from blog.routes import blog_bp
from auth.routes import auth_bp
def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://root:1234@localhost:3306/flask_db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from models.user import User  
    from models.post import Post 

    
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(blog_bp,url_prefix="/blog")

    @app.route("/")
    def index():
        return "Ok"
    return app
if __name__=="__main__":
    app=create_app()
    app.run(debug=True) 
    