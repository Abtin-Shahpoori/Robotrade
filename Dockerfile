FROM ubuntu
LABEL "Version"="1.0.0"
WORKDIR /home/robotrade

RUN useradd trader
# Test run
RUN echo "WHAT"

# Set Secret_key
ENV SECRET_KEY="3e345f87b33fc12d92737d92d036b05e9aa5b064b8b5668d4729e57b45d38324"

# environment variable
ENV FLASK_APP=app.py

# Installing python 
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv

#Installing packages
COPY requirements.txt requirements.txt
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt
RUN .venv/bin/pip install gunicorn

# Copying files to their places
COPY app app
COPY bots bots
COPY app.db config.py bot_template.py boot.sh ./
COPY migrations migrations

# giving accsess to execute boot
RUN chmod +x boot.sh

# Setting up user
RUN chown -R trader:trader ./
USER trader

# final configurations
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
