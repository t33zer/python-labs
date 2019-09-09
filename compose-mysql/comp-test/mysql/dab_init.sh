#!/bin/bash

# Initialize MySQL database.
# ADD this file into the container via Dockerfile.
# Assuming you specify a VOLUME ["/var/lib/mysql"] or `-v /var/lib/mysql` on the `docker run` command…
# Once built, do e.g. `docker run your_image /path/to/docker-mysql-initialize.sh`
# Again, make sure MySQL is persisting data outside the container for this to have any effect.


# Start the MySQL daemon in the background.
# mkdir /var/lib/mysql/mysql-files
# chown mysql:mysql /var/lib/mysql/mysql-files
# chmod 750 /var/lib/mysql/mysql-files
ls -alh /var/lib/mysql
/usr/sbin/mysqld --initialize --user=mysql &
mysql_pid=$!

until mysqladmin ping >/dev/null 2>&1; do
  echo -n "."; sleep 0.2
done

# create the default database from the ADDed file.
mysql -uroot -p"root"< /tmp/db_init.sql

