install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy is only pushing to ECR
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t cdfast .
	docker tag cdfast:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/cdfast:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/cdfast:latest
		
all: install lint test format deploy