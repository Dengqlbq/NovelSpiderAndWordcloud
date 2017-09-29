from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import jieba
import pymysql

connect = pymysql.connect(
            host='127.0.0.1',
            db='Scrapy_test',
            user='Your_User',
            passwd='Your_pass',
            charset='utf8',
            use_unicode=True)

cursor = connect.cursor()

sql = 'select intro from Scrapy_test.novel'
cursor.execute(sql)
result = cursor.fetchall()

txt = ''
for r in result:
    txt += r[0].strip()


wordlist = jieba.cut(txt)
ptxt = ' '.join(wordlist)

image = numpy.array(Image.open('Girl.png'))
wc = WordCloud(background_color='white', max_words=500, mask=image, max_font_size=60, font_path='FangSong_GB2312.ttf').generate(ptxt)

plt.imshow(wc)
plt.axis("off")
plt.show()
