from flask import Flask, render_template, jsonify, url_for, redirect, request
import requests

api_key="92b1ffbe2e0b485cbd3411a9a08decf2"

app=Flask(__name__)

#Function to fetch top news of India
def fetch_top_india():
  url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
  response=requests.get(url)
  if response.status_code==200:
    data=response.json()
    articles=data.get('articles',[])
  else:
    articles=[]
  return articles

#Function to fetch top new od the world
def fetch_top_world():
    all_articles = []
    countries = ['us', 'au']
    for country in countries:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])[:5]
            all_articles.extend(articles)
    return all_articles  # Return list of articles


#Function to fetch top news category wise
def fetch_category_news(category):
  url=f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}'
  response=requests.get(url)
  if response.status_code==200:
    data=response.json()
    articles=data.get('articles',[])
  else:
    articles=[]
  return articles



@app.route('/')
def index():
  top_india=fetch_top_india()
  top_world=fetch_top_world()
  category=['sports','business','entertainment','health','science','technology']
  sports_news=fetch_category_news(category[0])
  business_news=fetch_category_news(category[1])
  entertainment_news=fetch_category_news(category[2])
  health_news=fetch_category_news(category[3])
  science_news=fetch_category_news(category[4])
  tech_news=fetch_category_news(category[5])
  return render_template('index.html',top_india=top_india,top_world=top_world,sports_news=sports_news,business_news=business_news,entertainment_news=entertainment_news,health_news=health_news,science_news=science_news,tech_news=tech_news)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return redirect(url_for('index'))
    response = requests.get(f'https://newsapi.org/v2/everything', params={
        'q': query,
        'apiKey': api_key
    })
    search_results = response.json().get('articles', [])
    
    return render_template('search.html', articles=search_results, query=query)



if __name__=='__main__':
  app.run()

