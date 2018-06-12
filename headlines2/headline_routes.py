import feedparser
from flask import Flask, render_template

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

@app.route('/')
@app.route('/headlines/<publications>')
def headlines(publications="bbc"):
    feed = feedparser.parse(news_feeds[publications])
    first_article = feed['entries'] [0]
    return render_template('headlines.html',
                            title=first_article.get("title"),
                            published=first_article.get("published"),
                            summary=first_article.get("summary"))
