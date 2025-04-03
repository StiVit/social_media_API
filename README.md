# Social Media API

This is a FastAPI-based social media API that allows users to create, read, update, and delete posts. It also includes user authentication and voting functionality.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Docker Implementation](#docker-implementation)
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

## Docker Implementation

This project includes Docker support for both development and production environments. It provides a `Dockerfile` to build the application image and two `docker-compose` files for running the application with PostgreSQL.

### Building the Docker Image

To build the Docker image, run the following command:

```bash
docker build -t social_media_api .
```

### Running the Application with Docker Compose

#### Development Environment

For development, use the `docker-compose-dev.yml` file. This setup includes the application and a PostgreSQL database.

1. Start the containers:
    ```bash
    docker-compose -f docker-compose-dev.yml up --build
    ```

2. The application will be available at `http://127.0.0.1:8000/docs`.

3. To stop the containers:
    ```bash
    docker-compose -f docker-compose-dev.yml down
    ```

#### Production Environment

For production, use the `docker-compose-prod.yml` file. This setup is optimized for production use.

1. Start the containers:
    ```bash
    docker-compose -f docker-compose-prod.yml up --build -d
    ```

2. To stop the containers:
    ```bash
    docker-compose -f docker-compose-prod.yml down
    ```

### Notes

- Ensure that the `.env` file is properly configured before running the application in Docker.
- The `docker-compose-dev.yml` file is tailored for local development with debugging enabled, while the `docker-compose-prod.yml` file is configured for production with optimizations and stricter settings.
- You can modify the `docker-compose` files to suit your specific requirements.
- Use `docker logs <container_name>` to view logs for debugging purposes.
- For database migrations, you can run:
    ```bash
    docker exec -it <app_container_name> alembic upgrade head
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