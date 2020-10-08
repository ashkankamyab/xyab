FROM ubuntu
LABEL maintener="ashkankamyab@gmail.com" \
        repository="https://github.com/ashkankamyab/xyab.git"\
        last_update="Sa 12. Sep 2020"


RUN apt-get update -qqq && apt-get update -qqqy
RUN apt-get install -qqy \
        locales \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3 \
        python3-pip \
        python3-dev


# TODO: Tor compatibility
#RUN ["/bin/sh", "-c", "sed", "-i", "-e", "/ControlPort/s/^#//", "/etc/tor/torrc.sample" ]
#RUN ["/bin/sh", "-c", "sed", "-i",  "-e", "/CookieAuthentication/s/^#//", "/etrc/tor/torrc.sample"]

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

WORKDIR /usr/src/app
COPY main.py ./
COPY arzyab.py ./
COPY cred.json ./
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
