## <a name="description">Project overview: Blog Api </a>

A RESTful API using FastAPI, Postgres, Redis, and Docker, featuring:
Custom JWT authentication ,
User management ,
Blog CRUD operations ,
Comment management ,
Ensuring secure and scalable blog management

## <a name="tech-stack"> Tech Stack *  </a>
- FastAPI (Backend)
- Postgres (Database)
- Redis (Caching)
- Docker (Containerization)
- Custom JWT Authentication

## <a name="features"> Features</a>

    User Management

    Blog CRUD Operations

    Comment Management

    Password Reset

    Refresh Tokens

## <a name="endpoints"> API EndPoints</a>
### auth Endpoints
   - POST /register - Register a new user
   - POST /login - Login a user
   - GET /profile - Retrieve user profile
   - PATCH /profile - Update user profile
   - POST /password/reset - Reset password

### Blog Endpoints
   - POST /posts - Create a new blog post
   - GET /posts - Retrieve all blog posts
   - GET /posts/{id} - Retrieve a blog post by ID
   - PATCH /posts/{id} - Update a blog post
   - DELETE /posts/{id} - Delete a blog post

### Comment Endpoints
   - POST /comments - Create a new comment
   - GET /comments - Retrieve all comments
   - GET /comments/{id} - Retrieve a comment by ID
   - PATCH /comments/{id} - Update a comment
   - DELETE /comments/{id} - Delete a comment

