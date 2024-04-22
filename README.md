# Information_Retrieval
### In-depth documentation can be found in the pdf, which contains the paper and more information in the paper. The Operation of this is below for convenience. 

### The only sources used was Chatgpt, and prior learned knowledg in class. Chatgpt is used in code and homework assignments. ChatGPT is used more in the flask app, and html files, as it is more unfamiliar to me, but all IR-related is checked to make sure it matches correct logic ChatGPT is also used to explain parts of the documentation, where I read over to make sure it makes sense to the user. Since this is more of a logic, step-based paper, and not a personal paper, using ChatGPT helps convey steps better

## Operation:
The operation of the system involves a sequential execution of steps to achieve web crawling, indexing, querying, and information retrieval.
Web Scraping:
Begin by configuring the web spider with parameters such as the seed URL, maximum depth, and maximum number of pages to crawl.
Run the web spider to initiate the crawling process. The spider navigates through the seed domain, following links and collecting HTML content from web pages.
Extracted data, including the URL, title, and content of each web page, is saved to the specified directory as HTML files.
Indexing:
After web scraping is complete, preprocess the collected HTML content by tokenizing, removing stop words, and stemming the text.
Build an inverted index using the TF-IDF algorithm, which maps terms to the documents in which they appear and their corresponding TF-IDF scores.
Save the inverted index to disk for efficient querying.
Launching the Querying Interface:
Once indexing is finished, launch the Flask-based querying interface.
Users can input search queries through the interface, which triggers the retrieval of relevant documents from the inverted index.
Retrieved documents are ranked based on cosine similarity scores, and the top results are displayed to users.
Modifying Parameters:
If desired, parameters such as the seed URL, maximum depth, and maximum number of pages can be modified to target different domains or increase the scope of crawling.
Modify these parameters in the web spider configuration and rerun the scraping process to collect additional data.
Clearing Index:
If needed, clear the existing index to start indexing anew or with different data.
This step ensures that the inverted index reflects the most current data and parameters.
Repeatable Process:
The entire operation can be repeated as necessary, allowing for iterative improvements or adjustments to the crawling, indexing, and querying processes.
