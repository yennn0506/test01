import pandas as pd

# ===== 方法1：用字典建立 =====
data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54],
}

df1 = pd.DataFrame(data_dict)

# ===== 方法2：用列表（子列表）建立 =====
data_list = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54],
]

df2 = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

# ===== 顯示前5筆 =====
print("--- 前5筆資料 ---")
print(df1.head())
print("\n")

# ===== 顯示後5筆 =====
print("--- 後5筆資料 ---")
print(df1.tail())
print("\n")

# ===== 回傳列數與欄數 =====
print(f"資料維度 (列數, 欄數): {df1.shape}\n")

# ===== 欄位名稱 =====
print(f"欄位名稱: {df1.columns.tolist()}\n")

# ===== 資料型態 =====
print("--- 資料型態 ---")
print(df1.dtypes)
print("\n")

# ===== 非空值數量 =====
print("--- 非空值數量 ---")
print(df1.count())
print("\n")

# ===== 統計資訊（四捨五入到小數點2位）=====
desc = df1.describe().round(2)
print("--- 統計資訊 ---")
print(desc)
print("\n")

# ===== 整理成精美表格並存成 CSV =====
# 幫最左邊的統計指標欄位命名為 "Statistic"，讓 CSV 表格結構更完整
desc.index.name = "Statistic"

# 匯出成 CSV 檔案
desc.to_csv("0520_stock2.csv")
print("【系統提示】統計表格已成功整理並儲存至 '0520_stock2.csv' 檔案中！")