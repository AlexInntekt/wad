wad
Web Application Development
Project for school

Magazin online pentru piese auto.



Backend scris in 
Django 2.2
Python3.6


Instalare pe local:   
- se da:  
	 git clone https://github.com/AlexInntekt/wad


- Se face un mediu virtual python:
python3 -m venv .

- Se activeaza:  
pe unix/linux:  
source bin/activate   
iar pe windows:  
Scripts/activate  

- Se instaleaza dependintele:
pip3 install -r req/base.txt

- in bin/activate.bat se adauga:
export SECRET_KEY="aici-scrii-la-intamplare-o-parola"
export DJANGO_SETTINGS_MODULE="wad.settings.base"

- Se conecteaza la baza de date:
python3 src/manage.py migrate

- se ruleaza serverul pe local de test:
python3 src/manage.py runserver
