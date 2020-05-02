FROM python:3.7.7-alpine
LABEL maintaner="quanlook@qq.com"
COPY . /www
WORKDIR /www
RUN pip install  redis flask  -i https://pypi.douban.com/simple 
EXPOSE 5000
CMD [ "python" , "server.py"]
