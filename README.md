# NovelSpiderAndWordcloud

### 目标：爬取起点小说X类型小说前X页的所有小说并将所有简介做成词云

### power by：
1. Python 3.6
2. Scrapy 1.4
3. pymysql 
4. wordcloud
5. jieba
6. pillow
7. macOS 10.12.6

#### Blog：http://blog.csdn.net/sinat_34200786/article/details/78090649

---

### How to use ?

```
git clone https://github.com/Dengqlbq/NovelSpiderAndWordcloud.git
```
```
cd QiDian
```
```
scrapy crawl qi_dian_novel_spider
```
```
cd ../Wordcloud
```
```
python3 Wordcloud.py
```

---
### Achievement：
#### Collected:<br>

![Start](https://github.com/Dengqlbq/NovelSpiderAndWordcloud/blob/master/Show/3.png)

![ShowData](https://github.com/Dengqlbq/NovelSpiderAndWordcloud/blob/master/Show/4.png)

![SaveData](https://github.com/Dengqlbq/NovelSpiderAndWordcloud/blob/master/Show/5.png)
#### Wordcloud：<br>

![Before](https://github.com/Dengqlbq/NovelSpiderAndWordcloud/blob/master/Show/Girl.png)

![After](https://github.com/Dengqlbq/NovelSpiderAndWordcloud/blob/master/Show/15.png)
