FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /Users/user/PycharmProjects/untitled1 
RUN pip install --upgrade pip
RUN pip install django
RUN pip install xmltodict
RUN pip install requests
RUN python -m pip install Pillow
COPY . /Users/user/PycharmProjects/untitled1
EXPOSE 8000
CMD ["python3.6", "manage.py", "runserver"]