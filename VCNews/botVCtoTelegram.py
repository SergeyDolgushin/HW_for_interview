import json
import requests
from bs4 import BeautifulSoup
import telebot


class newsVCruBot():
    
    def __init__(self, url = 'https://vc.ru/new'):
        
        self.url_vc_ru = url

    def get_answer_from_site(self):

        HEADERS = {
        'Sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }    
        try:
            ret = requests.get(self.url_vc_ru, headers = HEADERS)
            ret.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return ret

    def parse_data(self, ret):
        
        soup = BeautifulSoup(ret.text, 'html.parser')
        main_block = soup.find(class_="feed__container")
        articles = main_block.find(class_ = "content content--short")
        title_article = soup.find(class_ = "content-title--short").text.replace('Статьи редакции', '', 1)
        format_title = title_article.strip()
        compare_title = self.get_config('last.json')
        news_text = articles.find("p").text.strip()
        link_to_full_version = articles.find(class_ = "content-link").get('href').strip()
        if compare_title['lastArt'] in format_title:
            return False
        else:
            compare_title['lastArt'] = format_title
            self.set_config(compare_title)
            return f'{format_title} \r\n\r\n {news_text}\r\n{link_to_full_version}'

    def get_config(self, conf_file = 'conf.json'):

        with open(conf_file, encoding = "utf-8") as file:
            config = json.load(file)
        
        return config

    def set_config(self, config):
    
        with open('last.json', 'w', encoding = "utf-8") as file:
            json.dump(config, file)        
    
    def start_bot(self, id):

        bot = telebot.TeleBot(id)
        return bot

    def send_message_to_channel(self, bot, text_news, channel):
        
        bot.send_message(channel, text_news)

        return True


if __name__ == '__main__':

      
    news = newsVCruBot()
    bot = news.start_bot(news.get_config()['ID'])
    ret = news.get_answer_from_site()
    current_news = news.parse_data(ret)
    if current_news != False:
        news.send_message_to_channel(bot, current_news, news.get_config()['channel'])
    