# 구두점 삭제
# 구두점 글자의 딕셔너리를 만들어 translate() 적용

import unicodedata
import sys

text_data = ["Big whale!!!!!! Small whale!!!",
            "Dolphine of East sea....!!!", 
            "There is mimk whale...and moby-dick",
            "ANd @@@@ we are also whale!!!@#!$!@%"]

punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                           if unicodedata.category(chr(i)).startswith('P'))

test = [string.translate(punctuation) for string in text_data]

print(test)