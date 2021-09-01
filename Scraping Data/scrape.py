import requests
from bs4 import BeautifulSoup
import pprint
import time

# res = requests.get('https://news.ycombinator.com/news')

# soup = BeautifulSoup(res.text, 'html.parser') # string to object

# links = soup.select('.storylink') # class storylink
# subtext = soup.select('.subtext') # class subtext

def get_data(pages):
    links = []
    subtext = []

    for page in range(pages):
        res = requests.get(f'https://news.ycombinator.com/news?p={page + 1}')
        
        soup = BeautifulSoup(res.text, 'html.parser') # string to object

        links = links + soup.select('.storylink') # class storylink
        subtext = subtext + soup.select('.subtext') # class subtext

        time.sleep(1) # robots.txt: crawl-delay: 30

    return [links, subtext]

def sort_post_by_votes(posts):
    return sorted(posts, key = lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = [] # each list element will be a dict

    for index, item in enumerate(links):
        title = item.getText() # post title
        href = item.get('href', None) # link new, if it doesn't existm href will be None (default parameter)
        vote = subtext[index].select('.score') # class score within subtext

        if len(vote): # only if the post has points
            points = int(vote[0].getText().replace(' points', '')) # from 'x points' to 'x' then str to int
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})

    return hn

def main():
    while True:
        try:
            pages = int(input('How many pages would you like to scrap? '))
            print()

            if pages > 0 and type(pages) == int:
                links, subtext = get_data(pages) # list unpacking
                break
        except ValueError:
            print('Please, type a number.')

    posts = create_custom_hn(links, subtext)
    sorted_posts = sort_post_by_votes(posts)

    for post in sorted_posts:
        print(f'Votes: {post["votes"]}')
        print(post['title'])
        print(f'{post["link"]} \n')
    
    print(f'{len(sorted_posts)} posts.')

if __name__ == '__main__':
    main()
