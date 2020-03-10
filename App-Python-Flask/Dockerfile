FROM python:3.6
WORKDIR /app_back

COPY ./requirements.txt /app_back/requirements.txt

RUN pip install -r requirements.txt

COPY . /app_back

#ENTRYPOINT [ "python" ]
EXPOSE 5000
CMD ["python",  "-m", "src.main" ]