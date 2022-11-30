import string
from nltk.tokenize import word_tokenize


sentence = "We had high expectations given the reviews and TIMEOUT mention for\
best pubs in Victoria area, we were disappointed. In particular, all the sides \
were served ice cold (literally, no hyperbole here). Peas were so cold we \
couldn't eat them, mashed potatoes as well, carrots were raw. Additionally they \
were out of steaks at 7:30 PM on a Friday night with a near empty pub.. huh? \
Either Timeout has very low standards or this place is only good when critics \
are around.\
\
One bright spot was a very kind bartender, but I'm not sure she is enough to\
save the experience."
sentence = sentence.lower()
sentence_no_digit = ""
for char in sentence:
    if char.isdigit() or char in string.punctuation:
        result = ""
    else:
        result = char
    sentence_no_digit += result
    sentence = sentence_no_digit.strip()
print(sentence)


