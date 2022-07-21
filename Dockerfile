#==============×==============#
#      Created by: Alfa-Ex
#=========× Sajiku ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Sajiku-Userbot https://github.com/Sajikuuu/Sajiku-Userbot /home/sajikuu/ \
    && chmod 777 /home/sajikuuserbot \
    && mkdir /home/sajikuu/bin/

COPY ./sample_config.env ./config.env* /home/sajikuu/

WORKDIR /home/sajikuu/

RUN pip install -r requirements.txt

CMD ["bash","start"]
