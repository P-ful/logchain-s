FROM pful/python-ubuntu-xenial:3.6

RUN apt update 
RUN apt install -y libgl1-mesa-dev

RUN pip install flask & \
	pip install PyQt5

RUN git clone --branch 0.1 https://github.com/P-ful/logchain-s.git /logchain

RUN mkdir /conf
WORKDIR /logchain

VOLUME ["/conf"]

RUN pip install netifaces
ENV PYTHONPATH /logchain

CMD ["python", "/logchain/launcher/logchain_launcher_for_genericpeer_restapi_node.py"]


