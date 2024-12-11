import requests
import time


# response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
topstorie = response.json()

print(topstorie[:30])

for i in topstorie[:30]:
    response_30 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json")
    art_30 = response_30.json()
    # print(art_30)
    if art_30.get("title") and art_30.get("url"):
        print({"title": art_30["title"], "link": art_30["url"]})
        # print(f"title: {art_30["title"]}, link: {art_30["url"]}")
    else:
        print(f"'title: {art_30["title"]}', 'link: {None}'")

    time.sleep(1)
# response = requests.get("https://hacker-news.firebaseio.com/v0")

# response_01 = requests.get("https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty")
# response_02 = requests.get("https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty")
# response_03 = requests.get("https://hacker-news.firebaseio.com/v0/item/121003.json?print=pretty")
# print(response)
# print(response.json())
# print(response.text)
# for i in range(3):
# time.sleep(1)
# print(i)

# response.request.path_url

# response_url = response.request.url
# response_title = response_01.request.title
# print(f"'title': {}, 'link': '{response_url}'")


# response_url = response_01.text
