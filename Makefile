PORT=8000

setup:
	clear
	@pip install -U pip setuptools poetry

dependencies:
	clear
	@make setup
	@poetry run pip install -U pip
	@POETRY INSTALL --no-root

update:
	@poetry update

lint:
	clear
	@echo "Checking code style..."
	ruff check . && ruff check . --diff

format:
	@echo "Applying code style..."
	ruff check . --fix && ruff format .'

run:
	clear
	fastapi dev apicultura/main.py

run-api:
	clear
	@poetry run uvicorn apicultura.main:app --host 0.0.0.0 -- port ${PORT} --reload

pre_test:
	task lint || task format

post_test:
	poetry run coverage report -m
	poetry run coverage html

unit:
	clear
	@echo "Running unit tests..."
	poetry run coverage run -m pytest apicultura -vv

test:
	clear
	make pre_test
	make test
	make post_test

build:
	clear 
	@echo "Building docker image..."
	@docker buildx build -t asolheiro/APIcultura .

run-container:
	clear
	@echo "Running APIcultura container..."
	@docker run --env-file=.env asolheiro/APIcultura

db: 
	docker compose up -d

db-stop:
	docker compose down

clean:
	docker system prune -y