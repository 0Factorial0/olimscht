import argparse
import requests
import time
import random

def make_request(url):
    #request every 1 seconds
    time.sleep(1)
    #try to request url, print status
    try:
        response = requests.get(url)
        print(f"{url} - {response.status_code}")
    #except error, print error
    except Exception as e:
        print(f"{url} - {str(e)}")

def main():
    #create argument structure as 'python3 <requester>.py --list <file>.txt'
    parser = argparse.ArgumentParser(description='Send requests to a list of URLs.')
    parser.add_argument('--list', type=str, required=True, help='Path to the file containing URLs.')
    args = parser.parse_args()

    #get the list and split
    with open(args.list) as f:
        urls = f.read().splitlines()

    #cut a random part of the list
    listLength = len(urls)
    firstIndex = random.randint(0, (listLength - 30))
    secondIndex = firstIndex + random.randint(5, 20)
    urlss = urls[firstIndex:secondIndex]

    #print out the list
    print("Going For [{0}->{1}] In Given Array".format(firstIndex, secondIndex))

    #push all links to requester
    for url in urlss:
        make_request(url)
    
    #call again
    main()

#route main function
if __name__ == "__main__":
    main()
