FROM ubuntu:17.04
MAINTAINER ome-devel@lists.openmicroscopy.org

# Update the repository sources list and install packages
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y \
    sudo \
    gzip \
    curl \
    git \
    apache2 \
    python \
    python-setuptools \
    python-pip \
    python-dev \
    libxml2-dev \
    libxslt-dev \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    libapache2-mod-wsgi \
    postgresql \ 
    postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

#=======================
# ROOT SPACE FROM HERE
#=======================

# Global install packages
RUN pip install \
    virtualenv

# Add configurations for apache
ADD omero-qa.conf /etc/httpd/conf.d/omero-qa.conf
# AD D omero-qa /etc/init.d/

# Add apache config to the etc foldßer
ADD docker/omero-qa.conf /etc/apache2/sites-enabled/qa.conf

# Init postqres database
RUN psql -c "CREATE USER qa_user WITH PASSWORD 'ome';"
RUN createdb qa_database -O qa_user

# Expose apache.
EXPOSE 80

# Add a user with default dir and ensure bash usage
RUN useradd -ms /bin/bash hudson

#=======================
# HUDSON SPACE FROM HERE
#=======================

# Set the working directory for docker
WORKDIR /home/hudson

# Make a directory to hold qa websites and virtual environments
RUN mkdir -p web \
    && mkdir -p virtual

#=======================
# Virtualenv setup
#=======================

# Create virtualenv enviorments
RUN virtualenv virtual/qa \
    && virtualenv virtual/qa_uploader

# Activate and obtain pip packages for qa and then leave vm
RUN source virtual/qa/bin/activate \
    && pip install \
    wheel \
    cython \
    lxml \
    matplotlib \
    numpy \
    pillow \
    geoip2 \
    psycopg2 \
    django-auth-ldap \
    django==1.4.2 \
    && deactivate

# Activate, obtain pip packages for qa_uploader and then leave vm
RUN source virtual/qa_uploader/bin/activate \
    && pip install \
    wheel \
    cython \
    lxml \
    matplotlib \
    numpy \
    pillow \
    geoip2 \
    psycopg2 \
    django-auth-ldap \
    django==1.4.2 \
    && deactivate

#=======================
# Web setup
#=======================

# Clone first version of omero qa to location
RUN cd web && \ 
    git clone -b master https://github.com/rgozim/qa.git qa \
    git clone -b fine_uploader_master https://github.com/rgozim/qa.git qa_uploader \
    && cd ..

# Download geoip data things
RUN curl http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \
	| gunzip > web/GeoLiteCity.dat &&\
	curl http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz \
	| gunzip > web/GeoIP.dat

# Copy the geo files to their each qa project
RUN cp GeoLiteCity.dat web/qa/GeoLiteCity.dat \
    && cp GeoLiteCity.dat web/qa_uploader/GeoLiteCity.dat \
    && rm GeoLiteCity.dat
RUN cp GeoIP.dat web/qa/GeoIP.dat \ 
    && cp GeoIP.dat web/qa_uploader/GeoIP.dat \
    && rm GeoIP.dat

# Add settings.py and initial_data2.json to the project
ADD settings.py web
ADD initial_data2.json web

# Copt the files to the web projects
RUN cp web/settings.py web/qa/omero_qa/settings.py \
    && web/settings.py web/qa_uploader/omero_qa/settings.py \
    && rm settings.py

RUN cp initial_data2.json web/qa/omero_qa/initial_data2.py \
    && web/settings.py web/qa_uploader/omero_qa/initial_data2.py \
    && rm initial_data2.py

# Add these files to our user
# ADD docker/run.sh develop/

# Create a persistant storage for apache
VOLUME ["/home/hudson/ome/apache_repo", "/var/lib/pgsql/9.6/data"]

# Set the user with docker
USER hudson



# Run the init script of acaphe2
# https://serverfault.com/a/608619
# RUN source /etc/apache2/envvars

#RUN /home/hudson/qa-virtualenv/bin/python /home/hudson/qa/manage.py \
#	collectstatic --noinput
# CMD develop/run.sh