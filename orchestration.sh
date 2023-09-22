cd /Users/alejandrogiraldoh/Development/us-jobs-reporting-db
cd extraction
make build
make run OPERATION="extract_jobs"  KEYWORD="data engineering" DAYS=2 LOCATION="Chicago, Illinois" GRADE=7
cd ..
cd transformation-load
make run OPERATION="save_jobs"
