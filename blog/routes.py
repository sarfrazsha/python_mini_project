from flask import Blueprint,render_template,request
from models.post import Post

from extensions import db

blog_bp = Blueprint("blog", __name__)

@blog_bp.route('/post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        ptitle = request.form.get('title')
        pcontent = request.form.get('content')
        puser_id = request.form.get('user_id') 
        
        new_post = Post(title=ptitle, content=pcontent, user_id=puser_id)
        db.session.add(new_post)
        db.session.commit()
        return "Post created!"
    return render_template('add_post.html')