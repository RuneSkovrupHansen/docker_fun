FROM ubuntu
ENV dir="/opt/censor"
COPY requirements.txt $dir/requirements.txt
WORKDIR $dir
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt
RUN python3 -m spacy download en
COPY censor.py $dir
