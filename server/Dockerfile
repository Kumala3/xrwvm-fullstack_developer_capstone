FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYCODE 1

ENV APP=/APP

WORKDIR /home/src/app

COPY requirements.txt /home/src/app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /home/src/app/

RUN chmod +x /home/src/app/entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/home/src/app/entrypoint.sh" ]

CMD ["gunicorn", "--bind" ":8000", "--workers", "3", "djangoproj.wsgi"]
