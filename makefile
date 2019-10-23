venv:
	virtualenv -p python3 venv

deps:
	./venv/bin/pip3 install -r requirements.txt

test:
	./venv/bin/python para_test.py
