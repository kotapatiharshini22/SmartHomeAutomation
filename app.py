from flask import Flask, render_template, redirect, url_for

from database import create_database
from database import get_devices

from devices import *

app = Flask(__name__)

create_database()


@app.route("/")

def home():

    devices = get_devices()

    return render_template("dashboard.html",devices=devices)


@app.route("/light_on")

def lighton():

    light_on()

    return redirect(url_for("home"))


@app.route("/light_off")

def lightoff():

    light_off()

    return redirect(url_for("home"))


@app.route("/fan_on")

def fanon():

    fan_on()

    return redirect(url_for("home"))


@app.route("/fan_off")

def fanoff():

    fan_off()

    return redirect(url_for("home"))


@app.route("/lock")

def lock():

    door_lock()

    return redirect(url_for("home"))


@app.route("/unlock")

def unlock():

    door_unlock()

    return redirect(url_for("home"))


@app.route("/ac_on")

def acon():

    ac_on()

    return redirect(url_for("home"))


@app.route("/ac_off")

def acoff():

    ac_off()

    return redirect(url_for("home"))


if __name__=="__main__":

    app.run(debug=True)