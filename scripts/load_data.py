import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()
db_url = os.getenv("DATABASE_URL").replace("postgresql://", "postgresql+psycopg://", 1)
engine = create_engine(db_url)
PROCESSED = 'D:\\Enterprise GPT\\data\\processed\\'

'''# 1 loading customers data into the database
df_customers = pd.read_csv(PROCESSED + 'customers.csv')
df_customers.to_sql('customers', engine, if_exists='append', index=False)
print(f"customers data loaded into the database successfully: {len(df_customers)} records")

# 2 loading sellers data into the database
df_sellers = pd.read_csv(PROCESSED + 'sellers.csv')
df_sellers.to_sql('sellers', engine, if_exists='append', index=False)
print(f"sellers data loaded into the database successfully: {len(df_sellers)} records")

# 3 loading products data into the database
df_products = pd.read_csv(PROCESSED + 'products.csv')
df_products.to_sql('products', engine, if_exists='append', index=False)
print(f"products data loaded into the database successfully: {len(df_products)} records")

# 4 loading product_category_translation data into the database
df_product_category_translation = pd.read_csv(PROCESSED + 'product_category_translation.csv')
df_product_category_translation.to_sql('product_category_translation', engine, if_exists='append', index=False)
print(f"product_category_translation data loaded into the database successfully: {len(df_product_category_translation)} records")

# 5 loading geolocation data into the database
df_geolocation = pd.read_csv(PROCESSED + 'geolocation.csv')
df_geolocation.to_sql('geolocation', engine, if_exists='append', index=False)
print(f"geolocation data loaded into the database successfully: {len(df_geolocation)} records")'''

# 6 loading orders data into the database
df_orders = pd.read_csv(PROCESSED + 'orders.csv', parse_dates=[
    'order_purchase_timestamp', 'order_approved_at',
    'order_delivered_carrier_date', 'order_delivered_customer_date',
    'order_estimated_delivery_date'
])
df_orders.to_sql('orders', engine, if_exists='append', index=False)
print(f"orders data loaded into the database successfully: {len(df_orders)} records")

# 7 loading order_items data into the database  
df_order_items = pd.read_csv(PROCESSED + 'order_items.csv', parse_dates=['shipping_limit_date'])
df_order_items.to_sql('order_items', engine, if_exists='append', index=False)
print(f"order_items data loaded into the database successfully: {len(df_order_items)} records")

# 8 loading order_payments data into the database
df_order_payments = pd.read_csv(PROCESSED + 'order_payments.csv')
df_order_payments.to_sql('order_payments', engine, if_exists='append', index=False)
print(f"order_payments data loaded into the database successfully: {len(df_order_payments)} records")

# 9 loading order_reviews data into the database
df_order_reviews = pd.read_csv(PROCESSED + 'order_reviews.csv', parse_dates=['review_creation_date', 'review_answer_timestamp'])
df_order_reviews.to_sql('order_reviews', engine, if_exists='append', index=False)
print(f"order_reviews data loaded into the database successfully: {len(df_order_reviews)} records")



