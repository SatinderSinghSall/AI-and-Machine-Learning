from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def prime():
    return render_template("login.html")

@app.route("/dashboard", methods={"GET", "POST"})
def dashboard():
    # if request.method == "POST":
    #     print(request.data)
    #     name = request.form["name"]
    #     password = request.form["password"]
        
    #     return f"<p>Welcome, {name} </P>"

    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
