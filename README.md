# LangChain Playground

学習用のLangChainリポジトリ

OpenAIの安価なモデル（gpt-3.5-turbo）を使って、基本的なChainやRetrievalなどを段階的に試す

## setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

* .envにOPENAI_API_KEY を設定する

---

### basic chain

* プロンプトに「日本の都道府県で人口が一番多いのはどこ？理由も説明して。」を投げてみる

```bash
python app/basic_chain.py
```

---

### Retrieval QA

**Retrieval QAとは？**
> 外部データ（PDF,CSVなど）を取り込み、検索(retrieval) + LLMの生成(generation) を組み合わせて回答する

**イメージ**

```text
[ PDFやテキストを読み込み ]
        ↓
[ チャンクに分割 ]
        ↓
[ ベクトル化してDBに保存（Chroma） ]
        ↓
[ ユーザーが質問 → 関連データを検索 → LLMに渡して回答生成 ]
```

```bash
python app/retrieval_qa.py
```

**実行結果**

```text
質問: 2021年3月時点での現金および預金の合計は？
回答: 申し訳ありませんが、提供された情報からは2021年3月時点での現金および預金の合計を特定することはできません。
```

```text
質問: 貸借対照表を含むPDFです。丁寧に読んでください。2021年3月時点での現金および預金の合計は？
回答: 申し訳ありませんが、提供された情報からは2021年3月時点での現金および預金の合計が特定できません。貸借対照表全体を確認する必要があります。
```

LangChain + Retrievalはナラティブな文章(マニュアル、議事録、契約書など)が向いているとのこと

* 表形式はそもそも埋め込みベクトルには向いてない
    * 表の構造が失われやすい
        * テキスト変換時に行・列が崩れる
    * 短くて意味が薄い分が多い
        * 現金 11,111 とかは意味ベクトルになりにくい
    * Embeddingは意味ベース
        * 表は構造と数値による情報が重要

```bash
python app/retrieval_qa2.py
```

IPAの議事録で試してみる

**実行結果**

```text
質問: この会議の目的はなんですか？
回答: この会議の目的は、特定のテーマや問題について議論し、意見を交換して、それに基づいて意思決定を行うことです。 具体的なテーマや問題についての議論や検討が行われる場として開催されています。
```

---

### Prompt Template

```bash
python app/prompt_template.py
```

**実行結果**

```text
入力: 渋谷
応答:
 渋谷は、東京都内にある有名な街です。ここはたくさんのお店やレストランが集まっていて、若者たちに人気のスポットです。渋谷駅は日本でも一番忙しい
```

↑みたいな簡単なものはf文字列やJSのテンプレートリテラルでも実現はできそう（Prompt Templateのメリット活かせてない。。。。）

**Prompt Templateのメリット**

| 特徴                                     | 内容                      |
|----------------------------------------|-------------------------|
| 構造化された定義                               | 	入力変数を明示的に宣言できる         |
| 再利用が前提の設計                              | チェーン・エージェント・ツールと組みやすい   |
| LLMに渡す入力の整形を自動化                        | 変数ミス・入力不足を防げる           |
| LangChain Expression Language（LCEL）と連携 | データフローを関数合成の様にかけちゃう     |
| トレース・可視化に対応                            | LangSmithやデバッグツールと組みやすい |



---

### Memory

```bash
python app/memory_chat.py
```

とりあえずはインメモリで会話履歴の利用をしてみる

**実行結果**
```text
--- 会話スタート ---



> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
[]
Human: おすすめのカフェ教えて
AI:

> Finished chain.
💬 ユーザー: 鹿児島県でおすすめのカフェ教えて
🤖 AI: おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
[HumanMessage(content='おすすめのカフェ教えて', additional_kwargs={}, response_metadata={}), AIMessage(content='おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？', additional_kwargs={}, response_metadata={})]
Human: そこ何時から開いてるの？
AI:

> Finished chain.
💬 ユーザー: そこ何時から開いてるの？
🤖 AI: そのカフェは通常朝8時から夕方6時まで営業しています。週末は遅くまで営業している場合もありますが、具体的な時間はお店のウェブサイトやSNSページで確認することをお勧めします。


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
[HumanMessage(content='おすすめのカフェ教えて', additional_kwargs={}, response_metadata={}), AIMessage(content='おすすめのカフェですね。周辺エリアにはたくさんの素敵なカフェがありますよ。例えば、カフェラテがおいしいと評判の"カフェ・ブランシュ"や、ベーグルが人気の"ベーグルハウス"などがあります。どんな雰囲気のカフェがお好みですか？', additional_kwargs={}, response_metadata={}), HumanMessage(content='そこ何時から開いてるの？', additional_kwargs={}, response_metadata={}), AIMessage(content='そのカフェは通常朝8時から夕方6時まで営業しています。週末は遅くまで営業している場合もありますが、具体的な時間はお店のウェブサイトやSNSページで確認することをお勧めします。', additional_kwargs={}, response_metadata={})]
Human: ちなみに駅から近い？
AI:

> Finished chain.
💬 ユーザー: ちなみに鹿児島中央駅から近い？
🤖 AI: そのカフェは駅から徒歩で約10分程度の距離にあります。比較的アクセスしやすい立地に位置しています。お店に行く際は、地図アプリを利用して道順を確認すると便利ですよ。
```

* 会話履歴は永続化できる？
  * ファイルに保存(開発中の検証・ログ用途に)
  * DBに保存(RDB / NoSQL)
  * LangChainのCustomMemoryを実装
    * 履歴を自動でDynamoDBやRedisに保存復元・セッション毎に管理できそう