
from textblob import TextBlob
import tempfile

f= tempfile.TemporaryFile(mode='w+')




def spell_check(text):

    g=TextBlob(text)
    h=g.correct()
    f.write(str(h))
    return f


def corrected():
    f.seek(0)

    return f.read()


def delete():
    f.seek(0)
    f.truncate(0)
    return f
    
