def test_add_user(client):
    response = client.post(
        "/auth/add",
        data={
            "username": "testuser",
            "email": "test@example.com"
        }
    )

    assert response.status_code == 200
    assert b"User added successfully" in response.data
