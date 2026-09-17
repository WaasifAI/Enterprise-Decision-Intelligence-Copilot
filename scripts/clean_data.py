import pandas as pd
RAW = 'D:\\Enterprise GPT\\data\\raw\\'
PROCESSED = 'D:\\Enterprise GPT\\data\\processed\\'

# customers keeping as it is no cleaning required
df_customers = pd.read_csv(RAW + 'olist_customers_dataset.csv')
df_customers.to_csv(PROCESSED + 'customers.csv', index=False)
print(df_customers.shape)

# products keeping as it is no cleaning required
df_products = pd.read_csv(RAW + 'olist_products_dataset.csv')
df_products.to_csv(PROCESSED + 'products.csv', index=False)
print(df_products.shape)

# orders coverting datetime colums to datetime datatpe
df_orders = pd.read_csv(RAW + 'olist_orders_dataset.csv')
date_colums = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for col in date_colums:
    df_orders[col] = pd.to_datetime(df_orders[col])
    
df_orders.to_csv(PROCESSED + 'orders.csv', index=False)
print(df_orders.shape)

#order_items converting datetime colums to datetime datatpe
df_order_items = pd.read_csv(RAW + 'olist_order_items_dataset.csv')
date_colums = ['shipping_limit_date']
for col in date_colums:
    df_order_items[col] = pd.to_datetime(df_order_items[col])
df_order_items.to_csv(PROCESSED + 'order_items.csv', index=False)
print(df_order_items.shape)

# order_reviews converting datetime colums to datetime datatpe
df_order_reviews = pd.read_csv(RAW + 'olist_order_reviews_dataset.csv')
date_colums = ['review_creation_date', 'review_answer_timestamp']
for col in date_colums:
    df_order_reviews[col] = pd.to_datetime(df_order_reviews[col])
df_order_reviews.to_csv(PROCESSED + 'order_reviews.csv', index=False)
print(df_order_reviews.shape)
 # sellers fixing garbage values in seller_city
df_sellers = pd.read_csv(RAW + 'olist_sellers_dataset.csv')
df_sellers.loc[df_sellers['seller_city'] == '04482255', 'seller_city'] = pd.NA
df_sellers.to_csv(PROCESSED + 'sellers.csv', index=False)
print(df_sellers.shape)
# product_category_name_transalation fixing 2 rows manually
df_product_translation = pd.read_csv(RAW + 'product_category_name_translation.csv')
new_rows = pd.DataFrame({
    'product_category_name': ['pc_gamer', 'portateis_cozinha_e_preparadores_de_alimentos'],
    'product_category_name_english': ['gaming_pc', 'small_appliances_and_food_preparation_devices']
})
df_product_translation = pd.concat([df_product_translation, new_rows], ignore_index=True)
df_product_translation.to_csv(PROCESSED + 'product_category_translation.csv', index=False)
print(df_product_translation.shape)

# geoloacation collapsing multiple rows for same zip code prefix to single row
df_geolocation = pd.read_csv(RAW + 'olist_geolocation_dataset.csv')
df_geolocation_clean = df_geolocation.groupby('geolocation_zip_code_prefix').agg({
    'geolocation_lat': 'mean',
    'geolocation_lng': 'mean',
    'geolocation_city': lambda x: x.mode()[0],
    'geolocation_state': lambda x: x.mode()[0]
}).reset_index()
df_geolocation_clean.to_csv(PROCESSED + 'geolocation.csv', index=False)
print(df_geolocation_clean.shape)

#order_payments fixing 0 installments to 1
df_order_payments = pd.read_csv(RAW + 'olist_order_payments_dataset.csv')
df_order_payments.loc[df_order_payments['payment_installments'] == 0, 'payment_installments'] = 1
df_order_payments.to_csv(PROCESSED + 'order_payments.csv', index=False)
print(df_order_payments.shape)

