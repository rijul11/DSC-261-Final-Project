from transformers import pipeline
import pandas as pd


def generate_sentiment_label_score(classifier_model, df, columnName):
    # ```
    # This is curated specifically for Stocknet Tweets Dataset. Changes might be required for other use cases.
    # This function takes sentiment analysis model as the 1st i/p followed by the dataframe and the column upon which sentimentAnalysis has to be run.
    
    # Sample Function Call For Tweets Dataset: 
    
    # model="distilbert-base-uncased-finetuned-sst-2-english"
    # generate_sentiment_label_score(model,tempDF,'text')


    # Sample Function Call For News Dataset:
    # model="distilbert-base-uncased-finetuned-sst-2-english"
    # newsDf = pd.read_csv(news_path, encoding='latin-1', parse_dates= [1], index_col = ['Date'])
    # newsDf = newsDf[newsDf['Title'].notna()]
    # generate_sentiment_label_score(model,tempDF,'Title')
    
    # Return : Same dataframe with 2 new columns 'sentiment_label', 'sentiment_score'
    # ```
    classifier = pipeline("sentiment-analysis", model=classifier_model)
    df[[columnName+' sentiment_label', columnName+' sentiment_score']] = df[columnName].apply(lambda text: pd.Series(classifier(text)[0]))
    return df