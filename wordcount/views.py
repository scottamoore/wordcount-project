from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	originaltext = request.GET['fulltext']

	fulltext = originaltext.lower()
	for char in ['-', '—']:
		fulltext = fulltext.replace(char, " ")
	for char in ['.', ":", ","]:
		fulltext = fulltext.replace(char, "")
	fulltext = fulltext.lstrip().rstrip()
	wordlist = fulltext.split()
	thelength = len(wordlist)

	worddict = {}
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
	minimaldict = dict((k,v) for k, v in worddict.items() if v >= 5)

	if len(minimaldict.items()) < 10:
		wordlist = worddict.items()
	else:
		wordlist = minimaldict.items()

	sortedwords = sorted(wordlist, key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {"originaltext": originaltext,
					"fulltext": fulltext, "count": thelength,
					"worddict": worddict, "wordlist": sortedwords})

def about(request):
	return render(request, 'about.html')

