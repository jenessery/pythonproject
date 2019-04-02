from flask import Flask, render_template, request
import requests
import json

app = Flask("Test")

def calcgen(year):
    import datetime
    today = datetime.datetime.now()
    if year> today.year:
        gen = "You are a time traveller, with a date of birth in the future!"
    elif year>=1997:
        gen = "You're too young :("
    elif year<1997 and year>1976:
        gen = "Millenial"
    elif year<=1976:
        gen = "You're too old :("
    else:
        raise Exception("Please input a valid year of birth")
    return gen

@app.route("/")

def default():
    return render_template("index.html", name="Internet Stranger")

@app.route("/welcome",methods=["POST"])
def agecondition():
    form_data = request.form
    year = form_data["year"]
    name = form_data["name"]
    gen=calcgen(int(year))
    if gen=="Millenial":
        return render_template("welcome.html", gen=gen.title(), year=year, name=name)
    else:
        return render_template("notwelcome.html",gen=gen, name=name)

@app.route("/dictionary",methods=["POST"])
def wordlookup():
    form_data = request.form
    word_id = form_data["word"]
    app_id = '9195ec30'
    app_key = '0af5c75c6cf9f52ce7eea31a04a9bcdc'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word_id.lower() + '/synonyms'

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}).json()
    return r

    synonyms = r['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
    word = r['results'][0]['word'][0]
    define = r['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']


    return render_template("dictionary.html",r=synonyms,w=word,d=define)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
	app.run()
