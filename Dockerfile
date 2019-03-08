FROM ubuntu
RUN  apt-get update \
     && apt-get install -y wget 
Run  apt-get install -y python 
Run  wget download https://bootstrap.pypa.io/get-pip.py 
Run  python get-pip.py 