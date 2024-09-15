from flask import Flask, jsonify, request, render_template
from Search.semantic_search import SemanticSearchApp

# Create an instance of the Flask application
app = Flask(__name__)

# Create an instance of the SemanticSearchApp
search_app = SemanticSearchApp()

# Define a route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for search
@app.route('/search', methods=['POST'])
def search():
    # Get the search query from the request
    query = request.json['query']

    # Perform the search using SemanticSearchApp
    results = search_app.search_documents(query)
    # Extract only the content from each result
    contents = [result['content'] for result in results]
    print('results')
    print(results)
    # Return the search results as a JSON response
    return jsonify(results=contents)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
