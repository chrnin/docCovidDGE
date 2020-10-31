#!/usr/bin/python3
from lxml import html, etree
import json, time, urllib.request
   
def main():
  allQuestions = []
  content = getContent()
  for c in content['helpcenterData']['containers']:
    url = 'https://info-entreprises-covid19.economie.gouv.fr/kb/guide/fr/' + str(c['id'])
    article = getArticle(url)
    if article != None: 
      content = getContentFromArticle(article)
      path = getPathFromArticle(article)
      if len(content) > 0:
        allQuestions.append({
          'titre': c['title'],
          'chemin': path[:int(len(path)/2)],
          'contenu': [c for c in content if c != '']
        })
  with open('data.json', 'w') as f:
    json.dump(allQuestions, f, indent=4)
  

def getArticle(url):
  try:
    with urllib.request.urlopen(url) as response:
      data = str(response.read())
      tree = html.fromstring(data)
    return tree
  except:
    return None

def getContentFromArticle(tree):
  raw = ''.join(tree.xpath("//script[@id='server-app-state']/text()")).encode('utf-8').decode('unicode_escape').replace("undefined",'"undefined"')
  text = raw.encode('raw_unicode_escape')
  content = json.loads(text)
  articles = []
  for c in content['explanationToDisplay']['contents']:
    articles.append(c['content'])
  return articles

def getPathFromArticle(tree):
  return [a.encode('utf-8').decode('unicode_escape') for a in tree.xpath("//a[contains(@class, 'ExplanationTop__Crumb')]/text()")]

def getContent():
  with urllib.request.urlopen("https://info-entreprises-covid19.economie.gouv.fr/kb") as response:
    data = str(response.read())
    tree = html.fromstring(data)
    return json.loads(''.join(tree.xpath("//script[@id='server-app-state']/text()")).encode('utf-8').decode('unicode_escape'))

if __name__ == "__main__":
    main()