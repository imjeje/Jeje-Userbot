#==============×==============#
#      Created by: Alfa-Ex
#=========× Ayiin ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Jeje https://github.com/imjeje/Jeje-Userbot /home/jeje/ \
    && chmod 777 /home/jeje \
    && mkdir /home/jeje/bin/

COPY ./sample_config.env ./config.env* /home/jeje/

WORKDIR /home/jeje/

RUN pip install -r requirements.txt

CMD ["bash","start"]
