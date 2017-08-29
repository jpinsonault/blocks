FROM python:3
RUN pip3 install pygame
ADD . /blocks
WORKDIR /blocks
CMD [ "python3", "-u", "./main.py" ]
