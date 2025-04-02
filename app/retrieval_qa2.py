from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()

# IPAの第 1 回 契約・決済アーキテクチャ検討会議事録のPDF読み込み
loader = UnstructuredPDFLoader("data/第1回契約・決済アーキテクチャ検討会議事録.pdf", mode="elements")
docs = loader.load()

# 分割
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n", "。", "、", " "]
)
chunks = splitter.split_documents(docs)

# 使用できない metadataを除外する
filtered_chunks = filter_complex_metadata(chunks)

# ベクトルDB（Chroma）にインデックスを作成
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings()
)

# Retrievalチェーンの構築
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 質問してみる
query = "この会議の目的はなんですか？"
response = qa.run(query)

print("質問:", query)
print("回答:", response)
