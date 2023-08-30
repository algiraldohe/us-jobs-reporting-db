from infrastructure.us_jobs_service import USJobsService


def extract_jobs(request, storage_service) -> None:
    us_api_service = USJobsService()
    data = us_api_service.search_data(request)
    # Here we should implement a pagination until not getting more
    # results and storing any files that should be loaded in the DW.

    # request["Page"] = 1 while ... until "SearchResultCount" == 0
    # storage_service.save_data(data, page=request["Page"])
    storage_service.save_data(data)

