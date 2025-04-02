from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

# メモリを定義（会話履歴）
# ConversationBufferMemory: 全履歴を保持
# ConversationSummaryMemory: 要約して保持
# ConversationTokenBufferMemory: トークン数で調整 (短期記憶)
memory = ConversationBufferMemory(return_messages=True)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # 処理の流れをログに出力
)

# memoryを試す
print("\n--- 会話スタート ---\n")

response1 = conversation.predict(input="おすすめのカフェ教えて")
print("💬 ユーザー: 鹿児島県でおすすめのカフェ教えて")
print("🤖 AI:", response1)

response2 = conversation.predict(input="そこ何時から開いてるの？")
print("💬 ユーザー: そこ何時から開いてるの？")
print("🤖 AI:", response2)

response3 = conversation.predict(input="ちなみに駅から近い？")
print("💬 ユーザー: ちなみに鹿児島中央駅から近い？")
print("🤖 AI:", response3)

#
# --- 会話スタート ---
#
#
#
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
#
# Current conversation:
# []
# Human: おすすめのカフェ教えて
# AI:
#
# > Finished chain.
# 💬 ユーザー: 鹿児島県でおすすめのカフェ教えて
# 🤖 AI: おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？
#
#
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
#
# Current conversation:
# [HumanMessage(content='おすすめのカフェ教えて', additional_kwargs={}, response_metadata={}), AIMessage(content='おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？', additional_kwargs={}, response_metadata={})]
# Human: そこ何時から開いてるの？
# AI:
#
# > Finished chain.
# 💬 ユーザー: そこ何時から開いてるの？
# 🤖 AI: そのカフェは通常朝8時から夕方6時まで営業しています。週末は遅くまで営業している場合もありますが、具体的な時間はお店のウェブサイトやSNSページで確認することをお勧めします。
#
#
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
#
# Current conversation:
# [HumanMessage(content='おすすめのカフェ教えて', additional_kwargs={}, response_metadata={}), AIMessage(content='おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？', additional_kwargs={}, response_metadata={}), HumanMessage(content='そこ何時から開いてるの？', additional_kwargs={}, response_metadata={}), AIMessage(content='そのカフェは通常朝8時から夕方6時まで営業しています。週末は遅くまで営業している場合もありますが、具体的な時間はお店のウェブサイトやSNSページで確認することをお勧めします。', additional_kwargs={}, response_metadata={})]
# Human: ちなみに駅から近い？
# AI:
#
# > Finished chain.
# 💬 ユーザー: ちなみに鹿児島中央駅から近い？
# 🤖 AI: そのカフェは駅から徒歩で約10分程度の距離にあります。比較的アクセスしやすい立地に位置しています。お店に行く際は、地図アプリを利用して道順を確認すると便利ですよ。
