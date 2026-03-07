from flask import Flask
from flask import render_template
from parser import fetch_articles,fetch_article_by_id

app = Flask(__name__)

@app.route("/")
def home_page():
    articles_list = fetch_articles()
    return render_template("home.html",articles_list=articles_list)

@app.route("/article/<id>")
def article_page(id):
    article = fetch_article_by_id(id)
    print(article)
    return render_template("article.html",article=article)

@app.route("/admin")
def admin_page():
    return 'Index Page'

@app.route("/edit/<int:id>")
def edit_article():
    return 'Index Page'

@app.route("/new")
def add_article():
    return 'Index Page'

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

