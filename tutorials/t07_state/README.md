# t07_state - セッションと状態管理

## 概要
ADKのSession & Memory機能の使用方法を学ぶためのチュートリアルです。エージェントの状態管理、セッション管理、メモリ機能の活用方法を実装します。

## 学習内容
- `InMemorySessionService`を使用したセッション管理
- `output_key`パラメータによるエージェント応答の状態保存
- `session_service.append_event()`による状態更新

## 実行方法

### 1. エージェント応答の状態保存
```bash
cd tutorials/t07_state
python main0_state.py
```

### 2. session_service.append_event()による状態更新
```bash
cd tutorials/t07_state
python main1_append_event.py
```

### 3. Callback関数内での状態更新
```bash
cd tutorials/t07_state
python main2_state_in_callback.py
```