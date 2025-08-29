FROM python:3.12.1


WORKDIR /app


COPY requirements.txt .
COPY setup.py .

RUN pip install  -r requirements.txt

COPY . .


EXPOSE 8000


CMD ["echo", "done"]







