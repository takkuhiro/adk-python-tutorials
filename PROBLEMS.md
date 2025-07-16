# Problems

ここではエラー集を記録していきます。

もしADKで使っている時に困ったことがあったらこちらを確認してください。

### Web UIで全文を入力できない
日本語入力の場合、Enterを押さないように心がけてください。
「Shift + Enter」とすることで改行できます。


### Callback関数が実行できない
入力変数は`context`ではなく、`callback_context`でないといけない。

### 入力で特定の文字をリプレイスしたいときは？
`before_model_callback`関数（`before_agent_callback`ではない）では`llm_response`を引数に取れるので、これを直接編集し、`return None`で返す

### is_final_response が Agent Engine　では取得できない
現時点では、Agent Engineからのレスポンスには is_final_response の情報が含まれていない

### adk web でしか実行できない / python main.py でしか実行できない
それぞれの場合でagentやtoolのimport方法が異なります

具体的にはadk webでは相対パスでの参照が必要になります

```
# adk web
from .agent import root_agent
from .tools import my_tool

# python main.py
from agent import root_agent
from tools import my_tool
```

