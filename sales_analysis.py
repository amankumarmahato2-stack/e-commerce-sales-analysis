
import pandas as pd
import matplotlib.pyplot as plt

# Load sales dataset
data = pd.read_csv("sales_data.csv")

# Calculate revenue
data["Revenue"] = data["Quantity"] * data["Price"]

# Total revenue
total_revenue = data["Revenue"].sum()

# Total orders
total_orders = data["Order_ID"].nunique()

# Average order value
average_order = total_revenue / total_orders

# Best-selling products
product_sales = data.groupby("Product")["Quantity"].sum()

# Monthly revenue
monthly_sales = data.groupby("Month")["Revenue"].sum()

# Display results
print("TOTAL REVENUE:", total_revenue)
print("TOTAL ORDERS:", total_orders)
print("AVERAGE ORDER VALUE:", average_order)

print("\nPRODUCT SALES:")
print(product_sales)

print("\nMONTHLY SALES:")
print(monthly_sales)

# Create monthly sales chart
monthly_sales.plot(kind="bar", title="Monthly Sales Analysis")

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("monthly_sales.png")
plt.show()
