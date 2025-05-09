# ベースイメージを指定 (image プロパティ相当)
FROM nvcr.io/nvidia/pytorch:25.04-py3

# ───────────────────────────────
# 1) Git をインストール
#   feature: ghcr.io/devcontainers/features/git:1 相当
RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*


# ───────────────────────────────
# 2) Node.js 18.x をインストール
#    curl がなければ先に導入し、NodeSource のセットアップスクリプトで nodejs を追加します。
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
 && apt-get install -y --no-install-recommends nodejs \
 && rm -rf /var/lib/apt/lists/*

 RUN pip install --no-cache-dir python-dotenv