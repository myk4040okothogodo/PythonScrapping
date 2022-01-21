import urllib.request
from bs4 import BeautifulSoup
import re
import collections


class servaError(Exception):
    """Raised when the url requests fail."""
    pass

class FileOperationsError(Exception):
    """ Raise when file operations."""
    pass

def get_page(url1, url2):
    #providing url
    url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed "
    i = 0
    wordfreq1,wordfreq2 = {},{}
    frequencies = [wordfreq1, wordfreq2]
    urls = [url1, url2]
    semicleantexts = ['semiclean1.txt', 'semiclean2.txt']
    while i < len(urls):
        try:
            #opening the url for reading
            html = urllib.request.urlopen(urls[i])
        except:
            raise servaError(" Yikes!, could collect from the provided url")
        #parsing the html file
        htmlParse = BeautifulSoup(html, 'html.parser')

        try:
            #getting all the paragraphs 
            with open( semicleantexts[i], 'w+') as file:
            for para in htmlParse.find_all("p"):
                file.write(para.get_text())
            file.close()
        except:
            raise FileOperationsError(" file operations(write or read) failed, try again")
    

        try:
            with open( semicleantexts[i]) as f:
                for line in f:
                   for word in re.findall(r'[\w]+', line.lower()):
                       frequencies[i][word] = frequencies[i].setdefault(word, 0) + 1
            frequencies[i] = collections.OrderedDict(sorted(frequencies[i].items()))           

        except:
            raise FileOperationsError("file operations(write or read ) faiiled, try again")



    #compare the two dictionaries    
    shared_items = { word: wordfreq1[word] for word in wordfreq1 if word in wordfreq2 and wordfreq1[word] == wordfreq2[word]}
    i =  0
    for dictio in frequencies:
        for key,value in dictio:
            print ("Word :"key, " frequencyOfOcurrence :",value)
        print("_________________________________________")
    

    percentage_similarity = (len(shared_items)/(len(wordfreq1))*100
    print("The first page share a similarity of :", percentage_similarity,"%", "with the second page")
    percentage_similarity2 = (len(share_items)/(len(wordfreq2))*100
    print("The second page share a similarity of :", percentage_similarity2,"%", "with the first page")    

if __name__ == '__main__':
    get_page()
