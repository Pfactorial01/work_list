FROM python:3.9
WORKDIR ./
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py

RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]