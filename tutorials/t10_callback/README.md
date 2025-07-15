# tutorial9_callback

ADKのCallbackを試します

CallbackはAgentが実行する前、実行した後の処理を定義できます

これにより、Agentが持つstateに応じて処理を分岐したり、特定の入力時に特定の応答を返したりできます

### 実行方法
以下で`before_agent_callback`の挙動が試せます
```
cd tutorial9_callback
python main_before_agent_callback.py
```

次に、以下でモデルの入出力の編集が試せます
(出力の変更はすぐに確認できると思います。入力の変更を確認したい場合は、23行目の`new_user_message`に好きな入力を設定してみるとそれに応じて出力が変わることにより確認できます)
```
cd tutorial9_callback
python main_edit_inout.py
```

### Callbackの設定方法
Agentには以下の6つの引数を設定できます
- `before_agent_callback`: Agentが本来の処理を実行する前に実行される関数を設定
- `before_model_callback`: LLMを実行する前に処理される関数を設定
- `before_tool_callback`: Toolを実行する前に処理される関数を設定
- `after_agent_callback`: Agentが本来の処理を実行した後に実行される関数を設定
- `after_model_callback`: LLMを実行した後に処理される関数を設定
- `after_tool_callback`: Toolを実行した後に処理される関数を設定


以下のように設定します
```
root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    before_agent_callback=check_if_agent_should_run # Callbackを設定します
)
```

### Callbackの用途
- ガードレール: 不適切な表現が入力された場合に、固定・編集した応答を返す
- ログ出力: Agentの応答前後の入出力をログに保存する
- ツールのキャッシュ: ツールの入出力結果を保持しておき、前回と同じ値が入力された場合に即座に結果を返す
- ツールの入出力値の変換: 例えば"東京"と入力されたら、"Tokyo"と変換するなど
- ツールの認証: 特定のツールが実行されるときに、認証ステップを実行する
- 画像などのArtifactを扱う: `before_agent_callback`でアップロードされたArtifactをloadする / AgentがArtifactを生成した場合は`after_agent_callback`でArtifactをsaveする


### Callbackの注意点
- Callbackの引数にはいくつか種類があるので注意する（`before_model_callback`と`before_agent_callback`など）
    - `before_agent_callback→types.Content` : エージェントのメイン実行ロジック ( _run_async_impl/ _run_live_impl) をスキップします。返されたContentオブジェクトは、そのターンのエージェントの最終出力として即座に扱われます。単純なリクエストを直接処理したり、アクセス制御を適用したりするのに便利です。
    - `before_model_callback→LlmResponse` : 外部の大規模言語モデル（LLM）への呼び出しをスキップします。返されたLlmResponseオブジェクトは、LLMからの実際のレスポンスであるかのように処理されます。入力ガードレール、プロンプト検証、キャッシュされたレスポンスの提供などに最適です。
    - `before_tool_callback→dictまたはMap`: 実際のツール関数（またはサブエージェント）の実行をスキップします。返された値はdictツール呼び出しの結果として使用され、通常はLLMに返されます。ツール引数の検証、ポリシー制限の適用、またはモック/キャッシュされたツール結果の返送に最適です。
    - `after_agent_callback→types.Content` :エージェントの実行ロジックによって生成された を置き換えます。Content
    - `after_model_callback→LlmResponse` : LLMから受信したものを置き換えますLlmResponse。出力のサニタイズ、標準的な免責事項の追加、LLMのレスポンス構造の変更に役立ちます。
    - `after_tool_callback→dictまたはMap`:ツールから返された結果を置き換えますdict。ツールの出力をLLMに送り返す前に、後処理または標準化を行うことができます。
- この処理では、(1)Agentに処理をさせずに特定の応答を出力する、(2)何もせずAgentを実行する、しかできないかも。「特定のフレーズを変換してAgentを実行する」などはできなそう。（調査中）


