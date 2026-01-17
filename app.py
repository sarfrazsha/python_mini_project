import os, sys
import time
from sqlalchemy.exc import OperationalError

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from extensions import db
from blog.routes import blog_bp
from auth.routes import auth_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+pymysql://root:1234@db:3306/flask_db"  # <-- Use 'db' not 'localhost'
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from models.user import User  
    from models.post import Post 

    # 🔹 Wait for MySQL to be ready
    with app.app_context():
        for i in range(10):  # Retry 10 times
            try:
                db.create_all()
                print("✅ Database connected!")
                break
            except OperationalError:
                print("⏳ Waiting for database...")
                time.sleep(3)  # Wait 3 seconds before retry

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(blog_bp, url_prefix="/blog")

    @app.route("/")
    def index():
        return "Ok"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")  # <-- host=0.0.0.0 for Docker
