import feedparser
from flask import Flask

from headlines import app



news_feeds = {
"bbc" : "http://feeds.bbci.co.uk/news/rss.xml",
"dailyTrust" : "https://www.dailytrust.com.ng/rss/feed.aspx?cat_id=3",
"vanguard_nig" : "https://investornews.vanguard/feed/",
"sahara" : "http://saharareporters.com/feeds/latest/feed",
"cnn": "http://rss.cnn.com/rss/edition.rss",
"fox": "http://feeds.foxnews.com/foxnews/latest",
"iol": "http://www.iol.co.za/cmlink/1.640"
}

@app.route('/headlines3/<publications>')
def headlines3(publications="bbc"):
    feed = feedparser.parse(news_feeds[publications])
    first_article = feed['entries'] [0]
    return """<html>
                    <head>
                        <title>News Headlines</title>
                    </head>
                    <body>
                        <h2>""" + publications.upper() + """ Headlines</h2>
                        <b>{0}</b> <br />
                        <i>{1}</i> <br />
                        <p>{2}</p> <br />
                    </body>
            </html>""".format(first_article.get("title"), first_article.get("published"), 
            first_article.get("summary"))
