import os
from dotenv import load_dotenv
from flask import Flask
from flask import render_template,request,redirect,url_for,make_response,session
from parser import fetch_articles,fetch_article_by_id,add_post,edit_post

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def home_page():
    articles_list = fetch_articles()
    return render_template("home.html",articles_list=articles_list)

@app.route("/article/<id>")
def article_page(id):
    article = fetch_article_by_id(id)
    return render_template("article.html",article=article)

@app.route("/auth/<page>",methods=['POST'])
def authentication(page):
    username = request.form.get('username')
    password = request.form.get('password')
    uname = os.getenv('HOST_UNAME')
    pwd = os.getenv('HOST_PASSWORD')
    if(username == uname and password == pwd):
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if('edit' in page):
            id = page[13:]
            page = page[:12]
            return redirect(url_for(page,id=id))
        return redirect(url_for(page))
    return "Only Admin can make changes"

@app.route("/admin",methods=['GET','POST'])
def admin_page():
    if 'username' not in session or 'password' not in session:
        return render_template('auth.html',page='admin_page')
    articles_list = fetch_articles()
    return render_template("admin.html",articles_list=articles_list)

@app.route("/edit/<id>")
def edit_article(id):
    if 'username' not in session or 'password' not in session:
        path = f"edit_article_{id}"
        return render_template('auth.html',page=path)
    article = fetch_article_by_id(id)
    return render_template("edit.html",article=article)

@app.post("/update/<id>")
def edit_form(id):
    title = request.form.get('title')
    date = request.form.get('date')
    desc = request.form.get('description')
    edit_post(id,title,date,desc)
    return redirect(url_for('admin_page'))

@app.route("/new")
def add_article():
    if 'username' not in session or 'password' not in session:
        return render_template('auth.html',page='add_article')
    return render_template("add.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.post("/add")
def add_form():
    title = request.form.get('title')
    date = request.form.get('date')
    desc = request.form.get('description')
    add_post(title,date,desc)
    return redirect(url_for('admin_page'))

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

