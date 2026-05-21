import pandas as pd

# 1. 讀取檔案
file_path = 'Grocery_Inventory_and_Sales_Dataset.csv'
df = pd.read_csv(file_path)

print("--- 資料成功載入，開始進行強力資料清理 ---")

# 🛠️ 強力清理：把所有欄位中的 $、逗號、空格都清乾淨，並轉成數字
for col in ['Unit_Price', 'Stock_Quantity', 'Sales_Volume']:
    # 確保欄位存在才處理
    if col in df.columns:
        # 強制轉成字串，去掉 $ 和 , 和 空格
        df[col] = df[col].astype(str).str.replace('$', '', regex=False)
        df[col] = df[col].str.replace(',', '', regex=False)
        df[col] = df[col].str.strip()
        # 最後轉換成浮點數數字型態
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 檢查轉換後的資料型態是否成功變成 float64 或 int64
print("\n[檢查欄位型態] 應皆為 float64 或 int64：")
print(df[['Unit_Price', 'Stock_Quantity', 'Sales_Volume']].dtypes)

print("-" * 50)

# ----------------------------------------------------
# 2. 開始核心計算

# (1) 計算每個商品的總庫存價值
df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']
print("\n(1) 每個商品的總庫存價值已計算完成：")
print(df[['Product_Name', 'Stock_Quantity', 'Unit_Price', 'Total_Inventory_Value']].head())


# (2) 找出最暢銷的商品
# 依【總銷量】來看
best_by_volume = df.loc[df['Sales_Volume'].idxmax()]

# 依【銷售總額】來看
df['Sales_Revenue'] = df['Sales_Volume'] * df['Unit_Price']
best_by_revenue = df.loc[df['Sales_Revenue'].idxmax()]

print("\n(2) 最暢銷商品分析結果：")
print(f"👉 依【總銷量】來看，最暢銷的是：{best_by_volume['Product_Name']}（售出 {int(best_by_volume['Sales_Volume'])} 件）")
print(f"👉 依【銷售總額】來看，最暢銷的是：{best_by_revenue['Product_Name']}（總銷售額 ${best_by_revenue['Sales_Revenue']:.2f}）")


# (3) 計算 9 折後的總收入
df['Discounted_Revenue'] = df['Sales_Revenue'] * 0.9
total_discounted_revenue = df['Discounted_Revenue'].sum()

print("\n(3) 9 折後的收入計算結果：")
print(f"👉 所有商品打 9 折後的總收入為：${total_discounted_revenue:.2f}")
