import os

from Search.database import Database
from Search.embedding import DocumentEmbedder

# Construct the absolute path to the database file
db_path = os.path.abspath('documents.db')
db_url = f'sqlite:///{db_path}'

# Initialize the database
db = Database(db_url)
model_name = 'all-MiniLM-L6-v2'
embedder = DocumentEmbedder(model_name)

def load_documents():
    documents = [
        "The rise of e-commerce has transformed the retail industry.",
        "The importance of data-driven decision making in business cannot be overstated.",
        "The impact of globalization on local economies is a complex issue.",
        "The role of leadership in organizational success is crucial.",
        "This is a sample document about machine learning.",
        "machine learning is a type of multiple subjects.",
        "Another document about natural language processing.",
        "A document about computer vision and image recognition.",
        "no one knows what is coming from machine learning.",
        "The rise of e-commerce has transformed the retail industry.",
        "Online shopping offers convenience and a wider range of products.",
        "Digital payment systems have enhanced the security of e-commerce transactions.",
        "The importance of data-driven decision making in business cannot be overstated.",
        "Big data analytics helps organizations uncover hidden patterns and insights.",
        "Data visualization tools are essential for interpreting complex datasets.",
        "The impact of globalization on local economies is a complex issue.",
        "Global trade agreements have both benefits and challenges.",
        "Cultural exchange is a significant aspect of globalization.",
        "The role of leadership in organizational success is crucial.",
        "Effective leaders inspire and motivate their teams towards common goals.",
        "Leadership styles can vary significantly across different cultures.",
        "Cybersecurity measures are critical in protecting sensitive information.",
        "Phishing attacks remain a significant threat to online security.",
        "Implementing strong passwords is a basic yet effective security measure.",
        "Renewable energy sources are vital for a sustainable future.",
        "Urban planning must incorporate green spaces for ecological balance.",
        "Sustainable agriculture practices help preserve natural resources.",
        "AI is transforming industries with automation and efficiency.",
        "Ethical considerations in AI development are increasingly important.",
        "Machine learning algorithms can improve over time with more data.",
        "Online learning platforms provide access to education worldwide.",
        "Personalized learning adapts to individual student needs.",
        "The integration of technology in classrooms enhances learning experiences.",
        "Regular exercise is crucial for maintaining physical and mental health.",
        "A balanced diet is essential for overall well-being.",
        "Mindfulness and meditation can reduce stress and improve focus.",
        "Cryptocurrency is gaining popularity as an alternative investment.",
        "Financial literacy is key to managing personal finances effectively.",
        "Stock market volatility requires strategic investment planning."
    ]
    return documents

def insert_documents(documents):
    for doc in documents:
        if not db.exists_document(doc):
            embedding = embedder.embed_documents([doc])[0]
            db.insert_document(doc[:10], doc, embedding)
        else:
            print(f"Skipping duplicate document: {doc}")

def get_all_documents():
    return db.get_all_documents()

# Call
if __name__ == '__main__':
    documents = load_documents()
    insert_documents(documents)
    rows = get_all_documents()
    for row in rows:
        print(row.content)
