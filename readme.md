# DSC 261 Project Final Report: A Comparative Analysis of Interpretability of Models for Sentiment Analysis


## Overview

Sentiment analysis in the financial domain is both challenging and rewarding, offering a unique lens through which to view market trends and investor sentiment. Our study leverages advanced deep learning models, specifically BERT (Bidirectional Encoder Representations from Transformers), known for their high accuracy in text classification tasks. However, the opaqueness of these models often leaves users guessing about the rationale behind their predictions.

To bridge this gap, we integrate interpretability techniques, namely Local Interpretable Model-agnostic Explanation (LIME) and SHapley Additive exPlanations (SHAP), into our analysis. These tools allow us to peek inside the "black box" of BERT, offering insights into the model's decision-making process by analyzing attention weights and feature importance scores.

## Goals

- **Sentiment Classification:** Utilize BERT-based models to categorize tweets related to stocks by their sentiment, aiding in the understanding of market sentiment.
- **Model Interpretability:** Apply LIME and SHAP to interpret the decision-making process of BERT models in financial sentiment analysis, providing clarity on how predictions are made.
- **Performance Comparison:** Contrast the performance and transparency of BERT with traditional rule-based models such as Logistic Regression and Naive Bayes. While these models offer greater interpretability, they often lag in accuracy.

## Why This Matters

The ability to accurately analyze sentiment on platforms like Twitter can offer actionable insights into market dynamics and investor behavior. By improving the interpretability of state-of-the-art models, we aim to make these insights more accessible and understandable, thereby enhancing trust and reliability in AI-driven financial analysis.

Join us in exploring the complex world of stock sentiment analysis through the lens of advanced NLP techniques and interpretable AI. Our findings not only contribute to academic knowledge but also have practical implications for investors, analysts, and enthusiasts interested in leveraging AI for financial decision-making.

## Get Started

Dive into our analysis by exploring the code, datasets, and results documented in this repository. Whether you're a researcher, practitioner, or enthusiast, there's something here for everyone interested in the cutting-edge of NLP and finance.

---

We're excited to share our journey with you and welcome any contributions, questions, or feedback. Let's advance the frontier of interpretable AI in finance together!


## DATASET 

The Dataset Link : https://paperswithcode.com/dataset/stocknet-1
Github Link for Dataset : https://github.com/yumoxu/stocknet-dataset


Dataset Licence : MIT License (https://github.com/yumoxu/stocknet-dataset?tab=MIT-1-ov-file)


## Code :

1. All the code is present in the notebooks folder
2. We have made some changes to the code such that it can be run locally 
3. We also have created a src folder containing generic functions that shall be reused throughout the code in addition to requirements.py


## Sample Results : 

### SHAP Sample Results - 
<img width="792" alt="Screenshot 2024-03-21 at 9 50 56 PM" src="https://github.com/rijul11/DSC-261-Final-Project/assets/129983758/37fae608-d2ad-40b7-9c80-31a7351260a6">
<img width="792" alt="Screenshot 2024-03-21 at 9 50 46 PM" src="https://github.com/rijul11/DSC-261-Final-Project/assets/129983758/e66bab3d-a48a-42a5-934b-90d741916cae">
<img width="793" alt="Screenshot 2024-03-21 at 9 50 26 PM" src="https://github.com/rijul11/DSC-261-Final-Project/assets/129983758/45945b49-8da9-482b-a093-e0549d34b94b">

### LIME Sample Results - 




