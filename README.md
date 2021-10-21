# lyrics-api
<p align="center">
    <a href="#description">Description</a> &bull; 
    <a href="#installation">Installation</a> &bull;  
    <a href="#usage">Usage</a> &bull;  
    <a href="#license">License</a>
</p>

## Description
Api to get lyrics of the songs by its title and artists name<br>
Currently it searches lyrics from azlyrics.com, more websites will be added in future

Sample response data:
```json
{
    "status":true,
    "lyrics":"The club isn't the best place to find a lover\n
    So the bar is where I go (mmmm)\n
    Me and my friends at the table doing shots\n
    Drinking fast and then we talk slow (mmmm)\n
    And you come over and start up a conversation with just me\n
    And trust me I'll give it a chance now (mmmm)\n
    Take my hand, stop, put Van The Man on the jukebox\n ........"
}
```
---
## Installation
Clone this repository using
```sh
git clone https://github.com/amit-y11/lyrics-api
```
Enter the directory and install all the requirements using
```sh
pip3 install -r requirements.txt
```
Run the app using
```sh
python3 app.py
```
Now the app is running on http://127.0.0.1:5000

## Usage
```sh
http://127.0.0.1:5000/getlyrics/?title=<Enter title of the song>&artists=<Enter artists of the song>
```
Example: Navigate to http://127.0.0.1:5000/getlyrics/?title=shape%20of%20you&artists=ed%20sheeran to get JSON response of lyrics data in return


#### You can fork the repo and deploy on VPS or deploy it on Heroku 😊  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/amit-y11/lyrics-api)

## License

[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

PicSplash is a Free Software: You can use, study, share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.  
