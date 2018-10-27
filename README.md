virtualenv elb-app
source elb-app/bin/activate

pip install -r requirement.txt
gunicorn --workers 3 app:app -b 0.0.0.0:8088
