import json
import os

def fetch_articles():
    articles = []
    directory = './articles'
    paths = os.listdir(directory)
    for path in paths:
        article_path = f"{directory[2:]}/{path}"
        try:
            with open(article_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                articles.append(data)
        except FileNotFoundError:
            print("Article {article} not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file. Check for invalid JSON syntax.")
    return articles

def fetch_article_by_id(id):
    directory = './articles'
    paths = os.listdir(directory)
    article_path = f"./articles/AT{id}.json"
    try:
        with open(article_path, 'r', encoding='utf-8') as file:
            article = json.load(file)
            return article
    except FileNotFoundError:
            print("Article {article} not found.")
    except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file. Check for invalid JSON syntax.")
    return ""

def add_post(title,date,desc):
    article = {}
    files = os.listdir('articles')
    id = int(files[len(files)-1][2:-5])+1
    article["id"] = id
    article['title'] = title
    article['date'] = date
    article['description']  = desc
    post = f"./articles/AT{id}.json"
    try:
        with open(post, 'w', encoding='utf-8') as file:
            json.dump(article,file)
    except FileNotFoundError:
            print("Article {article} not found.")
    except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file. Check for invalid JSON syntax.")

def edit_post(id,title,date,desc):
    post = f"./articles/AT{id}.json"
    try:
        with open(post, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data['title'] = title
        data['date'] = date
        data['description'] = desc
        with open(post, 'w', encoding='utf-8') as file:
            json.dump(data,file)
    except FileNotFoundError:
            print("Article {article} not found.")
    except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file. Check for invalid JSON syntax.")

def delete_post(id):
    pass


def main():
    print("Article Parser has been activated.")
    fetch_articles()


if __name__ == "__main__":
    main()