In this folder, We can observe multiple Jupyter Notebooks each serving a particular task of our project.

Notes :
1. All the code can be executed out of the box without any prior setup as all requirements have already been mentioned in the respective notebooks
2. For the sake of testing and ease of use, we have created a sample smaller dataset here named - tweets_labelled_09042020_16072020.csv and is available at this level.
3. Some jupyter notebooks might need the whole dataset, hence please refer to the readme in the dataset folder.
4. We have also included the code, we couldnt complete but are actively working on. All such code has been placed under FW folder.



One Such result which will take a lot of time, is the comparision betweem BERT models. The sample results for this are - 


model_name	                                                min_sentiment_score	        max_sentiment_score	        mean_sentiment_score	runtime
0	distilbert-base-uncased-finetuned-sst-2-english	        0.502498	                0.999811	                0.976865	            81.685143
1	roberta-large-mnli	                                    0.335916	                0.994299	                0.606306	            474.807743
3	roberta-base	                                        0.516505	                0.537983	                0.529074	            151.841959
2	bert-base-uncased	                                    0.500008	                0.552337	                0.509333	            155.868212