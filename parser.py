import urllib.request
import argparse
import difflib
import ssl
import re

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('s', type=str, help='s integer for the accumulator')
parser.add_argument('l', type=str, help='l integer for the accumulator')
args = parser.parse_args()

class Found:
    def __init__(self):
        pass

    def similar(self, url, letter):
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        my_file = urllib.request.urlopen(url, context=gcontext)
        mybytes = my_file.read()[:15000]
        string = mybytes.decode("utf8")
        my_file.close()

        string = string.split(" ")
        for i in string: 
            q = str(i)
            reg = re.compile('[^a-zA-Z ]')
            q = reg.sub('', i).lower()
            #q = q.lower()
            letter = letter.lower()
            seq = difflib.SequenceMatcher(None, q, letter)
            var = seq.ratio()
            if var > 0.5:
                print(seq.ratio(), "\t", i)

# s = "http://qaru.site/questions/182288/how-to-receive-json-data-using-http-post-request-in-django-16"
# s = 'https://www.google.ru/'
# s = "It$#@!%$^$&*() eas&^%$ier is typica(*@#$lly easi!@#$%^er, howev316422:er, to sele%^&ct the <form itself for ea~&$!@#sier serialization"
# l = "false"
a = Found()
a.similar(args.s, args.l)
    
