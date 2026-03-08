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
    return render_template("article.html",article=article)

@app.route("/admin")
def admin_page():
    articles_list = fetch_articles()
    return render_template("admin.html",articles_list=articles_list)

@app.route("/edit/<id>")
def edit_article(id):
    return 'Index Page'

@app.route("/new")
def add_article():
    return render_template("add.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

