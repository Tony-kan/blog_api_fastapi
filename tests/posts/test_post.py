from core.post.models import Post
from core.user.models import User


def test_create_post():
    post = Post(title = "My first post", content = "This is my 1st post")
    assert post.title == "My first post"
    assert post.content == "This is my 1st post"
    
    
def test_user_posts_relationship():
    user = User(username = "user", email = "user@gmail.com", hashed_password = "password")
    post = Post(title = "My first post", content = "This is my 1st post")
    assert post.author == user
