from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String, unique=True)
    embedding = Column(LargeBinary)

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self._initialize_database()

    def _initialize_database(self):
        Base.metadata.create_all(self.engine)

    def insert_document(self, title, content, embedding):
        session = self.Session()
        if not self.exists_document(content):
            document = Document(title=title, content=content, embedding=embedding)
            session.add(document)
            session.commit()
        session.close()

    def exists_document(self, content):
        session = self.Session()
        return session.query(Document).filter(Document.content == content).first() is not None

    def get_all_documents(self):
        session = self.Session()
        documents = session.query(Document).all()
        session.close()
        return documents

    def execute_query(self, query, params=()):
        session = self.Session()
        result = session.execute(query, params)
        session.close()
        return result.fetchall()

    def close_connection(self):
        self.engine.dispose()
