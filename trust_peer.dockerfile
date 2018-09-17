FROM pful/python-ubuntu-xenial:3.6

RUN apt update -y && \
    apt install -y libgl1-mesa-dev

RUN pip install flask && \
	pip install PyQt5

COPY ./src /logchain

RUN mkdir /conf
WORKDIR /logchain

VOLUME ["/conf"]

RUN pip install netifaces
ENV PYTHONPATH /logchain

CMD ["python", "/logchain/launcher/logchain_launcher_for_trustpeer.py"]


