
import gensim.downloader as api
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
from flask import Flask, render_template


 # load your model
w2v_model = Word2Vec.load('Word2VecModel')





# similar words to the word "time"
for word in w2v_model.wv.most_similar('trump'):
    print(word)

app = Flask(__name__)

@app.route("/")
def hindex():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)