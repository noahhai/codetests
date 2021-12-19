# Mongo Atlas Gui Access
# Url: https://cloud.mongodb.com/v2/61bf923b21429b7c8634764b#clusters
# Email: sandbox-293291912@mailinator.com
# Pass: 23j*@3723jrf-w2,,/

from pprint import pprint
from typing import List

from pymongo import DESCENDING, MongoClient
from pymongo.collection import Collection
from tabulate import tabulate

MONGO_HOST = ""  # TODO : Implement - Task 1
MONGO_USER = "readonly"
MONGO_PASS = "thycoticcentrify"
MONGO_DB = "sample_airbnb"
MONGO_COLLECTION = "listingsAndReviews"


def get_mongo_client() -> MongoClient:
    """Create a mongo client

    Returns:
        MongoClient: Mongo DB Client
    """

    # TODO : Implement - Task 1

    pass


def get_listings_reviews_collection(client: MongoClient) -> Collection:
    """Create a reference to the listingsAndReviews Collection
    in the sample airbnb database

    Args:
        client (MongoClient): Mongo DB Client

    Returns:
        Collection: Mongo DB Collection
    """

    # TODO : Implement - Task 1


def get_first_record(coll: Collection) -> dict:
    """Return the first record from a Mongo DB Collection

    Args:
        coll (Collection): Mongo DB Collection

    Returns:
        dict: Mongo DB Document
    """
    return coll.find_one({})


def get_most_reviewed_listing(coll: Collection) -> List:
    """Fetch the most reviewed listings

    Args:
        coll (Collection): Mongo DB Collection of ListingsAndReviews

    Returns:
        List: List of Mongo DB Documents
    """

    # TODO : implement - Task 2
    pipeline = []

    results = coll.aggregate(pipeline)
    return list(results)


def get_top_10_cities_by_number_listings(coll: Collection) -> List:
    """Fetch the top 10 cities ranked by the number of listings

    Args:
        coll (Collection): Mongo DB Collection of ListingsAndReviews

    Returns:
        List: List of Mongo DB Documents
    """

    pipeline = [
        {"$group": {"_id": "$address.market", "listingCount": {"$sum": 1}}},
        {"$sort": {"listingCount": -1}},
        {"$limit": 10},
    ]

    results = coll.aggregate(pipeline)
    return list(results)


def get_top_10_cities_by_average_rating(coll: Collection) -> List:
    """Fetch teh top 10 cities by the average rating of reviews of its listings

    Args:
        coll (Collection): Mongo DB Collection of ListingsAndReviews

    Returns:
        List: List of Mongo DB Documents
    """

    # TODO : implement - Task 3
    pipeline = []

    results = coll.aggregate(pipeline)
    return results


def main():
    # Increment as you work through the tasks and implement the required methods
    task_index = 1  # 1,2,3

    client = get_mongo_client()
    listings_reviews_collection = get_listings_reviews_collection(client)

    if task_index >= 1:
        first_record = get_first_record(listings_reviews_collection)
        print("Keys for first record in reviews collection:\n")
        pprint(list(first_record.keys()))

    if task_index >= 2:
        most_reviewed = get_most_reviewed_listing(listings_reviews_collection)
        print("\nMost Reviewed:\n")
        print(tabulate(most_reviewed, headers="keys"))

    if task_index >= 3:
        top_to_cities_by_number_listings = get_top_10_cities_by_number_listings(listings_reviews_collection)
        print("\nTop 10 cities by number listings:\n")
        print(tabulate(top_to_cities_by_number_listings, headers="keys"))

        top_to_cities_by_average_rating = get_top_10_cities_by_average_rating(listings_reviews_collection)
        print("\nTop 10 cities by average rating:\n")
        print(tabulate(top_to_cities_by_average_rating, headers="keys"))


if __name__ == "__main__":
    main()
