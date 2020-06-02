import requests as re
from time import sleep
import argparse
from urllib.parse import urljoin
import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='Times cookies to check when or if they expire by replaying Burp Suite request.')
parser.add_argument('request', type=str, help='<Required> BurpSuite request location')
parser.add_argument('-s', '--seconds', type=int, default=60, help='Amount of seconds inbetween each request')
parser.add_argument('--allow_redirections', action='store_true', help='Follow redirections after 300 status code')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose, enough said')
parser.add_argument('--nossl', action='store_false', help='Use ssl or not')

def main(args):
    try:
        method, headers, data = parse(args.request)
    except Exception as e:
        print("Error while parsing file {}".format(args.request))
        raise

    requesturl = urljoin("https://"+headers['Host'], method[1]).strip()
    for i in range(args.seconds*10000):
        try:
            if(method[0]):
                r = re.get(requesturl, data=data, headers=headers, verify=args.nossl, allow_redirects=args.allow_redirections)
            else:
                r = re.post(requesturl, data=data, headers=headers, verify=args.nossl, allow_redirects=args.allow_redirections)
        except re.exceptions.SSLError as ex:
            print(ex)
            exit('\nSSL Error, try --nossl')

        if r.status_code == 200:
            status, subdomain = 'Sucessful ping', method[1].strip()
   
        elif r.status_code >= 300 and r.status_code <= 400:
            status, subdomain = 'Redirection', r.headers['Location']

        else:
            print('Unsucessful ping with code [{}]'.format(r.status_code))
            print('Exiting...')
            exit()

        print('[{}]: Code {} -> ({}) | [Active for]: {} seconds | [Current Time]: {}.'. format(status, r.status_code, subdomain, i*args.seconds, datetime.datetime.now()))

        
        
        if (args.verbose):
            print('[Verbose]:', r.headers)

        sleep(args.seconds)

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