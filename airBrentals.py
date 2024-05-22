from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("")

# Prepare the Actor input
run_input = {
    "locationQuery": "Lake Blackshear, GA",
    "maxListings": 100,
    "startUrls": [],
    "includeReviews": False,
    "maxReviews": 10,
    "calendarMonths": 0,
    "addMoreHostInfo": False,
    "currency": "USD",
    "checkIn": "2024-09-22",
    "checkOut": "2024-09-21",
    "limitPoints": 10,
}

# Run the Actor and wait for it to finish
run = client.actor("GsNzxEKzE2vQ5d9HN").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

