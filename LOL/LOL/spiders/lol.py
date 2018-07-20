# -*- coding: utf-8 -*-
import scrapy
import re
from LOL.items import LolItem

from scrapy.http import HtmlResponse
class LolSpider(scrapy.Spider):
    name = 'lol'
    allowed_domains = ["http://yz.lol.qq.com/zh_CN/story/"]

    def start_requests(self):
        hero_names = "Aatrox,Ahri,Akali,Alistar,Amumu,Anivia,Annie,Ashe,AurelionSol,Azir,Bard,Blitzcrank,Brand,Braum,Caitlyn,Camille,Cassiopeia,Chogath,Corki,Darius,Diana,Draven,DrMundo,Ekko,Elise,Evelynn,Ezreal,Fiddlesticks,Fiora,Fizz,Galio,Gangplank,Garen,Gnar,Gragas,Graves,Hecarim,Heimerdinger,Illaoi,Irelia,Ivern,Janna,JarvanIV,Jax,Jayce,Jhin,Jinx,Kalista,Karma,Karthus,Kassadin,Katarina,Kayle,Kayn,Kennen,Khazix,Kindred,Kled,KogMaw,Leblanc,LeeSin,Leona,Lissandra,Lucian,Lulu,Lux,Malphite,Malzahar,Maokai,MasterYi,MissFortune,MonkeyKing,Mordekaiser,Morgana,Nami,Nasus,Nautilus,Nidalee,Nocturne,Nunu,Olaf,Orianna,Ornn,Pantheon,Poppy,Pyke,Quinn,Rakan,Rammus,RekSai,Renekton,Rengar,Riven,Rumble,Ryze,Sejuani,Shaco,Shen,Shyvana,Singed,Sion,Sivir,Skarner,Sona,Soraka,Swain,Syndra,TahmKench,Taliyah,Talon,Taric,Teemo,Thresh,Tristana,Trundle,Tryndamere,TwistedFate,Twitch,Udyr,Urgot,Varus,Vayne,Veigar,Velkoz,Vi,Viktor,Vladimir,Volibear,Warwick,Xayah,Xerath,XinZhao,Yasuo,Yorick,Zac,Zed,Ziggs,Zilean,Zoe,Zyra"
        hero_names = hero_names.split(",")
        urls = []
        for hero_name in hero_names:
            url = "http://yz.lol.qq.com/zh_CN/story/champion/"
            url = url + hero_name + "/"
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("-------------------我进入英雄联盟宇宙了--------------------")
        lolItem = LolItem()
        lolItem['name'] = response.xpath(
            '//span[@class="alt__5Tm"]/text()').extract_first()
        lolItem['shortName'] = response.xpath('//*[@id="Content"]/div/div[4]/div[2]/h3/'
                                              'text()').extract_first()
        lolItem['enName'] = response._get_url().split('/')[-2]
        lolItem['story'] = '<Br>'.join(
            response.xpath('//div[@class="ActCopy__3ku left__3Gg dark__1cN "]//p/text()').extract())
        yield lolItem
        print("-------------------我离开英雄联盟宇宙了--------------------")