build:
	docker build -t extraction-service .

run:
	docker run --env-file .env -v $(PWD)/../file-storage/:/file-storage extraction-service python main.py --console "$(OPERATION)" "$(KEYWORD)" $(DAYS) "$(LOCATION)"
