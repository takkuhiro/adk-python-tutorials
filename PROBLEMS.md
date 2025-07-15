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

### is_final_responseがAgent Engineでは取得できない
これは現在解決されていない問題

