# tutorial

ADKの Session & Memory を試します


### 実行方法
エージェント応答は`output_key`を指定することでStateに保存できることを確認します
```
cd tutorial11_state
python main0_state.py
```

次に`session_service.append_event()`からstateを更新できることを確認します
```
cd tutorial11_state
python main1_append_event.py
```

最後にCallbak関数内でstateを更新できることを確認します
```
cd tutorial11_state
python main2_state_in_callback.py
```