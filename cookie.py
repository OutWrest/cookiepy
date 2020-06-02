import requests as re
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Times cookies to check when or if they expire.')
parser.add_argument('-request', metavar='N', type=str, nargs='+', help='BurpSuite text request')


def main(min):
    exit()
    s = re.Session()

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

    s.post(url.format(login), loginData, verify=False)
    s.post(url.format(cq), cqData, verify=False)

    for i in range(10000):
        r = s.get(url.format(manage), verify=False).text

        if 'Some important content' in r:
            sleep(i*min%(5<<6))
            continue
        break




if __name__ == '__main__':
    args = parser.parse_args()
    main(2)