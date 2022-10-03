install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello test_*.py

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py 

refactor: format lint

deploy:
	#echo "deploys goes here"

all: install lint test format deploy