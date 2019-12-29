import urllib.request
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

r = urllib.request.urlopen('https://www.lyrics.com/lyric/836985/The+Beatles/Please+Mister+Postman')
soup = BeautifulSoup(r.read(), "html.parser")
text = soup.findAll("pre", {"id": "lyric-body-text"})[0].text
print(text)

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()