{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = open('adi.txt','r')\n",
    "lines= file.read()\n",
    "dic={}\n",
    "line =(lines.lower().split(\" \"))\n",
    "for x in line:\n",
    "    if x in dic:\n",
    "        dic[x]+=1\n",
    "    else:\n",
    "        dic[x]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "ans = lambda x,y : x*y\n",
    "\n",
    "print(ans(5,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'introduced': 2,\n",
       " 'to': 13,\n",
       " 'the': 27,\n",
       " 'rss': 2,\n",
       " 'at': 1,\n",
       " 'age': 1,\n",
       " 'of': 10,\n",
       " 'eight,': 1,\n",
       " 'beginning': 1,\n",
       " 'a': 9,\n",
       " 'long': 1,\n",
       " 'association': 1,\n",
       " 'with': 2,\n",
       " 'organisation.': 1,\n",
       " 'modi': 7,\n",
       " 'left': 1,\n",
       " 'home': 1,\n",
       " 'after': 1,\n",
       " 'finishing': 1,\n",
       " 'high-school': 1,\n",
       " 'in': 14,\n",
       " 'part': 1,\n",
       " 'due': 2,\n",
       " 'an': 1,\n",
       " 'arranged': 1,\n",
       " 'marriage': 1,\n",
       " 'jashodaben': 1,\n",
       " 'chimanlal,': 1,\n",
       " 'which': 3,\n",
       " 'he': 6,\n",
       " 'abandoned': 1,\n",
       " 'and': 11,\n",
       " 'publicly': 1,\n",
       " 'acknowledged': 1,\n",
       " 'only': 1,\n",
       " 'many': 1,\n",
       " 'decades': 1,\n",
       " 'later.': 1,\n",
       " 'travelled': 1,\n",
       " 'around': 1,\n",
       " 'india': 1,\n",
       " 'for': 5,\n",
       " 'two': 1,\n",
       " 'years': 1,\n",
       " 'visited': 1,\n",
       " 'number': 1,\n",
       " 'religious': 1,\n",
       " 'centres': 1,\n",
       " 'before': 1,\n",
       " 'returning': 1,\n",
       " 'gujarat.': 1,\n",
       " '1971': 1,\n",
       " 'became': 1,\n",
       " 'full-time': 1,\n",
       " 'worker': 1,\n",
       " 'rss.': 1,\n",
       " 'during': 1,\n",
       " 'state': 1,\n",
       " 'emergency': 1,\n",
       " 'imposed': 1,\n",
       " 'across': 2,\n",
       " 'country': 1,\n",
       " '1975,': 1,\n",
       " 'was': 3,\n",
       " 'forced': 1,\n",
       " 'go': 1,\n",
       " 'into': 1,\n",
       " 'hiding.': 1,\n",
       " 'assigned': 1,\n",
       " 'him': 1,\n",
       " 'bjp': 2,\n",
       " '1985': 1,\n",
       " 'held': 1,\n",
       " 'several': 1,\n",
       " 'positions': 1,\n",
       " 'within': 1,\n",
       " 'party': 3,\n",
       " 'hierarchy': 1,\n",
       " 'until': 1,\n",
       " '2001,': 1,\n",
       " 'rising': 1,\n",
       " 'rank': 1,\n",
       " 'general': 3,\n",
       " 'secretary.\\n\\nmodi': 1,\n",
       " 'appointed': 1,\n",
       " 'chief': 2,\n",
       " 'minister': 1,\n",
       " 'gujarat': 2,\n",
       " '2001': 1,\n",
       " 'keshubhai': 1,\n",
       " \"patel's\": 1,\n",
       " 'failing': 2,\n",
       " 'health': 1,\n",
       " 'poor': 1,\n",
       " 'public': 1,\n",
       " 'image': 1,\n",
       " 'following': 1,\n",
       " 'earthquake': 1,\n",
       " 'bhuj.': 1,\n",
       " 'elected': 1,\n",
       " 'legislative': 1,\n",
       " 'assembly': 1,\n",
       " 'soon': 1,\n",
       " 'after.': 1,\n",
       " 'his': 6,\n",
       " 'administration': 5,\n",
       " 'has': 5,\n",
       " 'been': 2,\n",
       " 'considered': 1,\n",
       " 'complicit': 1,\n",
       " '2002': 1,\n",
       " 'riots[a]': 1,\n",
       " 'or': 2,\n",
       " 'otherwise': 1,\n",
       " 'criticised': 2,\n",
       " 'its': 1,\n",
       " 'handling': 1,\n",
       " 'it.': 1,\n",
       " 'supreme': 1,\n",
       " 'court-appointed': 1,\n",
       " 'special': 2,\n",
       " 'investigation': 1,\n",
       " 'team': 1,\n",
       " 'found': 1,\n",
       " 'no': 1,\n",
       " 'evidence': 1,\n",
       " 'initiate': 1,\n",
       " 'prosecution': 1,\n",
       " 'proceedings': 1,\n",
       " 'against': 1,\n",
       " 'personally.[b]': 1,\n",
       " 'policies': 1,\n",
       " 'as': 2,\n",
       " 'minister,': 1,\n",
       " 'credited': 1,\n",
       " 'encouraging': 1,\n",
       " 'economic': 1,\n",
       " 'growth,': 1,\n",
       " 'have': 1,\n",
       " 'received': 1,\n",
       " 'praise.[10]': 1,\n",
       " 'significantly': 1,\n",
       " 'improve': 2,\n",
       " 'health,': 1,\n",
       " 'poverty': 1,\n",
       " 'education': 1,\n",
       " 'indices': 1,\n",
       " 'state.[c]\\n\\nmodi': 1,\n",
       " 'led': 1,\n",
       " '2014': 1,\n",
       " 'election': 1,\n",
       " 'gave': 1,\n",
       " 'majority': 1,\n",
       " 'indian': 2,\n",
       " 'lower': 1,\n",
       " 'house': 1,\n",
       " 'parliament,': 1,\n",
       " 'lok': 1,\n",
       " 'sabha,': 1,\n",
       " 'first': 1,\n",
       " 'time': 1,\n",
       " 'any': 1,\n",
       " 'single': 1,\n",
       " 'since': 1,\n",
       " '1984.': 1,\n",
       " \"modi's\": 1,\n",
       " 'tried': 1,\n",
       " 'raise': 1,\n",
       " 'foreign': 1,\n",
       " 'direct': 1,\n",
       " 'investment': 1,\n",
       " 'economy': 1,\n",
       " 'reduced': 1,\n",
       " 'spending': 1,\n",
       " 'on': 1,\n",
       " 'healthcare': 1,\n",
       " 'social': 1,\n",
       " 'welfare': 1,\n",
       " 'programmes.': 1,\n",
       " 'attempted': 1,\n",
       " 'efficiency': 1,\n",
       " 'bureaucracy;': 1,\n",
       " 'centralised': 1,\n",
       " 'power': 1,\n",
       " 'by': 1,\n",
       " 'abolishing': 1,\n",
       " 'planning': 1,\n",
       " 'commission.': 1,\n",
       " 'began': 1,\n",
       " 'high-profile': 1,\n",
       " 'sanitation': 1,\n",
       " 'campaign': 1,\n",
       " 'weakened': 1,\n",
       " 'abolished': 1,\n",
       " 'environmental': 1,\n",
       " 'labour': 1,\n",
       " 'laws.': 1,\n",
       " 'initiated': 1,\n",
       " 'controversial': 1,\n",
       " 'demonetisation': 1,\n",
       " 'high-denomination': 1,\n",
       " 'banknotes.\\n\\nfollowing': 1,\n",
       " \"party's\": 1,\n",
       " 'victory': 1,\n",
       " '2019': 1,\n",
       " 'election,': 1,\n",
       " 'revoked': 1,\n",
       " 'status': 1,\n",
       " 'jammu': 1,\n",
       " 'kashmir.': 1,\n",
       " 'also': 1,\n",
       " 'citizenship': 1,\n",
       " 'amendment': 1,\n",
       " 'act,': 1,\n",
       " 'resulted': 1,\n",
       " 'widespread': 1,\n",
       " 'protests': 1,\n",
       " 'country.\\n\\ndescribed': 1,\n",
       " 'engineering': 1,\n",
       " 'political': 1,\n",
       " 'realignment': 1,\n",
       " 'towards': 1,\n",
       " 'right-wing': 1,\n",
       " 'politics,': 1,\n",
       " 'remains': 1,\n",
       " 'figure': 1,\n",
       " 'controversy': 1,\n",
       " 'domestically': 1}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, '1971'), (1, '1975,'), (1, '1984.'), (1, '1985'), (1, '2001'), (1, '2001,'), (1, '2002'), (1, '2014'), (1, '2019'), (1, 'abandoned'), (1, 'abolished'), (1, 'abolishing'), (1, 'acknowledged'), (1, 'act,'), (1, 'after'), (1, 'after.'), (1, 'against'), (1, 'age'), (1, 'also'), (1, 'amendment'), (1, 'an'), (1, 'any'), (1, 'appointed'), (1, 'around'), (1, 'arranged'), (1, 'assembly'), (1, 'assigned'), (1, 'association'), (1, 'at'), (1, 'attempted'), (1, 'banknotes.\\n\\nfollowing'), (1, 'became'), (1, 'before'), (1, 'began'), (1, 'beginning'), (1, 'bhuj.'), (1, 'bureaucracy;'), (1, 'by'), (1, 'campaign'), (1, 'centralised'), (1, 'centres'), (1, 'chimanlal,'), (1, 'citizenship'), (1, 'commission.'), (1, 'complicit'), (1, 'considered'), (1, 'controversial'), (1, 'controversy'), (1, 'country'), (1, 'country.\\n\\ndescribed'), (1, 'court-appointed'), (1, 'credited'), (1, 'decades'), (1, 'demonetisation'), (1, 'direct'), (1, 'domestically'), (1, 'during'), (1, 'earthquake'), (1, 'economic'), (1, 'economy'), (1, 'education'), (1, 'efficiency'), (1, 'eight,'), (1, 'elected'), (1, 'election'), (1, 'election,'), (1, 'emergency'), (1, 'encouraging'), (1, 'engineering'), (1, 'environmental'), (1, 'evidence'), (1, 'figure'), (1, 'finishing'), (1, 'first'), (1, 'following'), (1, 'forced'), (1, 'foreign'), (1, 'found'), (1, 'full-time'), (1, 'gave'), (1, 'go'), (1, 'growth,'), (1, 'gujarat.'), (1, 'handling'), (1, 'have'), (1, 'health'), (1, 'health,'), (1, 'healthcare'), (1, 'held'), (1, 'hiding.'), (1, 'hierarchy'), (1, 'high-denomination'), (1, 'high-profile'), (1, 'high-school'), (1, 'him'), (1, 'home'), (1, 'house'), (1, 'image'), (1, 'imposed'), (1, 'india'), (1, 'indices'), (1, 'initiate'), (1, 'initiated'), (1, 'into'), (1, 'investigation'), (1, 'investment'), (1, 'it.'), (1, 'its'), (1, 'jammu'), (1, 'jashodaben'), (1, 'kashmir.'), (1, 'keshubhai'), (1, 'labour'), (1, 'later.'), (1, 'laws.'), (1, 'led'), (1, 'left'), (1, 'legislative'), (1, 'lok'), (1, 'long'), (1, 'lower'), (1, 'majority'), (1, 'many'), (1, 'marriage'), (1, 'minister'), (1, 'minister,'), (1, \"modi's\"), (1, 'no'), (1, 'number'), (1, 'on'), (1, 'only'), (1, 'organisation.'), (1, 'otherwise'), (1, 'parliament,'), (1, 'part'), (1, \"party's\"), (1, \"patel's\"), (1, 'personally.[b]'), (1, 'planning'), (1, 'policies'), (1, 'political'), (1, 'politics,'), (1, 'poor'), (1, 'positions'), (1, 'poverty'), (1, 'power'), (1, 'praise.[10]'), (1, 'proceedings'), (1, 'programmes.'), (1, 'prosecution'), (1, 'protests'), (1, 'public'), (1, 'publicly'), (1, 'raise'), (1, 'rank'), (1, 'realignment'), (1, 'received'), (1, 'reduced'), (1, 'religious'), (1, 'remains'), (1, 'resulted'), (1, 'returning'), (1, 'revoked'), (1, 'right-wing'), (1, 'riots[a]'), (1, 'rising'), (1, 'rss.'), (1, 'sabha,'), (1, 'sanitation'), (1, 'secretary.\\n\\nmodi'), (1, 'several'), (1, 'significantly'), (1, 'since'), (1, 'single'), (1, 'social'), (1, 'soon'), (1, 'spending'), (1, 'state'), (1, 'state.[c]\\n\\nmodi'), (1, 'status'), (1, 'supreme'), (1, 'team'), (1, 'time'), (1, 'towards'), (1, 'travelled'), (1, 'tried'), (1, 'two'), (1, 'until'), (1, 'victory'), (1, 'visited'), (1, 'weakened'), (1, 'welfare'), (1, 'widespread'), (1, 'within'), (1, 'worker'), (1, 'years'), (2, 'across'), (2, 'as'), (2, 'been'), (2, 'bjp'), (2, 'chief'), (2, 'criticised'), (2, 'due'), (2, 'failing'), (2, 'gujarat'), (2, 'improve'), (2, 'indian'), (2, 'introduced'), (2, 'or'), (2, 'rss'), (2, 'special'), (2, 'with'), (3, 'general'), (3, 'party'), (3, 'was'), (3, 'which'), (5, 'administration'), (5, 'for'), (5, 'has'), (6, 'he'), (6, 'his'), (7, 'modi'), (9, 'a'), (10, 'of'), (11, 'and'), (13, 'to'), (14, 'in'), (27, 'the')]\n"
     ]
    }
   ],
   "source": [
    "print((sorted(zip(dic.values(),dic.keys()))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(360, 480)\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "img = Image.open(\"m.jpg\")\n",
    "print(img.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "JPEG\n"
     ]
    }
   ],
   "source": [
    "print(img.format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "img.show()"
   ]
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
