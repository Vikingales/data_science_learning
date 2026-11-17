# My Python & SQL Learning Journey 

Hi! I'm Aliaksandra, a QA Engineer transitioning into Data Analytics Engineering. 
This repository contains my practical projects and daily exercises as I master Python and relational databases.

## Featured Projects 

### 1. [Server Log Parser (Python)](./txt_parser)
A Python script built to automate the analysis of raw server logs. It filters out informational events, extracts critical errors (e.g., application crashes, failed payments), and outputs a structured summary. 

**Skills used in this project:** File handling, control flow (if/else, loops), exception handling (try/except), and data extraction using tuples and lists.

### 2. [E-commerce Database Analysis (SQL)](./sql_marketplace)
A relational database schema designed for an online marketplace platform prototype (similar to Vinted). Includes DDL scripts for table creation (`users`, `items`), mock data insertion, and analytical SQL queries.

####  Database Schema & Relationships:

**1. `users` (Users / Sellers / Buyers)**
| Column | Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `user_id` | SERIAL | **PK** | Unique user identifier |
| `username` | VARCHAR(50) | NOT NULL | User profile handle |
| `country` | VARCHAR(30) | NOT NULL | User location (e.g., Lithuania) |
| `created_at` | DATE | NOT NULL | Registration date |

**2. `categories` (Product Categories Catalog)**
| Column | Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `category_id` | SERIAL | **PK** | Unique category identifier |
| `category_name` | VARCHAR(50) | **UNIQUE**, NOT NULL | Category name (e.g., Clothing, Shoes) |

**3. `items` (Marketplace Listings)**
| Column | Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `item_id` | SERIAL | **PK** | Unique item identifier |
| `seller_id` | INT | **FK** $\rightarrow$ `users(user_id)` | User who listed the item |
| `title` | VARCHAR(100) | NOT NULL | Item title / description |
| `category_id` | INT | **FK** $\rightarrow$ `categories(category_id)` | Item category reference |
| `price` | NUMERIC(10, 2) | NOT NULL | Item price |
| `status` | VARCHAR(20) | **CHECK** (`active`, `sold`, `reserved`) | Current item state |

**4. `orders` (Transactions & Purchases)**
| Column | Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `order_id` | SERIAL | **PK** | Unique transaction identifier |
| `item_id` | INT | **FK**, **UNIQUE** $\rightarrow$ `items(item_id)` | Sold item (1-to-1 relation) |
| `buyer_id` | INT | **FK** $\rightarrow$ `users(user_id)` | User who purchased the item |
| `order_date` | DATE | NOT NULL | Date of purchase |
| `shipping_fee` | NUMERIC(5, 2) | NOT NULL | Delivery cost |

---

* **`users`** $\rightarrow$ **`items`** (One-to-Many): A single user/seller can list multiple items. Linked via `seller_id = user_id`.
* **`categories`** $\rightarrow$ **`items`** (One-to-Many): Each category contains multiple items. Linked via `category_id`.
* **`items`** $\rightarrow$ **`orders`** (One-to-One): An item can be sold and ordered only once. Linked via `item_id`.
* **`users` (Buyer)** $\rightarrow$ **`orders`** (One-to-Many): A user can purchase multiple items over time. Linked via `buyer_id = user_id`.

**Skills used in this project:** Database design, primary & foreign keys, schema integrity (`CHECK` constraints), multi-table `JOIN`s, aggregations (`GROUP BY`, `SUM`, `AVG`), and structured data modeling.