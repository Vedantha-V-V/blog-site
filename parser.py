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
    print(article_path)
    try:
        with open(article_path, 'r', encoding='utf-8') as file:
            article = json.load(file)
            return article
    except FileNotFoundError:
            print("Article {article} not found.")
    except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file. Check for invalid JSON syntax.")
    return ""




def main():
    print("Article Parser has been activated.")
    fetch_articles()


if __name__ == "__main__":
    main()