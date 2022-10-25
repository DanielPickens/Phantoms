from python:3

RUN apt-get update && apt-get -y install --no-install-recommends \
   

RUN pip3 install pygame


CMD ["python3", "pygame"]
