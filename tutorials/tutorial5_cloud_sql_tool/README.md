# tutorial5_cloud_sql_tool

[Toolbox](https://googleapis.github.io/genai-toolbox/getting-started/introduction/) を使って Cloud Run と接続します

### 注意事項

現時点(2025/07/09)では、このAgentをGoogle Cloud上のAgent Engineにデプロイすることはできませんでした。
これは、ADKで提供されている`ToolboxSyncClient`がJSONシリアライズできないためです。
cf. https://github.com/google/adk-python/issues/856

### 実行方法
1. Cloud SQLのインスタンスを作成する (以下は一例です)
    1. Google Cloud コンソールを開き、Cloud SQLを選択する
    1. "CREATE INSTANCE" -> "Choose PostgreSQL" -> "Enterprise", "Sandbox"を選択する
    1. Instance IDに"adk-python-tutorials", Passwordに"postgresql-password"を入力する
    1. 安く済ませたいので、Customize your instance > Machine configuration > Machine で、"Shared core"の"1 vCPU, 0.614 GB"を選択する
    1. "CREATE INSTANCE"をクリックする
    1. インスタンスが起動するまで数分待つ
1. Cloud SQLにモックデータを入れる
    1. サイドバーより"Cloud SQL Studio"を選択する
    1. 先ほど設定した情報を入力して"Authenticate"をクリックする
    1. 以下のSQL文を順に実行し、モックデータを作成する
        ```
        CREATE TABLE memory(
            id            VARCHAR NOT NULL PRIMARY KEY,
            content       VARCHAR NOT NULL,
            created_at    TIMESTAMP NOT NULL,
            updated_at    TIMESTAMP NOT NULL,
            deleted BOOLEAN NOT NULL
        );

        INSERT INTO memory(id, content, created_at, updated_at, deleted)
        VALUES
            ('0197ee13-b181-7505-af2a-c6b314424fb9', '趣味はギターです', '2025-01-01 14:00:00', '2025-01-01 14:00:00', false),
            ('0197ee14-5e5b-7561-9ce3-1be44b64dbd9', 'アボカドが好きです', '2025-01-01 14:00:00', '2025-01-01 14:00:00', false);
        ```

1. tools.yamlを修正する
    - DB情報は先ほど作成した自身のインスタンスの情報に置き換えてください
    - このファイルでは先ほど作成した`memory`テーブルへのCRUD操作のSQLを定義します

1. toolboxをCloud Runにデプロイする
    - 参考: [codelab: データベース向け MCP ツールボックスとエージェント開発キット（ADK）を使用して旅行代理店を構築する](https://codelabs.developers.google.com/travel-agent-mcp-toolbox-adk?hl=ja)
    - 参考: [MCP Toolbox for Databases](https://googleapis.github.io/genai-toolbox/how-to/deploy_toolbox/)

    1. Google Cloud サービスを有効にする
        ```
        gcloud services enable run.googleapis.com \
                       cloudbuild.googleapis.com \
                       artifactregistry.googleapis.com \
                       iam.googleapis.com \
                       secretmanager.googleapis.com
        ```
    1. tools.yamlをsecretsとしてアップロードする
        ```
        gcloud secrets create tools --data-file=tools.yaml
        # 追加時は以下を代わりに実行する
        # gcloud secrets versions add tools --data-file=tools.yaml
        ```
    1. Cloud Run用のService Accountを作成し、権限をつける
        ```
        gcloud iam service-accounts create toolbox-identity

        gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member serviceAccount:toolbox-identity@$PROJECT_ID.iam.gserviceaccount.com \
           --role roles/secretmanager.secretAccessor

        gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member serviceAccount:toolbox-identity@$PROJECT_ID.iam.gserviceaccount.com \
           --role roles/cloudsql.client
        ```
    1. ToolboxをCloud Runにデプロイする
        ```
        gcloud run deploy toolbox \
            --image us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:latest \
            --service-account toolbox-identity \
            --region us-central1 \
            --set-secrets "/app/tools.yaml=tools:latest" \
            --args="--tools-file=/app/tools.yaml","--address=0.0.0.0","--port=8080" \
            --allow-unauthenticated
        ```
    1. .envの環境変数`MCP_TOOLBOX_URL=xxx`にデプロイしたURLを記入する
    1. `source ~/.env`で環境変数を読み込む
1. `adk web`で起動して確認する
    - 試しに「私の趣味を覚えていますか？」のように尋ねて、適切に"search-memory"が呼び出されてDBと接続できていることを確認する
