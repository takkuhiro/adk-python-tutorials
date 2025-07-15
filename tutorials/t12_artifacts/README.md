# tutorial9_artifacts

ADKのArtifactsを試します

Artifactsを利用することで、バイナリデータがバージョン管理された状態で利用できます

これにより、テキストだけでなく、ファイル、画像、音声などをLLMが扱うことができます

### 実行方法
画像を入力として直接バイナリデータで与える
```
cd tutorial10_artifacts
python main_image_input.py
```

次にArtifactServiceを使って、バイナリデータをArtifactServiceに保存・呼び出しできることを確認する
```
cd tutorial10_artifacts
python main_artifacts.py
```

### ArtifactServiceの使い方
ArtifactServiceはCallback（特に`before_model_callback`で呼び出す。`before_agent_callback`ではない。）で呼び出すことに注意

`before_model_callback`では`llm_request`を引数として受け取れるので、Artifact Serviceから呼び出したバイナリデータはここで`llm_request`を編集して直接挿入する

また、LLMが生成したファイルは`after_model_callback`でArtifact Serviceに保存すれば良い
