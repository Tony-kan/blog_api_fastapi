from core.user.models import User


def test_create_user():
    user = User(username="user", email="user@gmail.com", hashed_password="password")
    assert user.username == "user"
    assert user.email == "user@gmail.com"
    assert user.hashed_password == "password"
