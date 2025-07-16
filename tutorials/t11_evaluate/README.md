# t11_evaluate - ADKの評価機能

## 概要
ADKの評価機能を学ぶためのチュートリアルです。Tool Callingの正確性評価やレスポンスの一致度評価（ROUGE）の方法を実装します。

## 学習内容
- `adk eval`コマンドによる評価の実行
- Trajectory評価（Tool Callingの正確性）
- Response一致度評価（ROUGEスコア）

## 評価の種類
- **Trajectory**: 正しくTool Callingを行えたかを評価
- **Response一致度**: 正しく応答できたかを評価（ROUGEで算出）

### (注意)
現在日本語のトークナイズが機能しておらず、Response一致度では完全一致でない限りスコアが0になってしまうことが確認されています

## 実行方法

### Web UIでの評価データ作成
1. `adk web`で立ち上げ、ブラウザから`localhost:8080`を開き、ドロップダウンメニューより`t11_evaluate`を選択する
    ```bash
    cd tutorials/t11_evaluate
    adk web
    ```
1. 左のパネルから「Eval」を選択します
1. 新規作成の場合は"+"ボタンから eval set を作成します
1. テストデータを作成します
    1. Agentと会話をします
    1. 左のパネルの「+Add current session to evalsetXXX」をクリックします
1. もしAgentの応答が希望するものではない場合、テストケースを選択して編集します
    1. テストケースを選択したら画面右上の鉛筆マーク(カーソルを合わせたら「Edit current eval case」が表示されます)をクリックします
    1. そのセッションの中で編集したい応答の右側に表示されている鉛筆マークをクリックします
    1. 編集が完了したらチェックマークをクリックします
    1. そのセッションの編集が完了したら、右上の「Save」ボタンをクリックします（これを忘れると編集が保存されません）
1. 実行したいテストケースを選択します（全ての場合はテストケース一番上の四角にチェックを入れると、全てのテストケースが選択されます）
1. 「Run Evaluation」をクリックし、Evaluation Metricの設定が済んだら「Start」をクリックします

![](/assets/adk_eval.gif)


### CLIでの評価実行
```bash
cd tutorials/t11_evaluate
adk eval . evalset7cba40.evalset.json
```

### 実行結果の例
```bash
~/adk-python-tutorials/tutorials/tutorial8_evaluate $ adk eval . evalset7cba40.evalset.json
Using evaluation criteria: {'tool_trajectory_avg_score': 1.0, 'response_match_score': 0.8}
Running Eval: evalset7cba40:case47a35f
Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Result: ✅ Passed

Running Eval: evalset7cba40:casee0a273
WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Result: ❌ Failed

Running Eval: evalset7cba40:case05fb1a
Result: ❌ Failed

Running Eval: evalset7cba40:case9292e5
WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Result: ✅ Passed

Running Eval: evalset7cba40:casef415f4
WARNING:google_genai.types:Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Result: ✅ Passed

*********************************************************************
Eval Run Summary
evalset7cba40:
  Tests passed: 3
  Tests failed: 2
```

### pytestでの評価実行

事前にファイルの配置に気をつける
- `tests/integration/test_xxx.py`にテストファイルを配置する
- その階層の下にevalsetのファイルを配置する (今回の例では`tests/integration/fixture/weather_agent/test_files/weather_agent_evalset.test.json`)
- `tests/integration/test_xxx.py`でagentディレクトリを指定する（もしこのファイル内で`tests.xxx`のようにモジュールとしてimportするならそれらの階層に`__init__.py`を配置する）

```bash
export PYTHONPATH=.
pytest tests/integration
```


## 評価基準の設定
`test_config.json`で評価基準を設定：
```json
{
    "criteria": {
        "tool_trajectory_avg_score": 1.0,
        "response_match_score": 0.8
    }
}
```