import pandas as pd

# 1. 讀取 Kaggle 超市分析資料檔案
file_name = "SuperMarket Analysis.csv"
df = pd.read_csv(file_name)

# 2. 檢視資料筆數與前幾筆內容
print("=== Step 1: 檢視資料筆數與前幾筆內容 ===")
print(f"資料總筆數: {len(df)} 筆\n")
print("前 5 筆資料內容:")
print(df.head())
print("-" * 60)

# 3. 篩選出 Branch 為 A 且 Customer type 為 Member 的交易資料
print("=== Step 2: 篩選 Branch 為 A 且為 Member 的資料 ===")
filtered_df = df[(df['Branch'] == 'A') & (df['Customer type'] == 'Member')]
print(f"篩選後的交易筆數: {len(filtered_df)} 筆\n")
print("篩選後的前 5 筆內容:")
print(filtered_df.head())
print("-" * 60)

# 4. 以 Product line 為單位，計算 總銷售額（Sales）與 平均評分（Rating）
print("=== Step 3: 各產品線銷售額與平均評分彙總 ===")
# 註：若原始欄位名為 Total，請將 'Sales' 替換為 'Total'
prod_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2)

# 重新命名欄位以符合題目規範
prod_summary.columns = ['Total Sales', 'Average Rating']
print(prod_summary)
print("-" * 60)

# 5. 依 City 與 Gender 分組，計算平均銷售額與交易筆數
print("=== Step 4: 依 City 與 Gender 分組計算 ===")
city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Sales', 'count')
).round(2)
print(city_gender_summary)
print("-" * 60)

# 6. 找出總銷售額最高的產品線
highest_sales_product = prod_summary['Total Sales'].idxmax()
highest_sales_value = prod_summary['Total Sales'].max()
print("=== Step 5: 找出總銷售額最高的產品線 ===")
print(f"總銷售額最高的產品線為: {highest_sales_product}，總金額為: ${highest_sales_value:.2f}")
print("-" * 60)

# 7. 將產品線的銷售與評分彙總結果輸出為 0520_pandas_3OK.CSV
output_file = "0520_pandas_3OK.CSV"
prod_summary.to_csv(output_file)
print(f"=== Step 6: 彙總結果已成功匯出至檔案 '{output_file}' ===")