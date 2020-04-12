"""SCID annotated moves parser """
import re
from collections import deque


SCORE_PATTERN = re.compile(r'\s*\d+:(?P<score>[+\-]?\d+(\.\d+)?)\s*')
MATE_PATTERN = re.compile(r'\s*\d+:(?P<score>M(?P<sign>-?)\d+)\s*')
WORD_PATTERN = re.compile(r'\w+(-\w)*')


def parse(text):
    """SCID annotated moves parser """
    move = 'None'
    for line in map(lambda m: m.group(), re.finditer(r'.+', text)):
        score_matcher = re.fullmatch(SCORE_PATTERN, line)
        score = None
        if score_matcher:
            score = score_matcher.group('score').replace('+', '')
        else:
            mate_matcher = re.fullmatch(MATE_PATTERN, line)
            if mate_matcher:
                score = '%s20' % mate_matcher.group('sign')
        if score is None:
            word_matchers = deque(re.finditer(WORD_PATTERN, line), maxlen=1)
            if word_matchers:
                move = word_matchers.pop().group()
        else:
            print(move, score, sep='\t')
