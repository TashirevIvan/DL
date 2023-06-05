FROM ubuntu:22.10
FROM python:3.8.16

COPY FastDepthCompletionCPU .

RUN apt-get update

RUN python3.8 -m venv FDC

RUN . FDC/bin/activate && pip3 install -r requirements.txt
RUN pip install opencv-python
RUN apt-get install -y libgl1-mesa-glx
COPY entrypoint.sh .
ADD . .
COPY test.py .
RUN chmod +x entrypoint.sh
ENTRYPOINT ./entrypoint.sh


