import os
from datetime import datetime, timedelta
from apify_client import ApifyClient
from Rental import Rental

class airBrentals:

    def __init__(self, lat, lon, api_key):
        self.lat = float(lat)
        self.lon = float(lon)
        self.api_key = api_key
        self.rentals = []

    def get_local_listings(self, locationToQuery) -> []:
        # Initialize the ApifyClient with your API token
        client = ApifyClient(self.api_key)

        checkin = datetime.today()+timedelta(days=90)
        checkout = checkin + timedelta(days=1)

        # Prepare the Actor input
        run_input = {
            "locationQuery": locationToQuery,
            "maxListings": 100,
            "startUrls": [],
            "includeReviews": False,
            "maxReviews": 10,
            "calendarMonths": 0,
            "addMoreHostInfo": False,
            "currency": "USD",
            "checkIn": checkin.strftime('%Y-%m-%d'),
            "checkOut": checkout.strftime('%Y-%m-%d'),
            "limitPoints": 10,
        }

        # Run the Actor and wait for it to finish
        run = client.actor("GsNzxEKzE2vQ5d9HN").call(run_input=run_input)

        # Fetch and print Actor results from the run's dataset (if there are any)
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            print(item)
            rental = Rental(
                name=item["name"],
                url=item["url"],
                address=item["address"],
                lat=item["location"]["lat"],
                lng=item["location"]["lng"]
            )

            if self.isNearBy(float(rental.lat), float(rental.lng)):
                self.rentals.append(rental)

        return self.rentals

    def isNearBy(self, rental_lat, rental_lon) -> bool:
        if self.lat - .2 < rental_lat < self.lat + .2 and self.lon - .2 < rental_lon < self.lon + .2:
            return True
        else:
            return False

