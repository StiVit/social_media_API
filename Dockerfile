FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# It's very important not to forget to call the alembic upgrade command to build up the application database before running the app
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000