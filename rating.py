import pip._vendor.requests as requests
from datetime import datetime, timezone
from bottle import route, run, template, request




my_list = []  #for prediction


city = "San%20Francisco"   #should be entered using the search bar 


apiKey= "133427a1a3cc422f8271dfdf1e143648"  

# Define the URL for news data
news_url = "https://newsapi.org/v2/everything?q=" + city + "+crime&excludeDomains=freerepublic.com&from=2023-09-29&apiKey=" + apiKey
print(news_url)
# Crime keywords and their associated danger ratings
crime_keywords = {
    "Rape": 5,
    "Sexual Assault": 5,
    "Domestic Abuse": 4,
    "Physical Abuse": 4,
    "Sexual Abuse": 5,
    "Homicide": 5,
    "Murder": 5,
    "Trafficking": 5,
    "Human Trafficking": 5,
    "Drug Trafficking": 4,
    "Robbery": 3,
    "Armed Robbery": 4,
    "Kidnapping": 5,
    "Abduction": 5,
    "Child Abduction": 5,
    "Sex Trafficking": 5,
    "Laundering": 2,
    "Money Laundering": 2,
    "Arson": 4,
    "Arsonist": 4,
    "Assault": 4,
    "Physical Assault": 4,
    "Burglary": 3,
    "Home Invasion": 4,
    "Fraud": 3,
    "Identity Fraud": 4,
    "Credit Card Fraud": 4,
    "Embezzlement": 3,
    "White Collar Crime": 3,
    "Manufacturing": 3,
    "Drug Manufacturing": 3,
    "Counterfeiting": 2,
    "Distribution": 3,
    "Drug Distribution": 3,
    "Identity Theft": 3,
    "Vandalism": 2,
    "Graffiti": 1,
    "Theft": 3,
    "Stolen": 3,
    "Auto Theft": 4,
    "Bike Theft": 2,
    "Cybercrime": 2,
    "Online Fraud": 2,
    "Possession": 2,
    "Drug Possession": 2,
    "Trespassing": 1,
    "Criminal Trespassing": 2,
    "Shoplifting": 1,
    "Retail Theft": 1,
    "Petty Theft": 1,
    "Pickpocketing": 1,
}

# Make a GET request to the news URL
response = requests.get(news_url)

# Initialize variables to calculate city danger measure
total_danger_rating = 0
article_count = 0

# Check if the news request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    news_data = response.json()

    # Access and analyze the news data
    articles = news_data.get("articles", [])

    for index, article in enumerate(articles):
        title = article.get("title", "").lower()
        description = article.get("description", "").lower()

        # Calculate the danger rating for the article based on keywords
        danger_rating = 0
        for keyword, rating in crime_keywords.items():
            if keyword.lower() in title or keyword.lower() in description:
                danger_rating += rating

                # Assuming your date is in ISO 8601 format
                date_string = article.get("publishedAt","")

                # Convert the date string to a datetime object
                published_at = datetime.fromisoformat(date_string).replace(tzinfo=timezone.utc)

                # Get the current date and time
                current_date = datetime.now(timezone.utc)

                # Calculate the difference in days
                difference = current_date - published_at

                # Access the days component of the difference
                days_ago = difference.days

                # Assuming index and rating are defined
                my_list.append((index, rating, days_ago))


#datetime.utcnow()-datetime.fromisoformat(article.get("publishedAt",""))

        # If the article contains crime keywords, add its danger rating to the total
        if danger_rating > 0:
            total_danger_rating += danger_rating
            article_count += 1


    # Make a GET request to the city population API

    city_api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city)
    response = requests.get(city_api_url, headers={'X-Api-Key': 'MBLtSMUqzGZkqENlXZM7Zg==INiACq7u4cLZhRnE'})

    # Check if the city population request was successful (status code 200)
    if response.status_code == requests.codes.ok:
        city_data = response.json()

        # Get the population of the city
        city_population = city_data[0].get("population", 1)  # Default to 1 if population is not available

        # Calculate the city danger measure by dividing total_danger_rating by city_population
        if article_count > 0:
            city_danger_measure = (total_danger_rating / city_population) * 100000
        else:
            city_danger_measure = 0

        # Assign a danger rating to the city based on the value
        if city_danger_measure > 4:
            city_rating = 5
        elif city_danger_measure > 3:
            city_rating = 4
        elif city_danger_measure > 2:
            city_rating = 3
        elif city_danger_measure > 1:
            city_rating = 2
        else:
            city_rating = 1

        print("City Population:", city_population)
        print("City Danger Measure:", city_danger_measure)
        print("City Rating:", city_rating)
    else:
        print("City population request failed with status code:", response.status_code)
else:
    print("News request failed with status code:", response.status_code)
