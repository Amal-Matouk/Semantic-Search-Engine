# Semantic Search Engine

A semantic search engine built using Flask, SQLAlchemy, and machine learning techniques to provide intelligent search capabilities.

## Features

- Perform semantic search across various documents.
- Utilize machine learning models for embedding generation.
- Efficient search using Annoy index for nearest neighbor search.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Amal-Matouk/semantic-search.git
   cd semantic-search
   
2. **Create and activate a virtual environment:**
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
 ```bash
pip install -r requirements.txt


## Usage
1. **Prepare the database:**
Add your documents to the documents.db database using dataloader.py.

2. **Run the application:**
flask run
The application will be accessible at http://localhost:8888.

3. **Search:**
Navigate to the homepage and enter a query to perform a semantic search.
