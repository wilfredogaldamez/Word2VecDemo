
import gensim.downloader as api
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
from flask import Flask, render_template, request


 # load your model
w2v_model = Word2Vec.load('Word2VecModel')





# similar words to the word "time"
rList = []
for word in w2v_model.wv.most_similar('simulation'):
    print(word)
    rList.append(word)



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form.get('wordSearch')
        rList = []
        for word in w2v_model.wv.most_similar(word):
            print(word)
            rList.append(word)
        return render_template('index.html', rList = rList)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)