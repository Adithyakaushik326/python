{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://in.bookmyshow.com/bengaluru/movies/love-mocktail/ET00124382\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/love-mocktail-et00124382-21-01-2020-11-18-56.jpg\n",
      "https://in.bookmyshow.com/bengaluru/movies/ayyappanum-koshiyum/ET00123631\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/ayyappanum-koshiyum-et00123631-11-01-2020-02-03-02.jpg\n",
      "https://in.bookmyshow.com/bengaluru/movies/varane-avashyamund/ET00124501\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/varane-avashyamund-et00124501-22-01-2020-01-30-37.jpg\n",
      "https://in.bookmyshow.com/bengaluru/movies/world-famous-lover/ET00112147\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/world-famous-lover-et00112147-17-09-2019-01-20-33.jpg\n",
      "https://in.bookmyshow.com/bengaluru/movies/love-aaj-kal/ET00099651\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/love-aaj-kal-2-et00099651-26-03-2019-05-59-03.jpg\n",
      "https://in.bookmyshow.com/bengaluru/movies/oh-my-kadavule/ET00126103\n",
      "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/oh-my-kadavule-et00126103-07-02-2020-12-38-52.jpg\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import urllib\n",
    "import random\n",
    "def crawler(pages):\n",
    "    url='https://in.bookmyshow.com/bengaluru' \n",
    "    var = requests.get(url)\n",
    "    text=var.text\n",
    "    soup=BeautifulSoup(text)\n",
    "    for link in soup.find('div', attrs = {'class':'cards-list'}).findAll('a'):\n",
    "#         print(link.prettify()) \n",
    "        href=link.get('href')\n",
    "        src=link.find('img')\n",
    "        image = src.get('data-src')\n",
    "        print('https://in.bookmyshow.com/'+href)\n",
    "        print(image)  \n",
    "        name = href[17:]\n",
    "        i=name.index('/')\n",
    "        pic= name[:i]\n",
    "        u=r'D:\\Projects\\python practice\\bms/'+pic\n",
    "        urllib.request.urlretrieve('https:'+image,u+'.jpg')  \n",
    "       \n",
    "crawler(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
