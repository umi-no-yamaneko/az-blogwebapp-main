FROM python:3.9.8
WORKDIR /opt/build
ADD requirements.txt /opt/build/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install Flask==2.1.0
RUN pip install MarkupSafe==2.0.1

