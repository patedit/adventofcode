import urllib.request

_INPUT_URL = 'https://adventofcode.com/2020/day/{}/input'
_HEADERS = {'cookie': 'session=53616c7465645f5f00d8d284a2a7107cde71f05e3bb5b09535dbb5fbe8d4b562022167a860b929a188a00f361bbec779'}

class Advent:
    def __init__(self, day, test=None):
        self.day = day
        self.lines = []
        self.paragraphs = [[]]
        if test is None:
            self.url = _INPUT_URL.format(self.day)
            req = urllib.request.Request(self.url, headers=_HEADERS)
            response = urllib.request.urlopen(req)
        
            idx_paragraph = 0
            for line in response.read().splitlines():
                line = line.decode('utf-8')
                if line != '':
                    if line.isnumeric():
                        line = int(line)
                    self.lines.append(line)
                    self.paragraphs[idx_paragraph].append(line)
                else:
                    idx_paragraph += 1
                    self.paragraphs.append([])
        else:
            self.lines = [int(e) if e.isnumeric() else e for e in test.splitlines()]
