from flask import Flask
from flask import render_template,request
from parser import fetch_articles,fetch_article_by_id,add_post,edit_post

app = Flask(__name__)

@app.route("/")
def home_page():
    articles_list = fetch_articles()
    return render_template("home.html",articles_list=articles_list)

@app.route("/article/<id>",methods=['GET','POST'])
def article_page(id):
    print(id)
    if(request.method == 'POST'):
        title = request.form.get('title')
        date = request.form.get('date')
        desc = request.form.get('description')
        edit_post(id,title,date,desc)
    article = fetch_article_by_id(id)
    return render_template("article.html",article=article)

@app.route("/admin",methods=['GET','POST'])
def admin_page():
    if(request.method == 'POST'):
        title = request.form.get('title')
        date = request.form.get('date')
        desc = request.form.get('description')
        add_post(title,date,desc)
    articles_list = fetch_articles()
    return render_template("admin.html",articles_list=articles_list)


@app.route("/edit/<id>")
def edit_article(id):
    article = fetch_article_by_id(id)
    print(article)
    return render_template("edit.html",article=article)

@app.route("/new")
def add_article():
    return render_template("add.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

