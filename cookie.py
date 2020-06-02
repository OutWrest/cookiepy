import requests as re
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='<Required> Times cookies to check when or if they expire by replaying Burp Suite request.')
parser.add_argument('request', type=str, help='BurpSuite request location')
parser.add_argument('-s', '--seconds', type=int, help='Amount of seconds inbetween each request')

def main(args):
    exit()

    url = 'https://application.local:5001/{}'
    login = 'Account/Login/'
    cq = 'Account/AnswerChallengeQuestions/'
    manage = 'Manage/'

    loginData = {
        'UserName': 'user',
        'Password': 'asd',
        'RemeberMe': 'false'
    }

    cqData = {
        'Answer1': 'a',
        'Answer2': 'a'
    }

    re.post(url.format(login), loginData, verify=False)
    re.post(url.format(cq), cqData, verify=False)

    for i in range(10000):
        r = re.get(url.format(manage), verify=False).text

        if 'Some important content' in r:
            sleep(i*s%(5<<6))
            continue
        break

def parse(requestfile):
    # Parses requestfile, returns a request dictionary for replay.
    pass


if __name__ == '__main__':
    args = parser.parse_args()

    try:
        request = parse(args.request)
    except Exception as e:
        print("[{}] while parsing file {}".format(e,args.request))

    main(args)