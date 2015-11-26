__author__ = 'urlama1'


text = "X-DSPAM-Confidence:    0.8475";

start = text.find("0.8475")
end = start + len("0.8475")

print text[start:end]
