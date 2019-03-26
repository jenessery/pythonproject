from flask import Flask, render_template, request

app = Flask("Test")

def calcgen(year):
    import datetime
    today = datetime.datetime.now()
    if year> today.year:
        raise Exception("Year of birth cannot be in the future.")
    elif 1976<year<1997:
         gen = "Millenial"
    elif year<=1976:
        raise Exception("Sorry, you're too old for this website :(")
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
    try:
        return render_template("gen.html", gen=calcgen(int(year)).title(), year=year)
    except:
        return "Please input a valid year."
