FROM python:3.9-slim
RUN apt-get update \
  && apt-get install -y --no-install-recommends
RUN python -m venv /opt/venv
RUN pip3 install --upgrade pip
WORKDIR /develop/
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY animals.py .


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"
CMD python animals.py