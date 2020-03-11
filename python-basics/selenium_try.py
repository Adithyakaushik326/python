{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "import requests\n",
    "driver = webdriver.Chrome(r'D:\\Projects\\chromedriver.exe')\n",
    "driver.get(\"https://www.vtu4u.com/\")\n",
    "driver.find_element_by_id('usn').send_keys('1rn17is001')\n",
    "driver.find_element_by_id('syl3').click()\n",
    "driver.find_element_by_class_name(\"btn-home-search\").click();\n",
    "u=driver.current_url\n",
    " # s = driver.page_source\n",
    "# var = requests.get(u)\n",
    "# text = var.text\n",
    "# # print(text)\n",
    "# soup=BeautifulSoup(text)\n",
    "# for link in soup.find('div', attrs = {'class':'col-xs-4 ritbd'}).findAll('b'):\n",
    "#     val = link.get('string')\n",
    "    \n",
    "# print(s)"
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
