# ベースイメージを指定 (image プロパティ相当)
FROM nvcr.io/nvidia/pytorch:25.04-py3

# ───────────────────────────────
# 1) Git をインストール
#   feature: ghcr.io/devcontainers/features/git:1 相当
RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*


