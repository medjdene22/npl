from nltk.tokenize import TweetTokenizer, word_tokenize

text = "omgggg this lab is SO gooood!! can't wait for lab3 :) check https://nlp.univ.dz #NLP @prof_ahmed"

ws    = text.split()
wt    = word_tokenize(text)
tweet = TweetTokenizer().tokenize(text)

for name, toks in [("split", ws), ("word_tokenize", wt), ("TweetTokenizer", tweet)]:
    print(name, len(toks))
    print(toks, "\n")

print("comparison table:")
print(f"{'Tokenizer':<18}{'Tokens':<8}{'Hashtag':<9}{'URL':<6}{'Emoticon':<9}")
print("-" * 50)

for name, toks in [("split", ws), ("word_tokenize", wt), ("TweetTokenizer", tweet)]:
    print(f"{name:<18}{len(toks):<8}{'no' if '#' in toks else 'yes':<9}{'no' if 'https' in toks else 'yes':<6}{'yes' if ':)' in toks else 'no':<9}")
