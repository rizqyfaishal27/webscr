FROM python:3.6
MAINTAINER Rizqy Faishal "rizqyfaishal27@gmail.com"
ENV REFRESHED_AT 2019-04-13

RUN apt-get -yqq update

ADD . /data
WORKDIR /data

RUN unzip ./debs/chromedriver_linux64.zip
RUN cp chromedriver /usr/bin

RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf

RUN mkdir -p /screenshots
RUN pip install -r requirements.txt

CMD ["python", "script.py"]