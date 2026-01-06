from models.user import User
from extensions import db


def test_create_post(client, app):
    with app.app_context():
        # Create user first
        user = User(username="author", email="author@test.com")
        db.session.add(user)
        db.session.commit()

        user_id = user.id

    response = client.post(
        "/blog/post",
        data={
            "title": "Test Post",
            "content": "This is a test post",
            "user_id": user_id
        }
    )

    assert response.status_code == 200
    assert b"Post created" in response.data
