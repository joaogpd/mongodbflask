from flask import Flask, render_template, url_for, request, redirect, abort
from pymongo import MongoClient
from objectid import ObjectId
import datetime

app = Flask(__name__)

client = MongoClient('mongodb+srv://pstud:gVJQTsM2ftVKES5d@inf1039cardapuc.1cskrne.mongodb.net/?retryWrites=true&w=majority')

db = client["cardapuc"]

collection = db["restaurantes"]

posts = db.posts

@app.route("/")
def index():
    found_post = posts.find_one({ "nome" : "Rei do Mate" })
    return "<p>{}</p>".format(found_post)





