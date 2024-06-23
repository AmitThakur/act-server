# Start from the official Python base image.
FROM python:3.11

# Set the current working directory to /code (inside the container).
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/app

#
CMD ["fastapi", "run", "app/main.py", "--port", "80"]