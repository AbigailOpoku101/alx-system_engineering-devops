#!/usr/bin/python3
""" Queries the Reddit API parses the title of hot art.
and prints a sorted count for a given subreddit. """


import requests

def count_words(subreddit, word_list):
    headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/piroli_)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        # Create a dictionary to store the word counts
        word_counts = {}

        # Process each article
        for article in articles:
            title = article['data']['title'].lower()

            # Split the title into words
            words = title.split()

            # Count the occurrences of each word
            for word in words:
                # Remove non-alphanumeric characters from the word
                word = ''.join(ch for ch in word if ch.isalnum())

                # Check if the word is in the word_list
                if word.lower() in word_list:
                    # Update the word count in the dictionary
                    word_counts[word] = word_counts.get(word, 0) + 1

        # Sort the word counts by count (descending) and then alphabetically (ascending)
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # Print the sorted counts
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        print("Error: Unable to retrieve data from the Reddit API")

    # Recursive call to count_words with the same subreddit and word_list
    # Add an exit condition to avoid infinite recursion (e.g., if len(word_list) == 0)
    if len(word_list) > 0:
        count_words(subreddit, word_list[1:])


# Example usage
subreddit = "python"
word_list = ["python", "java", "javascript"]
count_words(subreddit, word_list)
