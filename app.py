from flask import Flask, jsonify, request
from flask_cors import CORS
from api import *
from api.lyricsapi import LyricsApi

app = Flask(__name__)
CORS(app)
Lyr = LyricsApi()

@app.route('/')
def home():
    return jsonify("Welcome to Lyrics Api")

@app.route('/getlyrics/')
def getlyrics():
    title = request.args.get('title')
    artists = request.args.get('artists')
    result = Lyr.getLyrics(artists,title)
    return jsonify(result)


if __name__ == '__main__':
    app.run()