dev-up:
	docker-compose -f docker-compose.dev.yml up

dev-clear:
	docker-compose -f docker-compose.dev.yml down -v
