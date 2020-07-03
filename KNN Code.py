import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
import pickle

class recommandationclass:
    
    def __init__(self):
        pass
    def recommandBook(self,book_name):
        
	df_book=pd.read_csv('Ebook.csv', usecols=['Ebook_Id','Ebook_name'], dtype={'Ebook_Id':'int32','Ebook_name':'str'})
        df_ratings=pd.read_csv('Rating.csv', usecols=['EReview_id','memberId','Ebook_Id','ERating'],dtype=	{'EReview_id':'int32','memberId':'int32','Ebook_Id':'int32','ERating':'float32'})
        
	df = pd.merge(df_book,df_ratings,on='Ebook_Id')
        
	combine_book_rating = df.dropna(axis = 0, subset = ['Ebook_name'])
        book_ratingCount = (combine_book_rating.
         groupby(by = ['Ebook_name'])['ERating'].
         count().
         reset_index().
         rename(columns = {'ERating': 'totalRatingCount'})
         [['Ebook_name', 'totalRatingCount']])
        
	rating_with_totalRatingCount = combine_book_rating.merge(book_ratingCount, left_on = 'Ebook_name', right_on = 'Ebook_name', how = 'left')
        popularity_threshold = 1
        
	rating_popular_book= rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
        book_features_df=rating_popular_book.pivot_table(index='Ebook_name',columns='memberId',values='ERating').fillna(0)
        book_features_df_matrix = csr_matrix(book_features_df.values)
        model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
        model_knn.fit(book_features_df_matrix)
        query_index=process.extractOne(book_name, book_ratingCount["Ebook_name"])[2]
        distances, indices = model_knn.kneighbors(book_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 7)
        recommandBooks = []
        for i in range(0, len(distances.flatten())):
            if i == 0:
                pass
            #print('\nRecommendations for {0}:\n'.format(book_features_df.index[query_index]))
            else:
                recommandBooks.append(book_features_df.index[indices.flatten()[i]])
                #print(book_features_df.index[indices.flatten()[i]])
        return recommandBooks
    


obj = recommandationclass()
Books=obj.recommandBook("A new journey")
for i in Books:
    print(i)