FROM balenalib/rpi-debian-python:latest
RUN install_packages build-essential python3 python3-pip python3-setuptools python3-venv python3-dev libffi-dev libssl-dev
RUN python3 --version
RUN pip3 install poetry
COPY . .
RUN poetry install --no-dev
EXPOSE 8000
CMD poetry run python3 services/camera-steam-server.py