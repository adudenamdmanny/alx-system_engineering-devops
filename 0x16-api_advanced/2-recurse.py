#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = {}  # Initialize the dictionary to store word counts

    headers = {'User-Agent': 'Your User Agent'}  # Replace with your User Agent
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()  # Convert title to lowercase
            for word in word_list:
                if word in title and title.count(word) > 0:
                    if word in word_counts:
                        word_counts[word] += title.count(word)
                    else:
                        word_counts[word] = title.count(word)

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")

    else:
        print("Invalid subreddit or no matching posts.")

# Example usage
subreddit = "programming"
word_list = ["python", "javascript", "java"]
count_words(subreddit, word_list)

