install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

deploy:
	#echo "deploys goes here"

all: install lint test format deploy