FROM nginx
EXPOSE 80
MAINTAINER Karthik
LABEL novacart page
COPY . /usr/share/nginx/html
