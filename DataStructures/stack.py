"""

Imagine you’re creating a web browser’s history functionality
 in which store every page a user visits so they can go back in time easily.
 Assume these are the actions a random user takes on their browser:

"""

from collections import deque

def new_web_site_in_history(url):
    web_history.append(url)


def delete_last_visited_web_site_from_history():
    web_history.pop()

def show_me_web_history():
    print(web_history)

web_history = deque()

new_web_site_in_history("https://realpython.com/")
new_web_site_in_history("https://realpython.com/python-csv/")
new_web_site_in_history("https://realpython.com/pandas-read-write-files/")

show_me_web_history()

delete_last_visited_web_site_from_history()
show_me_web_history()
