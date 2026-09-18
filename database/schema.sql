-- creating the postgres database schema with 9 tables, their relationships and constraints
-- TABLE 1 CUSTOMERS
CREATE TABLE customers(
    customer_id TEXT NOT NULL,
    customer_unique_id TEXT NOT NULL,
    customer_zip_code_prefix INT NOT NULL,
    customer_city TEXT NOT NULL,
    customer_state TEXT NOT NULL,
    PRIMARY KEY (customer_id)
);

-- TABLE 2 SELLERS
CREATE TABLE sellers(
    seller_id TEXT NOT NULL,
    seller_zip_code_prefix INT NOT NULL,
    seller_city TEXT,
    seller_state TEXT NOT NULL,
    PRIMARY KEY (seller_id)
);

-- TABLE 3 PRODUCTS
CREATE TABLE products(
    product_id TEXT NOT NULL,
    product_category_name TEXT,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT,
    PRIMARY KEY (product_id)
);

-- TABLE 4 PRODUCT CATEGORY TRANSLATIONS
CREATE TABLE product_category_translation(
    product_category_name TEXT NOT NULL,
    product_category_name_english TEXT NOT NULL,
    PRIMARY KEY (product_category_name)
);

-- TABLE 5 GEOLOCATION
CREATE TABLE geolocation(
    geolocation_zip_code_prefix INT NOT NULL,
    geolocation_lat DOUBLE PRECISION NOT NULL,
    geolocation_lng DOUBLE PRECISION NOT NULL,
    geolocation_city TEXT NOT NULL,
    geolocation_state TEXT NOT NULL,
    PRIMARY KEY (geolocation_zip_code_prefix)
);

-- TABLE 6 ORDERS
CREATE TABLE orders(
    order_id TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    order_status TEXT NOT NULL,
    order_purchase_timestamp TIMESTAMP NOT NULL,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- TABLE 7 ORDER ITEMS
CREATE TABLE order_items(
    order_id TEXT NOT NULL,
    order_item_id INT NOT NULL,
    product_id TEXT NOT NULL,
    seller_id TEXT NOT NULL,
    shipping_limit_date TIMESTAMP NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    freight_value NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id),
    CHECK (price >= 0),
    CHECK (freight_value >= 0)
);

-- TABLE 8 ORDER PAYMENTS
CREATE TABLE order_payments(
    order_id TEXT NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type TEXT NOT NULL,
    payment_installments INT NOT NULL,
    payment_value NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (order_id, payment_sequential),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CHECK (payment_value >= 0),
    CHECK (payment_installments >= 1)
);

-- TABLE 9 ORDER REVIEWS
CREATE TABLE order_reviews(
    review_id TEXT NOT NULL,
    order_id TEXT NOT NULL,
    review_score INT NOT NULL,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP NOT NULL,
    review_answer_timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY (review_id, order_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CHECK (review_score BETWEEN 1 AND 5)

);