#!/bin/bash

user=$(echo -n "felix" | md5sum | grep -Eo "\w+")
password=$(echo -n "joergen" | md5sum | grep -Eo "\w+")
#query=$(sed s/USER/$user/g /share/db_init.sql | sed s/PASS/$password/g)
mysql -uroot -p"root" < /share/db_init.sql

