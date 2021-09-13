from gensim.models import word2vec

with open("kimetu_yaiba.txt", "r") as f:
    kimetu = f.read()

# 英数字の削除
kimetu = re.sub("[a-xA-Z0-9_]","",kimetu)
# 記号の削除
kimetu = re.sub("[!-/:-@[-`{-~]","",kimetu)
# 空白・改行の削除
kimetu = re.sub(u'\n\n', '\n', kimetu)
kimetu = re.sub(u'\r', '', kimetu)

def meishi(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    noun = []
    for token in tokens:
        partOfSpeech = token.part_of_speech.split(",")[0]
        if partOfSpeech == "名詞":
            noun.append(token.surface)
    return noun

#名詞取り出し
kimetu = meishi(kimetu)

model = word2vec.Word2Vec(kimetu,
                        sg=1,
                        size=300,
                        min_count=2,
                        window=10,
                        hs=1,
                        negative=0)
model.save('kimetu_yaiba.model')

model = word2vec.Word2Vec.load("kimetu_yaiba.model")

model.wv.most_similar(positive=[u"鬼"], topn=10)
