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

run:
	clear
	fastapi dev apicultura/main.py

run-api:
	clear
	@poetry run uvicorn apicultura.main:app --host 0.0.0.0 --port ${PORT} --reload

lint:
	@echo "Checking code style..."
	poetry run ruff check . 

style:
	@echo "Applying code style..."
	poetry run isort .
	poetry run ruff check --select I --fix
	poetry run ruff format

post_test:
	poetry run coverage report -m
	poetry run coverage html

unit:
	clear
	@echo "Running unit tests..."
	poetry run coverage run -m pytest apicultura -x

test:
	clear
	@make lint
	@make unit

build:
	clear 
	@echo "Building docker image..."
	@docker buildx build -t ${USER}/APIcultura .

run-container:
	clear
	@echo "Running APIcultura container..."
	@docker run --env-file=.env ${USER}/APIcultura

db: 
	docker compose up -d

db-stop:
	docker compose down

clean:
	docker system prune -y

revision:
	poetry run alembic revision -m ${M} --autogenerate

migrate:
	poetry run alembic upgrade head