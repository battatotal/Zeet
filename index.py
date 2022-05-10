import os
from flask import Flask, render_template, url_for, g, abort
import json



app = Flask(__name__)



@app.errorhandler(404)
def pageNotFound(error):
    with open('mainmenu.json', mode='r', encoding='utf-8') as my_file:
        menu = json.load(my_file)
    return render_template("page404.html", title="Страница не найдена", menu= menu)


@app.route("/")
def index():
    with open('mainmenu.json', mode='r', encoding='utf-8') as my_file:
        menu = json.load(my_file)
    return render_template('index.html', menu= menu, title="Главная")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/about")
def about():
    return "<h1>О сайте</h1>"

@app.route("/gallery")
def gallery():
    with open('mainmenu.json', mode='r', encoding='utf-8') as my_menu:
        menu = json.load(my_menu)

    with open('objects.json', mode='r', encoding='utf-8') as my_obj:
        obj = json.load(my_obj)
    return render_template("galleryWork.html", title="Галерея", menu= menu, objects=obj)


@app.route("/actual_gallery")
def actual_gallery():
    with open('mainmenu.json', mode='r', encoding='utf-8') as my_menu:
        menu = json.load(my_menu)
    with open('objects.json', mode='r', encoding='utf-8') as my_obj:
        r = json.load(my_obj)
        obj = [o for o in r if o['actual'] == 'True']
    return render_template("actual_gallery.html", title="Галерея/Есть в наличии", menu= menu, objects=obj)

@app.route("/gallery/object/<alias>")
def object(alias):
    with open('mainmenu.json', mode='r', encoding='utf-8') as my_menu:
        menu = json.load(my_menu)
    #res = Objects.query.filter_by(url=alias).all()
    with open('objects.json', mode='r', encoding='utf-8') as my_obj:
        r = json.load(my_obj)
        res = [o for o in r if o['url'] == alias]

    if not res[0]:
        abort(404)

    return render_template("object.html", res=res, title="Галерея"+"/"+str(res[0]['title']), alias=alias, menu=menu)



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
    # from waitress import serve
    #
    # serve(app, host="127.0.0.1", port=5000)