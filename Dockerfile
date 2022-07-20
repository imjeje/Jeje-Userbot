#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Sajiku-Userbot https://github.com/Sajikuuu/Sajiku-Userbot /home/sajikuuserbot/ \
    && chmod 777 /home/sajikuuserbot \
    && mkdir /home/sajikuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/sajikuuserbot/

WORKDIR /home/sajikuuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
