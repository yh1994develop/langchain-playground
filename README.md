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