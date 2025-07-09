# tutorial5_apigee_tool

Google Cloud の Apigee (アピジー) を使ったツールを利用するエージェントです

ApigeeはAPIを一元管理するための仕組みで、ADKから簡単に利用できます。

### 準備
1. Google Cloud コンソールから Apigee を選択する
2. 「SET UP WITH DEFAULTS」をクリックする

### 実行方法
```
# venv環境に入る
source .venv/bin/activate

# ターミナルから実行
cd (root)
cp .env.template .env
# .envを自分で用意した値に設定する
source .env
cd tutorials/tutorial5_apigee_tool
python main.py
```
