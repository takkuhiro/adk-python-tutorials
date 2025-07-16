# t12_artifacts - バイナリデータの管理

## 概要
ADKのArtifacts機能の使用方法を学ぶためのチュートリアルです。バイナリデータ（画像、ファイル、音声など）の管理とLLMでの利用方法を実装します。

cf. 公式ドキュメント: [Artifacts](https://google.github.io/adk-docs/artifacts/)

## 学習内容
- `InMemoryArtifactService`を使用したバイナリデータの管理
- `before_model_callback`でのArtifactの保存と読み込み
- 画像データのLLMへの入力方法

## 実行方法

### 1. 画像を直接入力として与える
```bash
cd tutorials/t12_artifacts
python main_image_input.py
```

### 2. ArtifactServiceを使った保存・読み込み
```bash
cd tutorials/t12_artifacts
python main_artifacts.py
```

## ArtifactServiceの使い方
- `before_model_callback`で呼び出す（`before_agent_callback`ではない）
- `callback_context.save_artifact()`でバイナリデータを保存
- `callback_context.load_artifact()`で保存したデータを読み込み
- LLMへの入力は`llm_request`を編集して直接挿入
- LLMが生成したファイルは`after_model_callback`でArtifact Serviceに保存する
