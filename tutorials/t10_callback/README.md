# t10_callback - ADKのCallback機能

## 概要
ADKのCallback機能の使用方法を学ぶためのチュートリアルです。

Callbackにより、エージェントの実行前後での処理を追加することができます。

## 学習内容
- `before_agent_callback`を使用したエージェント実行前の制御
- `CallbackContext`を使用した状態アクセスとエージェント実行制御
- モデルの入出力編集

## Callbackの種類

| コールバック | 実行タイミング | 用途 |
|------------|--------------|------|
| `before_agent_callback` | エージェントの処理実行前（`_run_async_impl` / `_run_live_impl`の前） | アクセス制御 |
| `before_model_callback` | LLM実行前 | 入力ガードレール・プロンプト検証・キャッシュされたレスポンスの提供 |
| `before_tool_callback` | Tool実行前 | ツール引数の検証・キャッシュされたツール結果の提供 |
| `after_agent_callback` | エージェントの処理実行後 | 出力ガードレール・固定文言の追加・出力の編集 |
| `after_model_callback` | LLM実行後 | 出力ガードレール・固定文言の追加・出力の編集 |
| `after_tool_callback` | Tool実行後 | ツールの後処理や標準化 |

## Callbackの設定方法
```python
root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    before_agent_callback=check_if_agent_should_run # Callbackを設定します
)
```

## 実行方法

### 1. before_agent_callbackの動作確認
```bash
cd tutorials/t10_callback
python main_before_agent_callback.py
```

### 2. モデルの入出力編集
```bash
cd tutorials/t10_callback
python main_edit_inout.py
```

## Callbackの用途
- ガードレール: 不適切な表現の検出と応答の固定化
- ログ出力: エージェントの入出力をログに保存
- ツールのキャッシュ: ツールの実行結果をキャッシュ
- 入出力値の変換: 例：「東京」→「Tokyo」への変換
- ツールの認証: 特定ツール実行時の認証ステップ
- Artifactの処理: 画像等のバイナリデータの前処理・後処理
