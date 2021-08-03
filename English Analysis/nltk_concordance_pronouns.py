Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.cwd
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.cwd
AttributeError: module 'os' has no attribute 'cwd'
>>> os.getcwd()
'C:\\Program Files\\Python38'
>>> os.chdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets\\\\English Analysis)
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets\\)
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets\\\\English Analysis')
>>> os.getcwd()
'C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets\\English Analysis'
>>> f=open('allEn-03-2020-TweetText.txt', 'r', encoding="utf-8")
>>> raw= f.read()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    raw= f.read()
  File "C:\Program Files\Python38\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
MemoryError
>>> raw= f.read()
>>> tokens = word_tokenize(raw)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tokens = word_tokenize(raw)
NameError: name 'word_tokenize' is not defined
>>> import nltk
fr
>>> from nltk import *
>>> tokens = word_tokenize(raw)
>>> text = nltk.Text(tokens)
>>> print("Hello
        
             
