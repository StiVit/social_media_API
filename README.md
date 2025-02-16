# Social Media API

This is a FastAPI-based social media API that allows users to create, read, update, and delete posts. It also includes user authentication and voting functionality.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Migrations](#database-migrations)
- [Contributing](#contributing)
- [License](#license)


## Installation

To install the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/social_media_API.git
    cd social_media_API
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the project, you need to configure the environment variables.

**Copy the template file to create a new `.env` file:**
```bash
cp .env.template .env
```

Set up all your environmental variables

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_USERNAME=
DATABASE_NAME=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=
DEBUG=True  # Set to False in production
```

## Running the Application

1. Running the database migration:

```bash
alembic upgrade head
```

2. Start the FastAPI application:

```bash
uvicorn app.main:app --reaload
```

The application will be available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Authentication
- `POST /auth/login` - Login into an existing user

### Users
- `POST /users/` - Create a user
- `GET /users/{user_id}` - Get user details

### Posts
- `GET /posts` - Get all posts
- `POST /posts` - Create a new post
- `GET /posts/{post_id}` - Get a specific post
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post

### Votes
- `POST /votes` - Vote on a post
- `DELETE /votes` - Remove a vote from a post

## Database Migrations

Alembic is used for handling database migrations in this project. Follow these steps to create and apply migrations:

### Creating a New Migration

1. **Generate a new migration script:**
    ```bash
    alembic revision --autogenerate -m "description_of_change"
    ```

    This command will create a new migration script in the `alembic/versions` directory.

### Applying the Migration

1. **Apply the migration to the database:**
    ```bash
    alembic upgrade head
    ```

    This command will apply the latest migration to your database.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.