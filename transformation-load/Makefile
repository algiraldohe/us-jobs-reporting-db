build:
	docker build -t transform-load-service .

create-network:
	docker network create database-network

clear-db:
	rm -rf $(pwd)/postgres_data/

run-db:
	docker run --name db --env-file .env.docker -v $(pwd)/postgres_data/:/var/lib/postgresql/data --network database-network postgres:14.1-alpine

run-migrations:
	docker run --env-file .env.docker --network database-network transform-load-service alembic upgrade head

run:
	docker run --env-file .env.docker --network database-network transform-load-service python main.py