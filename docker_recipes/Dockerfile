FROM python:3.11

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

#build requirements file via Makefile and install
#install py dep
RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 8888
