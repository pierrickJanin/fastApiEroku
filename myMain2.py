# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:21:26 2022

@author: pjani
"""
# Python libraries
import pandas as pd

from bs4 import BeautifulSoup

from fastapi import FastAPI





app = FastAPI()
@app.get("/")
async def root():
    

    # chargement du fichier
    #mainFrame = pd.read_csv("C:/Users/pjani/Documents/parcours iml/projet/P5/data/QueryResults.csv")
    #test_df=mainFrame.head(5)
    doc1 = '<p>Game of Thrones is an amazing tv series!</p>'
    doc2 = '<p>Game of Thrones is the best tv series!</p>'
    doc3 = '<p>Game of Thrones is so great</p>'
    title1='title1'
    title2='title2'
    title3='title3'
   
    Body=[]
    Body.append(doc1)
    Body.append(doc2)
    Body.append(doc3)

    Title=[]
    Title.append(title1)
    Title.append(title2)
    Title.append(title3)
    
    def body_to_words(value):
        # 1. On supprime les balises html
        text = BeautifulSoup(value, "lxml").get_text() 
        #text = re.sub('\n', '', text)
        return(text)  

    test_df=pd.DataFrame(data={"Title":Title,"Body":Body})
    test_df['Body']=test_df['Body'].apply(body_to_words)
    test_df['mots']=test_df['Title']+": "+test_df['Body']


# on créer un nuage de mots avec tous les tokens, séparés par un espace

    comment_words=''
    for tokens_list in test_df["mots"]:
         comment_words += "".join(tokens_list)+"," #join extrait les "mots" d'une liste

    
    return comment_words
   
   
