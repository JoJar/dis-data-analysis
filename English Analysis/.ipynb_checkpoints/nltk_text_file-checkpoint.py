Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> f = open('PutinKremlinOligarchRussiaText.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f = open('PutinKremlinOligarchRussiaText.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'PutinKremlinOligarchRussiaText.txt'
>>> import os
>>> os.getcwd()
'C:\\Program Files\\Python38'
>>> os.chdir('C:\Users\c1635922\OneDrive - Cardiff University\Documents\Dissertation\datasets)
	 
SyntaxError: EOL while scanning string literal
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Program Files\\Python38'
>>> os.cgdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.cgdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets')
AttributeError: module 'os' has no attribute 'cgdir'
>>> os.chdir('C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets')
>>> os.getcwd()
'C:\\Users\\c1635922\\OneDrive - Cardiff University\\Documents\\Dissertation\\datasets'
>>> f = open('PutinKremlinOligarchRussiaText.txt')
>>> f.concordance("putin")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    f.concordance("putin")
AttributeError: '_io.TextIOWrapper' object has no attribute 'concordance'
>>> print(f.read())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(f.read())
  File "C:\Program Files\Python38\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1046: character maps to <undefined>
>>> f.read()
''
>>> f = open('PutinKremlinOligarchRussiaText.txt', 'rU')

Warning (from warnings module):
  File "<pyshell#14>", line 1
DeprecationWarning: 'U' mode is deprecated
>>> f = open('PutinKremlinOligarchRussiaText.txt', 'r')
>>> for line in f:
	print(line.strip())

	
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for line in f:
  File "C:\Program Files\Python38\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1046: character maps to <undefined>
>>> f = open('PutinKremlinOligarchRussiaText.txt', ,encoding='utf-8', 'r')
SyntaxError: invalid syntax
>>> f = open('PutinKremlinOligarchRussiaText.txt', encoding='utf-8', 'r')
SyntaxError: positional argument follows keyword argument
>>> f = open('PutinKremlinOligarchRussiaText.txt','r', encoding='utf-8')
>>> raw = f.read()
>>> type(raw)
<class 'str'>
>>> tokens = word_tokenize(raw)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tokens = word_tokenize(raw)
NameError: name 'word_tokenize' is not defined
>>> from nltk import *
>>> tokens = word_tokenize(raw)
>>> tokens.concordance("putin")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tokens.concordance("putin")
AttributeError: 'list' object has no attribute 'concordance'
>>> words = [w.lower() for w in tokens]
>>> vocab = sorted(set(words))
>>> type(vocab)
<class 'list'>
>>> print(vocab)

>>> text = nltk.Text(tokens)
>>> type(text)
<class 'nltk.text.Text'>
>>> text.collocations()
See Openings; Virus Spreads; disinformation campaigns; wage
disinformation; fake news; U.S. and…; coronavirus outbreak;
Disinformation https; Russia See; United States; sow doubts; another
opportunity; populist politicians; finding willing; Moscow ha…; claim
Beijing; Anti-NATO Influence; Influence Ops; Pushing Coronavirus;
coronavirus gives
>>> text.dispersion_plot(["russia", "democracy", "virus", "Putin"])
>>> d_plot = text.dispersion_plot(["russia", "democracy", "virus", "Putin"])
>>> d_plot
>>> d_plot()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d_plot()te
TypeError: 'NoneType' object is not callable
>>> print(d_plot)
None
>>> def lexical_diversity(text):
	return len(set(text))/len(text)

>>> def percentage(count, total):
	return 100 * count / total

>>> lexical_diversity(text)
0.06652276433255516
>>> V = set(text)
>>> long_words = [w for w in V if len(w) > 6]
>>> sorted(long_words)

>>> fdist1 = FreqDist(text)
>>> sorted(w for w in set(text) if len(w) > 7 and fdist1[w] > 7)
["'Liberal", '//t.co/2cnvSDxjXn', '//t.co/2nqnS4p56h', '//t.co/48PzpBWNrH', '//t.co/4HmGvdm8oU', '//t.co/6OqD4WGrZ5', '//t.co/8e64RJE1mc', '//t.co/9L4k2jp1bh', '//t.co/9eQLu6QcXD', '//t.co/BeXLsXPnJI', '//t.co/BmkzBAUu9V', '//t.co/CR0zxLYln8', '//t.co/CcpBpWYD9i', '//t.co/Ga6QQHNuR8', '//t.co/GkVT02JHAQ', '//t.co/IymjBviV9Z', '//t.co/K9gvpnyuTM', '//t.co/KzcfAyd6Kt', '//t.co/NenQlTa8Ok', '//t.co/OiJ4NDqNtf', '//t.co/RAKCg5k…', '//t.co/RieHHGcK7k', '//t.co/Shy9d4MWur', '//t.co/Ukn6bqD3Ap', '//t.co/Vo7hKgZix2', '//t.co/W4A3KPBR6E', '//t.co/ZrnQbL95s0', '//t.co/ajtnzjpRzT', '//t.co/cIZak4wj8Z', '//t.co/dDu…', '//t.co/eF8PXPxxMM', '//t.co/eMduY2…', '//t.co/f5QfJFPSBZ', '//t.co/fLCpt8yD18', '//t.co/g6qJwIZZir', '//t.co/g9wFwHwuBB', '//t.co/h1Qy8CS3…', '//t.co/kPm6TTCYih', '//t.co/l9hpoRIUX7', '//t.co/r3kXT5J4Ww', '//t.co/s5UdDbVKWa', '//t.co/ttiY7iPw0K', '//t.co/ttiY7j76Si', '//t.co/xaBzgGVqLi', '//t.co/z8YAfJC8NW', '//t.co/…', 'ALT_uscis', 'AP_Europe', 'Absolutely', 'According', 'Actually', 'AdamParkhomenko', 'Airspace', 'AlexandraChalup', 'AllMattNYT', 'Although', 'Alyssa_Milano', 'Ambassador', "America's", 'American', 'Americans', 'Analysis', 'Anglophone', 'Anti-NATO', 'Apparently', 'Atlantic', 'AtlanticCouncil', 'BREAKING', 'BULLSHIT', 'BenKTallmadge', 'BenjaminNorton', "Bernie's", 'BernieSanders', 'Biden2020', 'Billbrowder', 'BobRmhenry1', 'BorisJohnson', 'Breaking', 'BreitbartNews', 'Buckaye1', 'BulletinAtomic', 'CIA/deep', 'CNNPolitics', 'COMMENTATORS', 'CONSPIRACY', 'COVID-19', 'COVIDー19', 'Campaign', 'Canadian', 'ChrisCuomo', 'Collusion', 'ColumbiaBugle', 'ComfortablySmug', 'Commentary', 'Communist', 'Computational', 'Conditions', 'Confusion', 'Congress', 'Conspiracy', 'Continued', 'Coronaviruis', 'Coronavirus', 'CoronavirusPandemic', 'Corporation', 'Covid-19', 'Covington', 'Creativity', 'DIRECTIONS', 'DISINFORMATION', 'DLongsamson', 'DailyCaller', 'Dangerous', 'DarthPutinKGB', 'DaveKeating', 'DavidAgStone', 'DavidKlion', 'DefTechPat', 'DefendDemocracy', 'DefenseOne', 'Democracy', 'Democrat', 'Democratic', 'Democrats', 'Department', 'Disinfo_Digest', 'Disinformation', 'DonaldJTrumpJr', 'Downplaying', 'DwightCooper16', 'ECochnar', 'EUvsDisinfo', 'Editorial', 'Education4Libs', 'Election', 'Employed', 'EricBoehlert', 'EricTrump', 'Establishment', 'EuromaidanPress', 'European', 'EuropeanUnion', 'Europeans', 'Everyone', 'Everything', 'Evidence', 'Exploits', 'FRishmawy', 'Facebook', 'FakeNews', 'Farnesina', 'Fascinating', 'FearIsNotPanic', 'February', 'FitzInfo', 'Flashback', 'FliedGaff', 'FriendsofPutin', 'GOPLeader', 'GaleTStrong', 'General_Qanah', 'GianandreaGaian', 'Globalist', 'GovHowardDean', 'GovWhitmer', 'Government', 'Greenwald', 'HKrassenstein', 'Hannity—who', 'HillaryClinton', 'Humanitarian', 'IBelieveTara', 'IlvesToomas', 'Impeachment', 'IndiaToday', 'Influence', 'InformNapalm', 'IngrahamAngle', 'Insurance', 'Intelligence', 'Intercept', 'Interesting', 'Interference', 'IsabelO20183051', 'Italians', 'IvankaTrump', 'J_fassler', 'JackPosobiec', 'JayRouseDC', 'Jay_D007', 'JeremyKonyndyk', 'JoeBiden', 'JohnCornyn', 'Jordan_Sather_', 'JoyAnnReid', 'JuliaDavisNews', 'JulianRoepcke', 'KaranKanishk', 'Kavanaugh', 'KirkseniyaSF', 'Know_More_News', 'KremlinRussia', "L'ottanta", 'LaStampa', 'Lawmakers', 'Leskevicius', 'LindaKWS1', 'Linkiesta', 'Lombardy', 'MISINFORMATION', 'MSignorile', 'Mainstream', 'MalcolmNance', 'Malinka1102', 'MarkGaleotti', 'MattWolking', 'MaximEristavi', 'Meanwhile', 'Measures', 'MikeOkuda', 'Misinformation', "Moscow's", 'NYGovCuomo', 'NathanJRobinson', 'National', 'Newsweek', 'November', 'Novembe…', 'Ohra_aho', 'Oligarch', 'Openings', 'Orthodox', 'PR/propaganda', 'PROPAGANDA', 'PalmerReport', 'Pandemic', 'Patriots', 'PepperOceanna', 'Politico', 'Politics_PR', 'PoliticusSarah', 'PostOpinions', 'Postings', 'President', 'Probably', 'Propaganda', 'RANDCorporation', 'RaniaKhalek', 'ReadeAlexandra', 'RealCandaceO', 'RealSaavedra', 'ReflectingMan', 'Remember', 'RepAdamSchiff', 'RepJimBanks', 'RepStevenSmith', 'Republic', 'Republican', 'Republicans', 'Restrictions', 'Rob_Clotworthy', 'RoguePOTUSStaff', 'RonColeman', 'RusEmbUSA', "Russia's", 'Russiagate', 'Russians', 'SallyAlbright', 'Sam_Vinograd', 'Saturday', 'ScottPresler', 'SecPompeo', 'Security', 'SenSanders', 'Seriously', 'Services', 'Shameful', 'SheWhoRises', 'SlawomirDebski', 'Smollett', 'Snowbirdsix1000', 'Something', 'SovietSunTzu', 'SpeakerPelosi', 'Spreading', 'SputnikInt', 'SpyTalker', 'StefanTompson', 'TAPSTRIMEDIA', 'TarasKuzio', 'TatAtfender', 'Teri_Kanefield', 'ThePeoplesCube', 'TheRickWilson', 'TranslateRealDT', "Trump'sAlternate", 'Trumpsters', 'TuckerCarlson', 'TwitterSafety', 'TwitterSupport', 'Ukrainian', 'UmlandAndreas', 'Unfortunately', 'VLADIMIR', 'VNotKind', 'VanessaBeeley', 'Venezuela', 'Venezuelan', 'Villains', 'Vladimir', 'Washington', 'WhiteHouse', 'Wikileaks', 'Will_Bunch', 'XSovietNews', '_JakubJanda', '_ReaalAmerican_', 'abandoned', 'absolute', 'absolutely', 'accepting', 'according', 'accountable', 'accounts', 'accurate', 'accusation', 'accusations', 'accusing', 'actively', 'actually', 'adamhousley', 'addressing', 'administration', 'admitted', 'admitting', 'advantage', 'advantageous', 'agencies', 'aggravate', 'aggressively', 'agreement', 'aligning', 'allegation', 'allegations', 'alliance', 'allowing', 'ambassador', 'amplified', 'amplifying', 'analysis', 'analyzed', 'ananavarro', 'andrewsweiss', 'ant-Russian', 'anti-American', 'anti-NATO', 'anti-Russia', 'anti-Russian', 'anti-coronavirus', 'antisemitic', 'anything', 'apologist', 'apparently', 'applying', 'appreciates', 'aroseblush', 'arrivate', 'articles', 'artificialcaged', 'assistance', 'associate', 'attacked', 'attackers', 'attacking', 'attempting', 'attention', 'audiences', 'authoritarian', 'authorities', 'badmouthing', 'basically', 'beginning', 'believed', 'believes', 'believing', 'billionaire', 'biological', 'boasting', 'boyfriend', 'brainwashed', 'brainwas…', 'briebriejoy', 'bullshit', 'business', 'campaign', 'campaigns', 'candidate', 'capitalism', 'captured', 'carljackmiller', 'carolecadwalla', 'certainly', 'challenge', 'channels', 'checking', 'children', 'chrislhayes', 'christianrocca', 'citizens', 'claiming', 'colluded', 'collusion', 'colonial', 'combined', 'comments', 'communication', 'communism', 'communist', 'community', 'companies', 'comparison', 'complaining', 'complete', 'completely', 'complicit', 'concerned', 'concluded', 'condemned', 'conference', 'confused', 'confusion', 'congressman', 'connected', 'consider', 'considered', 'conspiracies', 'conspiracy', 'constant', 'constantly', 'continuando', 'continue', 'continued', 'continues', 'controlled', 'controls', 'convenient', 'convince', 'convincing', 'coronavirus', 'coronavirus-related', 'corporate', 'corruption', "couldn't", 'countries', 'coverage', 'covering', 'covid-19', 'covid-1…', 'creating', 'credibility', 'credible', 'criminal', 'critical', 'criticism', 'criticize', 'cuarentena', 'cultists', 'dangerous', 'dbongino', 'debunked', 'defending', 'defenseone', 'definitely', 'dementia', 'democracy', 'democrat', 'democrats', 'democra…', 'deployed', 'deploying', 'designed', 'designe…', 'desperate', 'despicable', 'destabilizzano', 'destroyed', 'destroying', 'destruction', 'determined', 'dictator', 'difference', 'different', 'dino_andreani', 'directing', 'disagree', 'disarray', 'discredit', 'discredited', 'disgrace', 'disgusting', 'dishonest', 'disinformation', 'disinformation…', 'disinfor…', 'dismissed', 'disseminate', 'disseminates', 'dissonance', 'distract', 'distribute', 'distrust', 'division', 'doctored', 'document', 'domestic', 'downplaying', 'economic', 'editorial', 'effective', 'election', 'elections', 'electoral', 'emergency', 'emergenza', 'emerging', 'emerytowanego', 'en_informnapalm', 'endorsed', 'engaging', 'entirely', 'epidemic', 'equipment', 'equivalent', 'ericgarland', 'esaltat…', 'especially', 'essenviews', 'establishment', 'euroradio', 'everybody', 'everyone', "everyone's", 'everything', 'everywhere', 'evidence', 'exploiting', 'exploits', 'explores', 'exposing', 'extortion', 'extremely', 'fabrication', 'facebook', 'favorite', 'feckless', 'fighting', 'flying_rodent', 'followers', 'forniture', 'friendly', 'frustrate', 'gabrielsherman', 'ggreenwald', 'government', "government's", 'governments', 'gratitude', 'gtconway3d', 'guessing', 'gullible', 'handling', 'happened', 'happening', 'healthcare', 'homework', 'honestly', 'hospital', 'hospitals', 'humanitarian', 'hwag_ucmc', 'hysteria', 'hysterical', 'idolizes', 'ignorant', 'impeached', 'impeachment', 'impediment', 'important', 'inaccurate', 'inciting', 'including', 'incompetence', 'incompetent', 'increase', 'independent', 'infected', 'infection', 'infections', 'influence', 'information', 'informed', 'innocent', 'installed', 'institutions', 'intelligence', 'intended', 'interest', 'interesting', 'interests', 'interfere', 'interfered', 'interference', 'interferes', 'interfering', 'international', 'internet', 'interview', 'introduce', 'introduces', 'invasion', 'investigate', 'investigated', 'investigation', 'involved', 'involvement', 'its_johnmartin', 'jacopo_iacoboni', 'jaketapper', 'jeremyscahill', 'joshrogin', 'journalism', 'journalist', 'journalists', 'jsolomonReports', 'julianbarnes', 'kalenskyj', 'kasey_stricklin', 'katzsecret2', 'kgosztola', 'kilmeade', 'krystalball', 'lara_lazar', 'leadership', 'legitimizing', 'leonidragozin', 'libelous', 'liberals', 'linda72135856', 'listeners', 'listening', 'literally', 'lockdown', 'machines', 'maggieNYT', 'magnified', 'mainstream', 'majority', 'manipulated', 'manipulation', 'marcorubio', 'markmackinnon', 'markscott82', 'material', 'measures', 'meddling', 'media/methods', 'mehdirhasan', 'melbournecoal', 'messaging', 'mfa_russia', 'militare', 'military', 'millions', 'misinformation', 'misinformation…', 'misleading', 'mitchellvii', 'mongering', 'mounting', 'mouthpiece', 'movement', 'multiple', 'naadirjeewa', 'narcissistic', 'narrative', 'narratives', 'national', 'nedprice', 'neeratanden', 'negative', 'newsburko', 'newspapers', 'no_silenced', 'nonsense', 'nytpolitics', 'objective', 'obviously', 'official', 'officials', 'olgaNYC1211', 'oligarch', 'oligarchi', 'oligarchs', 'oliverdarcy', 'olliecarroll', 'openings', 'operation', 'operations', 'opportunity', 'opposite', 'opposition', 'ordering', 'organisation', 'oromariposa06', 'otherwise', 'outbreak', 'overarching', 'pandemic', 'parading', 'parroting', 'partners', 'pathetic', 'patients', 'paulmasonnews', 'paweljabIonski', 'peddling', 'personal', 'personally', 'peterjukes', 'platform', 'platforms', 'playbook', 'pneumonia', 'political', 'politicians', 'politico', 'politics', 'polonium', 'population', 'populations', 'populism', 'populist', 'positive', 'possible', 'possibly', 'post-truth', 'postings', 'powerful', 'praising', 'presence', 'presidency', 'president', 'presidential', 'pretending', 'prevalent', 'primaries', 'pro-Russian', 'probably', 'problems', 'profesora', 'prolific', 'promoted', 'promotes', 'promoting', 'propaganda', 'propagandist', 'propagandists', 'propagating', 'prostřednictvím', 'provided', 'purposes', 'pursuing', 'qualcuno', 'quarantine', 'question', 'questioned', 'questions', 'raccontava', 'rassicurare', 're-elected', 'reaction', 'realDonaldTrump', 'realTuckFrumper', 'real_defender', 'realdonaldtrump', 'realities', 'received', 'receiving', 'recently', 'recognize', 'recording', 'redsteeze', 'referring', 'regarding', 'regardless', 'reidepstein', 'relations', 'relationship', 'released', 'releasing', 'reliable', 'remember', 'reminder', 'repeatedly', 'repeating', 'reported', 'reporter', 'reporters', 'reporting', 'repubblica', 'research', 'resources', 'respected', 'responds', 'response', 'responsibility', 'responsible', 'retweeting', 'ribaltamento', 'ridiculous', 'right-wing', 'ryangrim', 'sahouraxo', 'sanction', 'sanctions', 'sandrogozi', 'sanitarie', 'seanhannity', 'security', 'senatemajldr', 'sentiment…', 'seriously', 'sexually', 'sfuttando', 'shameful', 'sharpest', 'shaunking', 'significant', 'situation', 'situazione', 'smearing', 'so-called', 'socialist', 'soldiers', 'solidarity', 'soltando', 'something', 'sometimes', 'southfronteng', 'speaking', 'spending', 'sponsored', 'spouting', 'spreading', 'standard', 'starting', 'statement', 'straight', 'strategy', 'struggles', 'stupidity', 'submitting', 'subversion', 'successful', 'suddenly', 'suffering', 'supplies', 'supported', 'supporter', 'supporters', 'supporting', 'supports', 'supposed', 'suppression', 'surprise', 'surprised', 'suspicion.…', 'targeted', 'targeting', 'tassagency_en', 'techniques', 'theannakat', 'thedailybeast', 'themselves', 'theories', 'theorist', 'theorist/propagandist', 'theorists', 'thinking', 'thomaskaine5', 'thousands', 'throwing', 'timeline', 'together', 'traceyecorder', 'translated', 'trolling', 'tweeting', 'ua_informnapalm', 'undermine', 'undermines', 'understand', 'unfortunate', 'unleashed…', 'unreliable', 'unsubstantiated', 'untrustworthy', 'utilizing', 'vanabeau', 'ventilators', 'vergognosa', 'vetthebern', 'vigilante_intel', 'visegrad24', 'vulnerable', "w/Putin's", 'warrants', 'washingtonpost', 'watchdog', 'watching', 'weakening', 'weaponising', 'whatever', 'worldnews', "wouldn't", 'xtrixcyclex', 'yarotrof', 'yourself', 'zackbeauchamp', 'zero-sum', 'znalazła', '¡¡Jajajaja', 'говорят…', 'мывместе', '➡️Finalmente', '🇩🇪Niemczech', '🇷🇺Rosyjska']
>>> fdist2 = FreqDist(text)
>>> fdist2.most_common(50)
[('@', 19981), (':', 14684), ('.', 11103), ('Russia', 11025), ('the', 10807), ('and', 10006), ('to', 9279), (',', 8621), ('RT', 8560), ('China', 5828), ('https', 4787), ('a', 4429), ('disinformation', 4251), ('is', 4234), ('propaganda', 3689), ('of', 3557), ('in', 3373), ('that', 3357), ('for', 3345), ('coronavirus', 3213), ('on', 3185), ('’', 2735), ('Putin', 2584), ('have', 2370), ('#', 2328), ('are', 2234), ('?', 2130), ('about', 2048), ('As', 1914), ('The', 1845), ('!', 1805), ("''", 1770), ('campaigns', 1764), ('it', 1674), ('you', 1662), ('wage', 1588), ('seized', 1580), ('Disinformation', 1575), ('news', 1508), ('U.S.', 1405), ('Virus', 1403), ('as', 1391), ('See', 1379), ('from', 1371), ('and…', 1366), ('Spreads', 1356), ('Openings', 1356), ('with', 1312), ('seek', 1280), ('Trump', 1248)]
>>> fdist2.plot(50, cumulative=True)
<AxesSubplot:xlabel='Samples', ylabel='Cumulative Counts'>
>>> fdist1.most_common(50)
[('@', 19981), (':', 14684), ('.', 11103), ('Russia', 11025), ('the', 10807), ('and', 10006), ('to', 9279), (',', 8621), ('RT', 8560), ('China', 5828), ('https', 4787), ('a', 4429), ('disinformation', 4251), ('is', 4234), ('propaganda', 3689), ('of', 3557), ('in', 3373), ('that', 3357), ('for', 3345), ('coronavirus', 3213), ('on', 3185), ('’', 2735), ('Putin', 2584), ('have', 2370), ('#', 2328), ('are', 2234), ('?', 2130), ('about', 2048), ('As', 1914), ('The', 1845), ('!', 1805), ("''", 1770), ('campaigns', 1764), ('it', 1674), ('you', 1662), ('wage', 1588), ('seized', 1580), ('Disinformation', 1575), ('news', 1508), ('U.S.', 1405), ('Virus', 1403), ('as', 1391), ('See', 1379), ('from', 1371), ('and…', 1366), ('Spreads', 1356), ('Openings', 1356), ('with', 1312), ('seek', 1280), ('Trump', 1248)]
>>> fdist1_sorted = sorted(w for w in set(text) if len(w) > 7 and fdist1[w] > 7)
>>> FreqDist(fdist1_sorted)
FreqDist({"'Liberal": 1, '//t.co/2cnvSDxjXn': 1, '//t.co/2nqnS4p56h': 1, '//t.co/48PzpBWNrH': 1, '//t.co/4HmGvdm8oU': 1, '//t.co/6OqD4WGrZ5': 1, '//t.co/8e64RJE1mc': 1, '//t.co/9L4k2jp1bh': 1, '//t.co/9eQLu6QcXD': 1, '//t.co/BeXLsXPnJI': 1, ...})
>>> fdist1_sorted.most_common(50)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    fdist1_sorted.most_common(50)
AttributeError: 'list' object has no attribute 'most_common'
>>> fdist1_sorted = sorted(w for w in set(text) if len(w) > 7 and fdist1[w] > 100)
>>> fdist1_sorted
['//t.co/48PzpBWNrH', '//t.co/RAKCg5k…', 'AP_Europe', 'American', 'Americans', 'Anti-NATO', 'COVID-19', 'ComfortablySmug', 'Coronaviruis', 'Coronavirus', 'DaveKeating', 'DefTechPat', 'Disinformation', 'European', 'GianandreaGaian', 'Influence', 'JoeBiden', 'JohnCornyn', 'Openings', 'President', 'Propaganda', 'RaniaKhalek', '_JakubJanda', 'absolutely', 'accurate', 'advantage', 'anything', 'authorities', 'brainwashed', 'campaign', 'campaigns', 'collusion', 'conspiracy', 'continue', 'coronavirus', 'coronavirus-related', 'countries', 'defenseone', 'deployed', 'disarray', 'disgusting', 'disinformation', 'election', 'epidemic', 'government', 'increase', 'infections', 'interference', 'julianbarnes', 'misinformation', 'mounting', 'narratives', 'olgaNYC1211', 'oligarch', 'opportunity', 'outbreak', 'pandemic', 'partners', 'playbook', 'politicians', 'politico', 'populist', 'promoting', 'propaganda', 'pursuing', 'realDonaldTrump', 'respected', 'shameful', 'soldiers', 'spreading', 'straight', 'supplies', 'theories', 'together', 'undermine', 'utilizing', 'washingtonpost']
>>> 
