import os
import sqlite3
import logging
from flask import Flask, session, redirect, url_for, request, render_template, abort

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.logger.setLevel(logging.INFO)


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


def is_authenticated():
    return "username" in session


def authenticate(username, password):
    # Basic input validation
    if not username or not password:
        abort(400)

    connection = get_db_connection()
    user = connection.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()
    connection.close()

    if user and user["password"] == password:
        app.logger.info(f"user '{username}' logged in successfully")
        session["username"] = username
        return True

    app.logger.warning(f"failed login attempt for '{username}'")
    abort(401)


@app.route("/")
def index():
    return render_template("index.html", is_authenticated=is_authenticated())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if authenticate(username, password):
            return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
