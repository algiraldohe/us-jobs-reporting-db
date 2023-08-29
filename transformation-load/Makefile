build:
	docker build -t transform-load-service .

create-network:
	docker network create database-network

clear-db:
	rm -rf $(PWD)/postgres_data/

restart-db:
	docker rm db
	docker network rm database-network

run-db:
	docker run --name db --env-file .env.docker -v $(PWD)/postgres_data/:/var/lib/postgresql/data --network database-network -p 5432:5432  postgres:14.1-alpine

create-migrations:
	docker run --env-file .env.docker --network database-network transform-load-service alembic revision --autogenerate -m "$(MESSAGE)"

run-migrations:
	docker run --env-file .env.docker --network database-network transform-load-service alembic upgrade head

run:
	docker run --env-file .env.docker -v $(PWD)/../file-storage/:/file-storage --network database-network transform-load-service python main.py --console "$(OPERATION)"
