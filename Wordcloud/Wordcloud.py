from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import jieba
import pymysql

connect = pymysql.connect(
            host='127.0.0.1',
            db='Scrapy_test',
            user='root',
            passwd='password',
            charset='utf8',
            use_unicode=True)

cursor = connect.cursor()

sql = 'select intro from Scrapy_test.novel'
cursor.execute(sql)
result = cursor.fetchall()
txt = ''
for r in result:
    txt += r[0].strip()

# 此处error参数因为直接读取报错，主要因为文本不是unicode编码
# 更好的解决办法时chardet探测编码方式
# test = open('择天记.txt', 'rb').read()
wordlist = jieba.cut(txt)
ptxt = ' '.join(wordlist)

image = numpy.array(Image.open('Girl.png'))
wc = WordCloud(background_color='white', max_words=500, mask=image, max_font_size=60, font_path='FangSong_GB2312.ttf').generate(ptxt)
plt.imshow(wc)
plt.axis("off")
plt.show()
