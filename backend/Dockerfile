FROM python:3.11

#ENV PYTHONUNBUFFERD=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
#RUN python manage.py collectstatic --no-input

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]