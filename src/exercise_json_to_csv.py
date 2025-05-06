# 指定したJsonファイルを読み込み
# 各オブジェクトのキーをヘッダー行に、
# 値をcsv形式で出力する関数を実装する
# 例）入力ファイル: sample.json
# [
#   {"name": "John", "age": 30, "city": "New York"},
#   {"name": "Anna", "age": 22, "city": "London"},
#   {"name": "Mike", "age": 32, "city": "Chicago"}
# ]
# 出力ファイル: sample.csv
# name,age,city
# John,30,New York
# Anna,22,London
# Mike,32,Chicago

import json
import csv


def json_to_csv(json_file, csv_file):
    # JSONファイルを開く
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # CSVファイルを開く
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # ヘッダー行を書き込む
        writer.writerow(data[0].keys())

        # 各オブジェクトの値を書き込む
        for item in data:
            writer.writerow(item.values())

# json_to_csvのテスト用関数
def test_json_to_csv():

    # テスト用のJSONデータを作成してファイルに保存                     
    test_json_data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Anna", "age": 22, "city": "London"},
        {"name": "Mike", "age": 32, "city": "Chicago"}
    ]

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(test_json_data, f, ensure_ascii=False, indent=4)

    # JSONファイルをCSVに変換
    json_to_csv('test.json', 'test.csv')

    # CSVファイルの内容を確認
    with open('test.csv', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

# main関数
if __name__ == "__main__":
    # テスト用のJSONファイルをCSVに変換
    test_json_to_csv()
    
    