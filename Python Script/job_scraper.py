from serpapi import GoogleSearch

params = {
  "engine": "google_jobs",
  "q": "Computer Science",
  "ltype": "1", # remote
  "hl": "en", # english speaking
  "chips": "date_posted:week,", # posted in the last week
  "api_key": "key"
}

search = GoogleSearch(params)
results = search.get_dict()
job_results = results["jobs_results"]

with open("job_results.txt", "w") as output_file:
    for job in job_results:

        listing_params = {
            "engine": "google_jobs_listing",
            "q": job['job_id'],
            "api_key": "key"
        }
        listing_info = GoogleSearch(listing_params)
        listing_results = listing_info.get_dict()
        listing_link = listing_results['search_metadata']['google_jobs_listing_url']

        job_info = "%s\nCompany: %s\nLocation: %s\n%s\n" \
                    % (job['title'], job['company_name'], job['location'], job['via'])
        for extra in job['extensions']:
            job_info += "%s | " % extra
        job_info = job_info[:-3]
        job_info += "\n%s\n\n" % listing_link
        output_file.write(job_info)