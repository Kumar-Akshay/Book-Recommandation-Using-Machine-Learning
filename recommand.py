import pickle
import json
from KnnBookSuggestion import recommandationclass

with open("KnnRecommandModel.pkl","rb") as f:
    mp = pickle.load(f)
book_name1 = 'The Demon Girl'
var = mp.recommandBook(book_name1)
str1 = []
for i in var:
    print(i)
    str1.append(i)
    st={"book": str1}
    

print(st)