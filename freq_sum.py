import nltk, time
"""
Mention the absolute path of NLTK data directory.
"""
nltk.data.path.append('')
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import time,sys

start_time = time.time()
for x in range(0,1):
    pass
    tme={"t1": 0.0, "t2": 0.0, "t3": 0.0, "t4": 0.0}
    counter={"i1":0, "i2":0, "i3":0, "i4":0}
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    from bs4 import BeautifulSoup

    class FrequencySummarizer:
      def __init__(self, min_cut=0.2, max_cut=0.6):
        #print("in __init__")
        start_time = time.time()
        global t1
        global i1
        counter["i1"]+=1
        """
         Initilize the text summarizer.
         Words that have a frequency term lower than min_cut 
         or higer than max_cut will be ignored.
        """
        self._min_cut = min_cut
        self._max_cut = max_cut 
        self._stopwords = set(stopwords.words('english') + list(punctuation))
        tme["t1"]+=time.time() - start_time
        #print("out __init__")
        #print("sleep")
        #time.sleep(5)

      def _compute_frequencies(self, word_sent):
        #print("in _compute_frequencies")
        start_time = time.time()
        global t2
        global i2
        counter["i2"]+=1
        """ 
          Compute the frequency of each of word.
          Input: 
           word_sent, a list of sentences already tokenized.
          Output: 
           freq, a dictionary where freq[w] is the frequency of w.
        """
        freq = defaultdict(int)
        for s in word_sent:
          for word in s:
            #print(word)
            if word not in self._stopwords:
              freq[word] += 1
        
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        
        for w in list(freq):
          freq[w] = freq[w]/m
          #print(freq[w])
          if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
            del freq[w]
        tme["t2"]+=time.time() - start_time 
        #print("out _compute_frequencies ")
        #print("sleep")
        #time.sleep(5)   
        return freq

      def summarize(self, text, n):
        #print("in summarize")
        start_time = time.time()
        global t3
        global i3
        counter["i3"]+=1
        """
          Return a list of n sentences 
          which represent the summary of text.
        """
        sents = text
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        #print(ranking.keys())
        #for count, value in enumerate(word_sent,1):
    		#print(count, value)
        for i,sent in enumerate(word_sent):	
          for w in sent:
            if w in self._freq:
              #print(w)
              ranking[i] += self._freq[w]
        
        sents_idx = self._rank(ranking, n)
        
        #print("after nlargest....sleep")
        #time.sleep(5) 
        tme["t3"]+=time.time() - start_time
        
        #print("out summarize")
        #print("sleep")
        #time.sleep(5)    
        return [sents[j] for j in sents_idx]

      def _rank(self, ranking, n):
        #print("in rank")
        start_time = time.time()
        global t4
        global i4
        counter["i4"]+=1
        """ return the first n sentences with highest ranking """
        tme["t4"]+=time.time() - start_time
        
        #print("out rank")
        #print("sleep")
        #time.sleep(5)
        return nlargest(n, ranking, key=ranking.get)
        
    inp = sys.argv[1]
    out = sys.argv[2]
    length = sys.argv[3]
    fil = open(inp,"r")
    text = fil.readlines()
    fs = FrequencySummarizer()

    save = open(out,"w")

    for s in fs.summarize(text,int(length)):
        save.write(s)
    save.close()
    
print("Finished in %s seconds." % (time.time() - start_time))   
