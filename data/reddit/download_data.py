import praw
import pandas as pd
from tqdm import tqdm

# URL con la información para crear las credenciales: https://github.com/reddit-archive/reddit/wiki/OAuth2

client_id = 'XXX'
client_secret = 'XXX'
user_agent = 'Mental Health'

reddit = praw.Reddit(client_id=client_id, 
            client_secret=client_secret, 
            user_agent=user_agent,
            )

# Ejemplo de foro
topicos = ['mentalhealth']

posts_final = pd.DataFrame()
for elem in tqdm(topicos):
    posts = []
    ml_subreddit = reddit.subreddit(elem)
    for post in ml_subreddit.hot(limit=1000):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    posts_final = pd.concat([posts_final, posts], axis = 0)
    print(posts_final)

posts_final = posts_final.reset_index(drop = True)
