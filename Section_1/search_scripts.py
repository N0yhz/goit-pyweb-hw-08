from models import Author, Quote

def find_quotes_by_author(name):
    author =  Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(f"{quote.quote}")
    else:
        print("Author not found")

def find_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(f"{quote.quote}")

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