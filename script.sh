#!/bin/bash

python freelance/manage.py makemigrations
python freelance/manage.py migrate
python freelance/manage.py runserver 0.0.0.0:8000