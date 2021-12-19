# Tasks

## 1. Mongo Basics:

    a. implement get_mongo_client()
    b. implement get_listings_reviews_collection()
    c. verify get_first_record() works

## 2. Pipelines (a):

    a. implement query for get_most_reviewed_listing()

## 3. Pipelines (b):

    a. implement query for get_top_10_cities_by_average_rating()

## 4. Improvements:

    a. discuss which improvements could be made to the code
        - parameterize methods for number of items to fetch
        - convert methods to cli / api
        - error handling anywhere / on connection
        - dont hardcode database credentials
        - average rating
            - filter out cities with under certain amount of ratings / adjust for variance for low number listings/ratings
            - if we are interested in average visitor experience we should weight listings scores by number of ratings
        - other ideas for metrics for top destinations
        - check indexes for query performance

## 5. Productionize

    a. convert from a cli to a web-based api
    b. display data using graphics (or discuss how one would do so)
