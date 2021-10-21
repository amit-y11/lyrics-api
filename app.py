from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from api import *
from api.lyricsapi import LyricsApi

app = Flask(__name__)
CORS(app)
Lyr = LyricsApi()

@app.route('/')
def home():
    return redirect("https://amit-y11.github.io/lyrics-api/")

@app.route('/getlyrics/')
def getlyrics():
    title = request.args.get('title')
    artists = request.args.get('artists')
    result = Lyr.getLyrics(artists,title)
    return jsonify(result)


if __name__ == '__main__':
    app.run()