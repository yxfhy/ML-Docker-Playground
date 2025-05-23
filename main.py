# main.py


import argparse
import os

from dotenv import load_dotenv


def process_parameters(param1: str, param2: str, param3: str) -> str:
    # Process the parameters and return a result
    print("Processing parameters...")
    return f"Processed parameters: {param1}, {param2}, {param3}"


def main():

    # 引数のパース

    parser = argparse.ArgumentParser(
        description="ML Docker Playground サンプルスクリプト"
    )

    parser.add_argument("--name", type=str, default="world", help="挨拶する相手の名前")
    args = parser.parse_args()

    # .env の読み込み
    load_dotenv()

    greeting = os.getenv("GREETING", "Hello")

    # 実行
    print(f"{greeting}, {args.name}!")


if __name__ == "__main__":
    main()
