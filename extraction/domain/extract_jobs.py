from infrastructure.us_jobs_service import USJobsService


def extract_jobs(request, storage_service) -> None:
    us_api_service = USJobsService()
    data = us_api_service.search_data(request)

    storage_service.save_data(data)

