import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__, static_url_path='/', static_folder='ui')

app.config.from_object(os.environ['APP_SETTINGS'])
# app.config.from_object("config.DevelopmentConfig")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# API Controllers
@app.route("/api/coupons/all")
def get_all():
    try:
        coupons = Coupon.query.all()
        return  jsonify([e.serialize() for e in coupons])
    except Exception as e:
	    return(str(e))

@app.route("/api/coupons/<lat>/<long>")
def get_by_lat_long(lat, long):
    try:
        coupons = Coupon.query.filter_by(latitude = lat, longitude = long).all()
        return jsonify([e.serialize() for e in coupons])
    except Exception as e:
	    return(str(e))

# Serve UI (html)
@app.route('/')
def send_home_page():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def send_static_files(path):
    return app.send_static_file(path)

if __name__ == '__main__':
  app.run()