# Basic Information_Retrieval Search Engine

This is a simple implementation that goes through how a information retrieval system works. It goes through scraping, indexing, and querying information specifically from wikipedia.

In-depth documentation can be found in the pdf, which contains the paper, screenshots, and future upgrades, in the paper. You can find how to operate this below

Chatgpt was used mainly for the flask and html. Python code was checked in depth since it kind of makes is own assumptions and has no validation on weather if the code is correct or not(can give a result, hard to verify if its correct)

The index data I used is here. https://drive.google.com/drive/folders/1WOqQxmhASbblfTxOrMaO3gbYipv8N58F?usp=drive_link

All of this was done in pycharm, and ran in order according to operation. then flask link is clicked to run. currently you can change depth and max pages in webscraping file, but this ideally should be set in a environment variable file.

## Operation:
The operation of the system involves a sequential execution of steps to achieve web crawling, indexing, querying, and information retrieval.
### Web Scraping:
Begin by configuring the web spider with parameters such as the seed URL, maximum depth, and maximum number of pages to crawl.
Run the web spider to initiate the crawling process. The spider navigates through the seed domain, following links and collecting HTML content from web pages.
Extracted data, including the URL, title, and content of each web page, is saved to the specified directory as HTML files. This is stored as blocks that can be used to be more eddicient and can possibly be parallel processed. the scraping process could also be done using the library scrapy.
It should look like this. Error cases should be looked into and web_scraper logic can be modified to get more information as html is not always the same.

![image](https://github.com/user-attachments/assets/7ea943e3-db06-4030-b89a-5c01a66d19de)
### Indexing:
After web scraping is complete, preprocess the collected HTML content by tokenizing, removing stop words, and stemming the text.
Build an inverted index using the TF-IDF algorithm, which maps terms to the documents in which they appear and their corresponding TF-IDF scores.
Save the inverted index to disk for efficient querying.
### Launching the Querying Interface:
Once indexing is finished, launch the Flask-based querying interface.
Users can input search queries through the interface, which triggers the retrieval of relevant documents from the inverted index. This is done using the search.py which is used in the background of the flask app. This currently uses cosine similarity, but knn search and word2vec can be used to improve this.
Retrieved documents are ranked based on cosine similarity scores, and the top results are displayed to users. Another area of improvement is query correction since this currently looks for exact words.

Valid Results:
![image](https://github.com/user-attachments/assets/e155ceda-9f75-4455-a8f6-f076da2aea78)
![image](https://github.com/user-attachments/assets/c7bd5b8c-a7ea-4d8b-a09d-4d3fc8220169)
![image](https://github.com/user-attachments/assets/53244ade-d014-4910-8378-4e57460a9ae1)

Unvalid results:
![image](https://github.com/user-attachments/assets/bd29b348-739c-42fa-bdfd-fea965bf3502)

clicking the link in valid pages goes to the wikipedia page

### Modifying Parameters:
If desired, parameters such as the seed URL, maximum depth, and maximum number of pages can be modified to target different domains or increase the scope of crawling.
Modify these parameters in the web spider configuration and rerun the scraping process to collect additional data. If parallel processing was done using scrapy and creating the index, this would go faster. 
### Clearing Index:
If needed, clear the existing index to start indexing anew or with different data.
This step ensures that the inverted index reflects the most current data and parameters. This is only useful when checking new data and should not be implemented practically.
### Repeatable Process:
The entire operation can be repeated as necessary, allowing for iterative improvements or adjustments to the crawling, indexing, and querying processes. Clearing can help iterate this to start over to see what happens in different tests.

you can clone this and run:
python web_spider.py
python build_index,py
python app.py

if clearing:
python clear.py
