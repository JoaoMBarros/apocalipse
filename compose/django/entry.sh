#!/bin/bash

echo "Cria migrações"
python manage.py makemigrations sobreviventes
echo "============================="

echo "Cria tabelas"
python manage.py migrate
echo "============================="

echo "Roda servidor" 
python manage.py runserver 0.0.0.0:8000