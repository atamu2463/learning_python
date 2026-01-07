# リスト型とリスト操作(他言語の配列に相当)
# 配列と違い、可変長で型が異なるデータを混在させられる

# リスト定義または別のデータをリストに変換・・・list()を使用
chars = list("ABC")
print(chars)  #出力： ['A', 'B', 'C']

# リストへ要素を追加
# リストの末尾に追加・・・append()を使用
fruits = ["りんご", "バナナ"]
fruits.append("みかん")
print(fruits) # 出力：['りんご', 'バナナ', 'みかん']

# リストの特定位置に要素を挿入・・・insert()を使用
fruits.insert(1, "ぶどう")
print(fruits) # 出力：['りんご', 'ぶどう', 'バナナ', 'みかん']

# リストのすべての要素を削除・・・clear()を使用
fruits.clear()
print(fruits) # 出力：[]

# リストから指定した値のうち最初の1つを削除・・・remove()を使用
fruits = ["りんご", "バナナ", "みかん"]
fruits.remove("バナナ")
print(fruits) # 出力：['りんご', 'みかん']

# リストの要素数を取得・・・len()を使用
print(len(fruits)) # 出力：3   

