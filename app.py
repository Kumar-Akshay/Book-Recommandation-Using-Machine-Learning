from flask import Flask, request, jsonify, render_template
import pickle
import json
import sys
from KnnBookSuggestion import recommandationclass


app = Flask(__name__)
@app.route('/recommand',methods=['POST'])
def recommand():
    data = request.get_json(force=True)
    print(data)
    with open("KnnRecommandModel.pkl","rb") as f:
        obj = pickle.load(f)
    book_name=data['parameter']
    print(book_name)
    recommandbooks = obj.recommandBook(book_name)
    books = []
    for i in recommandbooks:
        books.append(i)
    bookresponse={"book": books}
    print(bookresponse["book"])

    return bookresponse


if __name__ == "__main__":
    app.run(debug=True)