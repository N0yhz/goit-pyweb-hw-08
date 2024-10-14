import redis
import json
from models import Author, Quote

r = redis.Redis(host='localhost', port=6379, db=0)

def find_quotes_by_author(name):

    cache_key = f'name:{name}'
    cached_results = r.get(cache_key)

    if cached_results:
        print('Results from cache:')
        quotes = json.loads(cached_results)
        for quote in quotes:
            print(f"{quote}")
    else:        
        authors = Author.objects(fullname__icontains=name)
        quotes_list = []
        if authors:
            for author in authors:
                quotes = Quote.objects(author=author)
            for quote in quotes:
                quotes_list.append(quote.quote)
                print(f"{quote.quote}")

            r.set(cache_key, json.dumps(quotes_list), ex=300)  # Cache results for 5 minutes
        else:
            print("Author not found")

def find_quotes_by_tag(tag):

    cache_key = f'tag:{tag}'
    cached_results = r.get(cache_key)

    if cached_results:
        print('Results cached from:')
        quotes = json.loads(cached_results)
        for quote in quotes:
            print(f"{quote}")

    else:
        quotes = Quote.objects(tags__icontains=tag)
        quotes_list = []
        for quote in quotes:
            quotes_list.append(quote.quote)
            print(f"{quote.quote}")

        r.set(cache_key, json.dumps(quotes_list), ex=300)

def find_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        print(f"{quote.quote}")

while True:
    command = input('Command:').strip()

    if command.startswith('name:'):
        name = command[len('name:'):].strip()
        find_quotes_by_author(name)

    elif command.startswith('tag:'):
        tags = command[len('tag:'):].strip()
        find_quotes_by_tag(tags)

    elif command.startswith('tags:'):
        tags = command[len('tags:'):].strip()
        find_quotes_by_tags(tags)

    elif command.lower() == 'exit':
        break

    else:
        print("Invalid command. Exiting")