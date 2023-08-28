echo "Start Extraction Process"
cd /Users/alejandrogiraldoh/Development/us-jobs-reporting-db/orchestration.sh
cd extraction && /usr/local/bin/docker run --env-file .env -v /file-storage/:/file-storage extraction-service touch hola.txt
echo "Finish Extraction Process"

# cd ..
# cd transformation-load
# make run

# Command to run extraction service
# python3 main.py --console "extract_jobs" "data engineering" 2 "Chicago, Illinois"
