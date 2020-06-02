import requests as re
from time import sleep
import argparse
from urllib.parse import urljoin
import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='<Required> Times cookies to check when or if they expire by replaying Burp Suite request.')
parser.add_argument('request', type=str, help='BurpSuite request location')
parser.add_argument('-s', '--seconds', type=int, default=60, help='Amount of seconds inbetween each request')
parser.add_argument('-nossl', action='store_true', help='Use ssl or not')

def main(args):
    try:
        method, headers, data = parse(args.request)
    except Exception as e:
        print("Error while parsing file {}".format(args.request))
        raise

    requesturl = urljoin("https://"+headers['Host'], method[1])
    for i in range(args.seconds*100000):
        if(method[0]):
            r = re.get(requesturl, data=data, headers=headers, verify=args.nossl)
            print(r.text)
        else:
            r = re.post(requesturl, data=data, headers=headers, verify=args.nossl)

        if r.status_code == 200:
            print('Sucessful ping after being active for {} seconds, the current time is {}.'.format(i*args.seconds, datetime.datetime.now()))
            sleep(args.seconds)
        else:
            print('Unsucessful ping with code', r.status_code)
            print('Exiting...')
            exit()

def parse(requestfile):
    with open(requestfile, 'r') as f:
        file_contents = f.read().splitlines()
    
    assert 'GET' in file_contents[0] or 'POST' in file_contents[0], "File does not contain GET or POST request"

    headers = {}
    data = {}
    for i in range(len(file_contents))[1:]:
        if ': ' in file_contents[i]:
            k, v = file_contents[i].split(': ')
            headers[k] = v
            continue
        if file_contents[i].strip():
            for param in file_contents[i].split('&'):
                k, v = param.split('=')
                data[k] = v

    method = 'GET' in file_contents[0], file_contents[0].split()[1]
    
    return method, headers, data

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)