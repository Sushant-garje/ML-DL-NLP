from flask import Flask,render_template,request,redirect,url_for



'''
it creates an instance of the flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''

## WSGI application
app =Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask!</H1></html>"

@app.route("/index",methods=["GET"])
def index():
    containt = {
        "name":"sushant"
    }
    return render_template("index.html", **containt)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"hello {name}!"
    else:
        return render_template("form.html")


# Variable rule
@app.route("/success/<int:score>")
def success(score):
    if score >= 90:
        res= "topper"
    elif score >= 35:
        res= "pass"
    else:
        res= "fail"

    containt = {
        "result":res,
        "score":score
    }
    return render_template("result.html",**containt)

@app.route("/submit",methods=["GET","POST"])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        math = float(request.form["maths"])
        c = float(request.form["C"])
        data_science = float(request.form["data_science"])

        total_score =(science + math + c + data_science)/4
    else:
        return render_template("submit.html")
    return redirect(url_for("success",score=total_score))

if __name__ == "__main__":
    app.run(debug=True)