# ML-Docker-Playground

このプロジェクトは、機械学習モデルをDockerで開発＆デプロイするためのプレイグラウンドです。

## 特徴

- **Dockerで簡単**: 環境構築がスムーズで再現性も高い。
- **デプロイが容易**: モデルをコンテナ化してすぐにデプロイ可能。

## 必要なもの

- Docker (20.10以上推奨)
- Docker Compose (2.0以上推奨)
- Visual Studio Code (1.60以上推奨)

## 始め方

1. リポジトリをクローン:
    ```bash
    git clone https://github.com/your-username/ML-Docker-Playground.git
    cd ML-Docker-Playground
    ```

2. Dockerイメージをビルド:
    ```bash
    docker-compose build
    ```

3. コンテナを起動:
    ```bash
    docker-compose up
    ```

4. VS Codeの設定を`settings.json`に追加:　　

    ```json
    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.black-formatter",
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.organizeImports": "explicit"
            }
        },
        "isort.args": [
            "--profile",
            "black"
        ]
    }
    ```

5. 必要に応じてVS Codeの設定を適用。**コンテナのパイソンのversionが古い場合にはフォーマッターは自動起動しないので注意**

## 使い方

1. `src/`フォルダにモデルのコードを配置。
2. 必要に応じて`Dockerfile`や`docker-compose.yml`を編集。
3. コンテナ内でモデルをトレーニングまたはデプロイ。

## ディレクトリ構成

```
ML-Docker-Playground/
├── src/                # モデルやスクリプトを配置するフォルダ
├── Dockerfile          # Dockerイメージの設定ファイル
├── docker-compose.yml  # マルチコンテナ設定ファイル
└── README.md           # プロジェクトの説明
```

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)で公開されています。

