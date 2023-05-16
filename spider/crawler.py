import argparse
import urllib.request
import re

#create argument structure as 'python3 spider/crawler.py --file <file>.txt --output <file>.txt'
parser = argparse.ArgumentParser(description='Web Crawler Spider')
parser.add_argument('-d', '--domain', type=str, default='',
                    help='Specify a domain name. Example: https://www.example.com/')
parser.add_argument('-f', '--file', type=str, default='',
                    help='Specify the name of the domain file. Example: domains.txt')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Specify the name of the output file. Example: output.txt')
args = parser.parse_args()

#get links of url
def get_links(url):
    import os
    from os.path import exists
    import random
    '''Returns all links at the given URL.'''
    #create links array
    links = []
    try:
        #request url
        response = urllib.request.urlopen(url)
        #decode it to utf-8
        html = response.read().decode('utf-8')
        #scrap the url and only get the links
        hrefs = re.findall(r'<a\s.*?href=[\"\'](.*?)[\"\'].*?>', html)
        #loop all hrefs
        for href in hrefs:
            #if it starts with http, append the href
            if href.startswith('http'):
                links.append(href)
            #if it starts with /, append the url and href
            elif href.startswith('/'):
                links.append(url + href)
    except:
        #if not connected, pass to the other link
        pass
    #get the current location of /mitm folder
    file_path = os.path.dirname(os.path.abspath("start.py"))
    randomName = str(random.randint(23,23232323))
    #dump links to a file
    #links_file = file_path+"/link/dump/"+randomName+".txt"
    #linkss = open(links_file, "w")
    #for link in links:
    #    linkss.write(link + '\n')
    #crawl
    return links

#crawler
def crawl(domain, counter):
    import os
    from os.path import exists
    '''Visits all pages in the specified domain.'''
    #create a set as visited
    visited = set()
    #get the current location of /mitm folder
    file_path = os.path.dirname(os.path.abspath("start.py"))
    links_file = file_path+"/link/links.txt"
    #get the existing list and add it to visited links set
    if(exists(links_file)):
        f = open(links_file, "r")
        visited_urls = f.read().splitlines()
        for urls in visited_urls:
            visited.add(urls)
    #get the comain in queue
    queue = [domain]
    #loop queue
    while queue:
        #if you have 200 pages of an url, break
        if(counter == 200):
            break
        #pop and get the url
        url = queue.pop(0)
        #if it is in visited pass
        if url in visited:
            continue
        #or add it to visited links
        visited.add(url)
        #print output
        print('Crawling:', url)
        #get the links of url
        links = get_links(url)
        #write link to the output file
        with open(args.output, 'a') as f:
            f.write(url + '\n')
            counter += 1
        #check all links
        for link in links:
            #if it starts with the same domain add it to queue
            if link.startswith(domain):
                queue.append(link)

#main method
if __name__ == '__main__':
    #if you have one domain
    if args.domain:
        #push the domain
        crawl(args.domain)
    #if you have a file
    elif args.file:
        #read the file and split the lines as domains
        with open(args.file, 'r') as f:
            domains = [line.strip() for line in f.readlines()]
        #push every domain
        for domain in domains:
            counter = 0
            crawl(domain, counter)
    #or print error
    else:
        print('You must specify a domain name or file.')