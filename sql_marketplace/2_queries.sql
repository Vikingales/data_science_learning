-- QUERY 1: Calculate total revenue and sold items per seller
-- Skills I applied: INNER JOIN, GROUP BY, Aggregate functions (SUM, COUNT), ORDER BY
SELECT 
    u.username,
    COUNT(i.item_id) AS total_sold_items,
    SUM(i.price) AS total_revenue
FROM users u
JOIN items i ON u.user_id = i.seller_id
WHERE i.status = 'sold'
GROUP BY u.username
ORDER BY total_revenue DESC;


-- QUERY 2: Find the average price of sold items grouped by category
-- Skills I applied: Filtering (WHERE), Aggregation (COUNT, AVG), Rounding, GROUP BY
SELECT 
    category,
    COUNT(item_id) AS items_count,
    ROUND(AVG(price), 2) AS avg_price
FROM items
WHERE status = 'sold'
GROUP BY category;


-- QUERY 3: Retrieve top-3 most expensive active listings on the platform
-- Skills I applied: Data filtering, Sorting (ORDER BY DESC), and Result restriction (LIMIT)
SELECT 
    title,
    category,
    price
FROM items
WHERE status = 'active'
ORDER BY price DESC
LIMIT 3;

-- QUERY 4: Full transaction breakdown (Buyer, Seller, Item, Category, Revenue)
-- Skills I applied: Multi-table JOINs (4 tables), Aliasing, Date filtering
SELECT 
    o.order_id,
    o.order_date,
    buyer.username AS buyer_name,
    seller.username AS seller_name,
    i.title AS item_title,
    c.category_name,
    i.price,
    o.shipping_fee
FROM orders o
JOIN users buyer ON o.buyer_id = buyer.user_id
JOIN items i ON o.item_id = i.item_id
JOIN users seller ON i.seller_id = seller.user_id
JOIN categories c ON i.category_id = c.category_id
ORDER BY o.order_date DESC;