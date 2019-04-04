import urllib.request as ur
import re

#Empty lists to be used in later functions
toVisit = []
visitedSites = []
uniqueEmails = []

#Function which finds all email addresses on the website
def get_addresses(content):
    strings = re.findall('[a-zA-Z0-9_.]*[@][a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', str(content))
    for x in range(0, len(strings)):
        if strings[x].endswith("."):
            strings[x] = strings[x][0:len(strings[x])-1]
    return strings

#Function that puts all UNIQUE email addresses in a list
def get_emails(content, uniqueEmails):
    allEmails = get_addresses(content)
    for email in allEmails:
        if email not in uniqueEmails: 
            uniqueEmails.append(email)
    return uniqueEmails

#Function that gets all the urls from a website queues them to visit if they haven't already been visited
def get_urls(content, toVisit, visitedSites):
    url = ''
    urls = []
    startIndex = content.find('href=') + 6
    endIndex = content.find(">", startIndex) - 1
    for i in range(len(content)):
        url = content[(startIndex):(endIndex)]  
        if url not in urls and url.find('https') != -1:
            urls.append(url)
            startIndex = content.find('href=', startIndex) + 6
            endIndex = content.find(">", startIndex) - 1
    for i in urls:
        if i not in visitedSites:
            if i not in toVisit:
                toVisit.append(i)
    return toVisit, visitedSites
        
#Function which does all the crawling using previous functions
def crawl(start, limit):
    '''Crawl takes a website (start) and an integer (limit) and finds all unique email addresses that can be accessed from the website and its urls. The function stops when limit number of websites have been crawled'''
    toVisit.append(start)
    while toVisit:
        website = toVisit.pop()
        if website not in visitedSites:
            connection = ur.urlopen(website)
            if (connection.status == 200):
                content = str(connection.read())
                visitedSites.append(website)
                get_urls(content, toVisit, visitedSites)
                get_emails(content, uniqueEmails)
            else:
                connection.close()
                return -1
        connection.close()
                
        if len(visitedSites) >= limit:
            break
        
    return uniqueEmails

        
        
        
        