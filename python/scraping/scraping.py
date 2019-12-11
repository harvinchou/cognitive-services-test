import sys
import os
import time
import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

site = 'http://www.bbc.co.uk'

def _get_all_urls(homeurl: str):    
    response = requests.get(homeurl)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')
    li_list = soup.find('div', attrs={'class':'widget widget-list widget-list-automatic'}).find_all('li')

    for li_tag in li_list:
        url = site + li_tag.a['href']

        if 'media-english' in url:
            _get_media_english(url)

        if 'todays-phrase' in url:
            _get_todays_phrase(url)
            
def _get_todays_phrase(url: str):
    #url = 'http://www.bbc.co.uk/learningenglish/chinese/features/todays-phrase/ep-191128'
    if url[-6:] > '191128':     # only scraping articles newer than this number
        try:
            print(f'Get Todays Phrase from {url}')
            response = requests.get(url)
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'html.parser')
            name_box = soup.find('h3', text="例句").find_next_siblings('p')

            with open('bbc-todays-phrase.txt', 'a', encoding="utf-8") as fp:
                for p_tag in name_box:
                    for p_text in list(p_tag.stripped_strings):
                        print(p_text)
                        fp.writelines(f"{p_text}\n")
            
            time.sleep(2)
        except:
            print("Unexpected error:", sys.exc_info()[0])    

def _get_media_english(url: str):
    #url = 'http://www.bbc.co.uk/learningenglish/chinese/features/media-english/ep-191125'
    if url[-6:] > '000000':     # only scraping articles newer than this number
        try:
            print(f'Get Media English from {url}')
            response = requests.get(url)
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find('div', attrs={'class':'text', 'dir':'ltr'}).contents

            with open('bbc-media-english.txt', 'a', encoding="utf-8") as fp:
                i = 1
                while i < len(tags):
                    if tags[i].name == 'h3':
                        if '词汇' in tags[i].text:
                            break
                    if tags[i].name == 'p':
                        print(tags[i].text)
                        fp.writelines(f"{tags[i].text}\n")
                    i += 1            
            
            time.sleep(2)
        except:
            print("Unexpected error:", sys.exc_info()[0])    

def main():
    _get_all_urls(sys.argv[1])

    
if __name__ == '__main__':
    main()