from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# テンプレートの定義
template = PromptTemplate.from_template(
    "{place}について、小学生にもわかるように説明してください。"
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

chain = template | llm

place = "渋谷"
response = chain.invoke({"place": place})

print("入力:", place)
print("応答:\n", response.content)

# 入力: 渋谷
# 応答:
#  渋谷は、東京都内にある有名な街です。ここはたくさんのお店やレストランが集まっていて、若者たちに人気のスポットです。渋谷駅は日本でも一番忙しい