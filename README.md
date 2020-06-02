# CookiePy
 
Are you extremely lazy? Do you want any program to just work without having to worry about anything? **Introducing CookiePy,** the all-in-one utility that wastes your time while simultaneously reinventing a prominent feature that exists in Burp Suite.

## Features

* Parses Burp Suite requests in 'replays' them
* Much lighter weight utility
* Makes the objective twice as hard
* Makes use of machine learning to optimize requests (just kidding)
* That's it, set your standards low before pulling the project

## Installation

Make sure to have [python3](https://www.python.org/downloads/) installed with the [requests](https://requests.readthedocs.io/en/master/) library.

```bash
pip3 install requests
git clone https://github.com/OutWrest/CookiePy
```

## Usage

To get a list of the available options:

```bash
>>> python3 cookie.py --help
```
```
usage: cookie.py [-h] [-s SECONDS] [--allow_redirections] [-v] [--nossl] request 
Times cookies to check when or if they expire by replaying Burp Suite request.

positional arguments:
  request               <Required> BurpSuite request location

optional arguments:
  -h, --help            show this help message and exit
  -s SECONDS, --seconds SECONDS
                        Amount of seconds inbetween each request
  --allow_redirections  Follow redirections after 300 status code
  -v, --verbose         Verbose, enough said
  --nossl               Use ssl or not
```

The python program parses HTTP requests, the easiest way to set it up is by going to Burp Suite, getting a request (with a cookie) of a page only visible to **Authenticated users** because when an unauthenticated user makes a request, a different output will occur. Copy the request (**GET** or **POST**) to a file.

```bash
python3 cookie.py path-to-requestfile
```

#### Examples

Testing the cookie.py with my [other project](https://github.com/OutWrest/BurpsRSuite).

```bash
python3 cookie.py example.txt -s 2
```
```
HTTPSConnectionPool(host='application.local', port=5001): Max retries exceeded with url: /Manage (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')],)",),))

SSL Error, try --nossl
```

SSL Errors are evident of a poor setup but hey, it works. --nossl will put a bandaid on that error.

```bash
python3 cookie.py example.txt -vs 2 --nossl
```
```
[Redirection]: Code 302 -> (/Account/AnswerChallengeQuestions) | [Active for]: 0 seconds | [Current Time]: 2020-06-02 11:25:10.840581.
[Verbose]: {'Connection': 'close', 'Date': 'Tue, 02 Jun 2020 16:25:10 GMT', 'Server': 'Kestrel', 'Content-Length': '0', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT', 'Location': '/Account/AnswerChallengeQuestions', 'Set-Cookie': '.AspNetCore.Identity.Application=CfDJ8I-mu7nAx-xNinCN0EJ54fli-3wzTmGwD8BvKakvEZX2UwUdcxzubwniFSxsdhPawbnfl7d4NKwHkwTGT5aBSAtKgAev7ZLqtn5ltl8HxLIIIpdjjBzsuMYrNMTc9E7CKhs83Jw3_oQGddBm2kyFg2SAFKPQwJRBCp5szBqpUUwqdSJvrc7bJd6ZdKmLCMOZCjuix3R2B7W9KR3rkVJIbCf8IvlOYSTbu9AJeNBJot4NkFMoXXN2cYKW_bxUyiWgMGdwCsetDjqeYPFAKGO3mMFwlpquDa9MbBOR5hJHXeqLgVj7tLo_ujQWmSUX78Y8bw_TiXaONXVBCwOJWibOiTHXHfVZxjzTjh-gyRW76MOII34gZuhagCjC2B41QEy3Kqm3aETTq8Sdyo5CfnuvxIGRDsr5AZvRyOGk_6nU0NgtilLxQmYNhP7CkdmPef86oeSwymRnDp78YHzau6TKBSfiDXMtwx7ShCi59YPQc0suIHFtU3nojEpGIoI7dweZArhFP90kBoawsBwxPlwVu04zFD2b5-xsntvrAXnLliBBTxn4WTM35fJVqXJpjHvwM7_NefoxgU5mPM6ZfAIYVOyJr_GRs_d1muwlP7tAANPKiZPx1LeiPVNkzCMvB3BKZChM-vGr0wYw8OnxjQsyWb8oa7AZuOQ9uOQuf7bCitZL; path=/; secure; samesite=lax; httponly'}
```

Verbose will also return the headers for each requests

```bash
python3 cookie.py example.txt -s 2 --nossl --allow_redirections
```
```
[Sucessful ping]: Code 200 -> (/Manage) | [Active for]: 0 seconds | [Current Time]: 2020-06-02 11:27:40.544758.
[Sucessful ping]: Code 200 -> (/Manage) | [Active for]: 2 seconds | [Current Time]: 2020-06-02 11:27:42.588236.
[Sucessful ping]: Code 200 -> (/Manage) | [Active for]: 4 seconds | [Current Time]: 2020-06-02 11:27:44.631328.
```

With `allow_redirections`, the program will follow redirections but it shows the original request page with status code on output.