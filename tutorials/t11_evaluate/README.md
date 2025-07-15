# tutorial8_evaluate

ADKのEvaluate機能を試します

ADKでは以下の評価を実行できます
- Trajectory: 正しくTool Callingを行えたかを評価する
- Response一致度: 正しく応答できたかを評価する（ROUGEで算出）

### Web UIでの実行
1. `adk web`で立ち上げ、ブラウザからWeb UIにアクセスします
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

### CLIでの実行
Web UIでテストデータを作成したら、それを用いて`adk eval`でCLIから評価できます。
```
cd tutorial8_evaluate
adk eval . evalset7cba40.evalset.json
```

実行結果の例
```
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

### pytestでの実行
1. 事前にファイルの配置に気をつける
    - `tests/integration/test_xxx.py`にテストファイルを配置する
    - その階層の下にevalsetのファイルを配置する (今回の例では`tests/integration/fixture/weather_agent/test_files/weather_agent_evalset.test.json`)
    - `tests/integration/test_xxx.py`でagentディレクトリを指定する（もし`tests.xxx`のようにモジュールとして呼び出すならそれらの階層に`__init__.py`を配置する）
1. PYTHONPATHを現在のディレクトリに設定する
    ```
    export PYTHONPATH=.
    ```
1. pytestを実行する
    ```
    pytest tests/integration
    ```
