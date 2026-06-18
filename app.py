# =========================================
# IMPORT FLASK
# =========================================

from flask import Flask, render_template

# =========================================
# CREATE APP
# =========================================

app = Flask(__name__)

# Secret Key
app.secret_key = "pitchup_secret_key"

# =========================================
# HOME ROUTE
# =========================================

@app.route("/")
def home():
    return render_template("home.html")

# =========================================
# RUN SERVER
# =========================================

if __name__ == "__main__":
    app.run(debug=True)