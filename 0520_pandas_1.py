import numpy as np
import pandas as pd

# 1. 建立 stock1 (先用 pd.Series 將 list 轉為 Series，pandas 會自動把 None 轉為 NaN)
stock1_list = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(stock1_list)

# 2. 加入商品名稱作為索引，建立 stock2
index_labels = ["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
stock2 = pd.Series(stock1_list, index=index_labels)

# 3. 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# --- 輸出結果 ---

print("stock1")
print(stock1)
print("\n"  + "\n")

print("stock2")
print(stock2)
print("\n" + "\n")

print("stock3")
print(stock3)
print("\n" + "\n")

# 4. 輸出 Banana 的庫存值
print(f"Banana 庫存： {stock2['Banana']}")
print("\n"  + "\n")

# 5. 計算與檢查缺失值
print("缺失值檢查：")
null_check = stock2.isnull()
print(null_check)
print()
print(f"缺失值數量： {null_check.sum()}")

# 6. 把 stock2 存檔為 0520_stock.csv (設定 header=False 符合題目 Series 格式)
stock2.to_csv("0520_stock.csv", header=False)