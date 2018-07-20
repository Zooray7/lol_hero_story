from scrapy import cmdline
cmdline.execute("scrapy crawl lol -o hero_story.json --nolog".split())