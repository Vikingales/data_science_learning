# My Python & SQL Learning Journey 

Hi! I'm Aliaksandra, a QA Engineer transitioning into Data Analytics Engineering. 
This repository contains my practical projects and daily exercises as I master Python and relational databases.

## Featured Projects 

### 1. [Server Log Parser (Python)](./txt_parser)
A beginner Python project that reads a server log file and extracts error entries. It identifies lines containing `ERROR`, collects the date and platform information, and displays the errors along with their total count. The script also handles cases where the input file cannot be found. 

#### Project Files:
- `log_parser.py` - Script for parsing txt file.
- `server_logs.txt` - File simulating a server log.

**Skills used in this project:** File handling, reading text files, loops, conditional statements (if/else), exception handling (try/except), string methods (split), lists, tuples, f-strings.

### 2. [E-commerce Database Analysis (SQL)](./sql_marketplace)
A relational database schema designed for an online marketplace platform prototype (similar to Vinted). Includes SQL scripts for creating a relational database with four tables (users, items, categories, orders), inserting sample data and performing basic analytical queries.

#### Project Files:
- `1_create_schema.sql` - Database tables, constraints, and sample data.
- `2_queries.sql` - Basic analytical SQL queries.

#### Database Schema & Relationships:

```text
┌─────────────────────────┐                     ┌─────────────────────────┐
│       categories        │                     │          users          │
├─────────────────────────┤          __________ ├─────────────────────────┤
│ PK  category_id         │         |(1-to-many)│ PK  user_id             │
│     category_name       │         |           │     username            │
└────────────┬────────────┘         |           |     country             |
             |                      |           |     created_at          |
             |                      |           └──────┬──────────────────┘
             │                      |                  │           
             │ (1-to-many)          |                  │  (1-to-many)         
             ▼                      |                  ▼           
┌─────────────────────────┐         |            ┌─────────────────────────┐
│          items          │         |            │         orders          │
├─────────────────────────┤         |            ├─────────────────────────┤
│ PK  item_id             │ ◄───────             │ PK  order_id            │
│ FK  category_id         │                      │ FK  buyer_id            │
│ FK  seller_id           │ ──────────────────►  │ FK  item_id             │
│     title               │   (1-to-0..1)        |     order_date          |          
|     price               |                      |     shipping_fee        |
|     status              |                      └─────────────────────────┘
└─────────────────────────┘                      
```

- **users → items (One-to-Many):** A user can list multiple items for sale. Linked via seller_id = user_id.
- **categories → items (One-to-Many):** A category can contain multiple items. Linked via category_id.
- **items → orders (One-to-Zero-or-One):** Each order is linked to exactly one item, and an item can appear in a maximum of one order. Linked via item_id.
- **users → orders (One-to-Many):** A user can purchase multiple items over time. Linked via buyer_id = user_id.

**Skills used in this project:** Database design, primary and foreign keys, data integrity constraints (CHECK, UNIQUE), INNER JOIN, multi-table JOINs, GROUP BY, aggregate functions (COUNT, SUM, AVG), filtering (WHERE), sorting (ORDER BY), result limitation (LIMIT), rounding (ROUND).

#### Tools I used:
- Visual Studio Code (VS Code)
- Git & GitHub
- MySQL
- Python