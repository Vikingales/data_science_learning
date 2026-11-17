-- 1. Table of product categories
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

-- 2. Table of users (sellers and buyers)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    country VARCHAR(30) NOT NULL,
    created_at DATE NOT NULL
);

-- 3. Table of items (offered for sale)
CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    seller_id INT NOT NULL REFERENCES users(user_id),
    title VARCHAR(100) NOT NULL,
    category_id INT NOT NULL REFERENCES categories(category_id),
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'sold', 'reserved'))
);

-- 4. Orders/transactions table (records the fact that a product was purchased by a buyer)
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL UNIQUE REFERENCES items(item_id), -- One item can be sold once
    buyer_id INT NOT NULL REFERENCES users(user_id),
    order_date DATE NOT NULL,
    shipping_fee NUMERIC(5, 2) NOT NULL CHECK (shipping_fee >= 0)
);


INSERT INTO categories (category_name) VALUES 
('Clothing'), ('Shoes'), ('Accessories'), ('Jewelry'), ('Toys');

INSERT INTO users (username, country, created_at) VALUES
('anna_vinted', 'Lithuania', '2025-01-15'),
('marius_lt', 'Lithuania', '2025-03-20'),
('elena_shop', 'Latvia', '2025-06-10'),
('tomas_k', 'Estonia', '2025-08-01');

INSERT INTO items (seller_id, title, category_id, price, status) VALUES
(1, 'Vintage Levi''s Jeans', 1, 35.00, 'sold'),
(1, 'Nike Air Max Sneakers', 2, 60.00, 'active'),
(2, 'Wool Winter Coat', 1, 85.00, 'sold'),
(3, 'Leather Backpack', 3, 45.00, 'active'),
(3, 'Silver Ring', 4, 20.00, 'sold'),
(4, 'Board Game Set', 5, 25.00, 'active'),
(1, 'Summer Floral Dress', 1, 25.00, 'sold');

INSERT INTO orders (item_id, buyer_id, order_date, shipping_fee) VALUES
(1, 2, '2025-10-01', 3.49), -- Marius bought jeans from Anna
(3, 4, '2025-10-05', 4.50), -- Tomas bought coat from Marius
(5, 1, '2025-10-10', 2.99), -- Anna bought ring from Elena
(7, 2, '2025-10-12', 3.49); -- Marius bought dress from Anna