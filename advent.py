import urllib.request
import os

advent_dir = os.path.dirname(__file__)

_INPUT_URL = 'https://adventofcode.com/{}/day/{}/input'
_HEADERS = {
    'cookie': 'session={}'
}
_ADVENT_COOKIE_SESSION_ENV_VAR = 'ADVENT_COOKIE_SESSION'

class Advent:
    lines = []
    paragraphs = [[]]

    def _read_lines(self, lines):
        idx_paragraph = 0
        for line in lines:
            try:
                line = line.decode('utf-8')
            except Exception: pass
            if line != '':
                if line.isnumeric() and line[0] != '0': line = int(line)
                self.lines.append(line)
                self.paragraphs[idx_paragraph].append(line)
            else:
                idx_paragraph += 1
                self.paragraphs.append([])

    def __init__(self, year, day, test=None, use_file=False):
        self.year = year
        self.day = day
        lines_to_read = None
        if test:
            lines_to_read = test
        elif use_file:
            input_file_path = os.path.join(advent_dir, '{}/in/q{}.in'.format(self.year, self.day))
            f = open(input_file_path, 'r')
            lines_to_read = f.read()
        else:
            self.url = _INPUT_URL.format(self.year, self.day)
            if _ADVENT_COOKIE_SESSION_ENV_VAR not in os.environ:
                raise Exception("{} env var missing".format(_ADVENT_COOKIE_SESSION_ENV_VAR))
            _HEADERS['cookie'] = _HEADERS['cookie'].format(os.environ[_ADVENT_COOKIE_SESSION_ENV_VAR])
            req = urllib.request.Request(self.url, headers=_HEADERS)
            response = urllib.request.urlopen(req)

            lines_to_read = response.read()
        
        self._read_lines(lines_to_read.splitlines())
