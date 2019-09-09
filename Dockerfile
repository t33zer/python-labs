FROM richarvey/nginx-php-fpm
MAINTAINER t33

RUN mkdir /prerun

ADD ./2nd-lab /shared
 
