import json
from urllib.request import urlopen
from random import shuffle
import random
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    # 1. はてブのホットエントリーページのHTMLを取得する 
    with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")

    # 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")

    # 3. 記事一覧を取得する
    news_list = soup.select(".entrylist-contents-title a")

    #4. ランダムに1件取得する
    news = random.choice(news_list)
    print(news)

    # 5. JSON形式で返却する.
    return json.dumps(
        {
            "content" : news["title"],
            "link" : news["href"]
        }
    )

@app.route("/api/soccer_news")
def api_soccer_news():
    """Jリーグニュースのサイトから記事を入手して、ランダムに1件返却します."""

    # 1. JリーグニュースのHTMLを取得する 
    with urlopen("https://www.jleague.jp/news/") as res:
        html = res.read().decode("utf-8")

    # 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")

    # 3. 記事一覧を取得する
    Jnews_list = soup.select("a").string
    print(Jnews_list)

    #4. ランダムに1件取得する
    Jnews = random.choice(Jnews_list)
    print(Jnews)

    # 5. JSON形式で返却する.
    return json.dumps(
        {
            "content" : Jnews["title"],
            "link" : Jnews["href"]
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=5004)