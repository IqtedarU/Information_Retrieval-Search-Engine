from flask import Flask, request, jsonify, render_template, send_file
import os
from search import search_query, load_index

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Assuming you have an HTML file named index.html

@app.route('/view_document/<string:title>', methods=['GET'])
def view_document(title):
    # Retrieve the file path of the document based on the doc_id
    file_name = f"{title}.html"
    directory = 'C:/website_content'
    file_path = os.path.join(directory, file_name)

    # Send the file to the user for viewing
    return send_file(file_path, mimetype='text/html')

@app.route('/search', methods=['GET'])
def search():
    # Extract the search query from the request parameters
    query = request.args.get('query')

    # Load inverted index
    index_file = "C:/index/inverted_index.pkl"  # Update with your index file path
    inverted_index = load_index(index_file)

    # Perform search query processing
    search_results = search_query(query, inverted_index)

    # Slice search_results to only include the first 15 results
    search_results = search_results[:15]

    # Render the search template with the search results
    return render_template('search.html', query=query, search_results=search_results)


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
    app.run('0.0.0.0', '5000')
