FROM python:3.12.7-slim-bullseye
COPY . .
RUN apt-get update
RUN apt-get -y install ffmpeg
RUN pip install -r requirements.txt
EXPOSE 50001
CMD ["python", "main.py"]