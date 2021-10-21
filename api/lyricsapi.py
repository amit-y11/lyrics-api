from bs4 import BeautifulSoup as bs
import requests
from config import *


class LyricsApi():
    '''
    Lyrics Api Class
    ---

    Methods
    ---
    * getLyrics(artists,title) -> dict
        
    '''

    def getLyrics(self,artists : str,title : str) -> dict:
        '''
        get lyrics from title and artists name

        Parameters
        ---
        * artists : (str) the name of the artists
        * title : (str) the name of the song

        Returns
        ---
        A dictionary with keys status (bool)

        If status is true then dictionary contains lyrics (str) key else 
        it contains Error key
        '''
        try:
            artists = artists.lower()
            title = title.lower()

            result_page = requests.get(f'{azlyrics_search_endpoint}{title} {artists}',headers=endpoint_headers)
            result_soup = bs(result_page.text,'html.parser')
            results = result_soup.select_one('td.visitedlyr a')
            if results is not None:
                link = results.get('href')
                lyrics_page = requests.get(link,headers=endpoint_headers)
                lyrics_soup = bs(lyrics_page.text,'html.parser')
                res = lyrics_soup.find("div",attrs={"class":None,"id":None})
                return {
                    "status":True,
                    "lyrics":res.text.strip()
                }
            else:
                return {
                    "status":False,
                    "Error":"Lyrics not Found"
                }
        except Exception as e:
            return {
                "status":False,
                "Error": e
            }

