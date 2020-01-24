FROM python:3.7
ADD . /todo-lists
WORKDIR /todo-lists
RUN pip install -r requirements.txt
CMD python app.py