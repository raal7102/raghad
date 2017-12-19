from bs4 import BeautifulSoup
import urllib2
import re
from nltk.corpus import stopwords

def getURLsList(url):
    resp = urllib2.urlopen(url)
    soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

    pages = []
    for link in soup.find_all('a', href=True):
        page = link['href']

        if page[:4] != "http":
            page = url + "/" + page

        pages.append(page)

    return pages

def getKeyWords(url):
    resp = urllib2.urlopen(url)
    soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    regex = r'(\w*) '
    words = filter(lambda w: w != '', re.findall(regex, visible_text))

    filtered_words = [w for w in words if w not in stopwords.words('english')]

    return filtered_words

def getRankings(listOfURLs):
    urlDictionary = {}
    rankingDictionary = {}
    for url in listOfURLs:
        pages = getURLsList(url)
        for page in pages:
            if url not in urlDictionary:
                urlDictionary[url] = []
            urlDictionary[url].append(page)
    for item in urlDictionary:
        rankingDictionary[item] = len(item)
    return rankingDictionary

def getKeywordsToWebpages(listOfURLs):
    keywordDictionary = {}
    print(listOfURLs)
    for url in listOfURLs:
        keywords = getKeyWords(url)
        for keyword in keywords:
            if keyword not in keywordDictionary:
                keywordDictionary[keyword] = []
            if url not in keywordDictionary[keyword]:
                keywordDictionary[keyword].append(url)
    return keywordDictionary

def main():
    listOfURLs = ["http://cnn.com", "http://abcnews.go.com", "http://cbs.com", "http://cnn.com/us"]
    print("hello")
    rankingDict = getRankings(listOfURLs)
    print(rankingDict)
    keywordDict = getKeywordsToWebpages(listOfURLs)
    print(keywordDict)
    result = {}

    testSearch = "olArabicSet"
    if testSearch in keywordDict:
        print("found search keyword")
        urlOptions = keywordDict[testSearch]
        testSearchDictionary = {}
        for url in urlOptions:
            if url in rankingDict:
                testSearchDictionary[url] = rankingDict[url]
        for key, value in sorted(testSearchDictionary.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            print "%s: %s" % (key, value)
            result[key] = value

    print(result)
    return result


if __name__== "__main__":
    main()