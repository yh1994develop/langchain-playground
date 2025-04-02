import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = PromptTemplate.from_template(
    "日本の都道府県で人口が一番多いのはどこ？理由も説明して。"
)

# 安価なモデル gpt-3.5-turbo を指定
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=500,
)

chain: RunnableSequence = prompt | llm

response = chain.invoke({})
print(response.content)

# 出力結果
# 日本の都道府県で人口が一番多いのは東京都です。理由としては、東京都は日本の首都であり、
# 政治、経済、文化の中心地であるため、全国から人々が集まってきます。
# また、東京都は多くの企業が本社や支社を構えており、それに伴って多くの就職機会があります。
# さらに、東京都は日本国内外からの観光客も多く訪れるため、一時的に滞在する人々も多いです。
# これらの要因により、東京都の人口は他の都道府県を大きく上回っています。
