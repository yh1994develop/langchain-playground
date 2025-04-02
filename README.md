# LangChain Playground

学習用のLangChainリポジトリ

OpenAIの安価なモデル（gpt-3.5-turbo）を使って、基本的なChainやRetrievalなどを段階的に試す

## setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### basic chain
* プロンプトに「日本の都道府県で人口が一番多いのはどこ？理由も説明して。」を投げてみる
```bash
python app/basic_chain.py
```