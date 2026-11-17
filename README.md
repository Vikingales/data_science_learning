# My Python & SQL Learning Journey 

Hi! I'm Aliaksandra, a QA Engineer transitioning into Data Analytics Engineering. 
This repository contains my practical projects and daily exercises as I master Python and relational databases.

## Featured Projects 

### 1. [Server Log Parser (Python)](./txt_parser)
A Python script built to automate the analysis of raw server logs. It filters out informational events, extracts critical errors (e.g., application crashes, failed payments), and outputs a structured summary. 

**Skills used in this project:** File handling, control flow (if/else, loops), exception handling (try/except), and data extraction using tuples and lists.

### 2. [E-commerce Database Analysis (SQL)](./sql_marketplace)
A relational database schema designed for an online marketplace platform prototype (similar to Vinted). Includes DDL scripts for table creation (users, items), mock data insertion, and analytical SQL queries.

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
│     title               │   (1-to-1)           |     order_date          |          
|     price               |                      |     shipping_fee        |
|     status              |                      └─────────────────────────┘
└─────────────────────────┘                      
```

* **users** $\rightarrow$ **items** (One-to-Many): A single user/seller can list multiple items. Linked via seller_id = user_id.
* **categories** $\rightarrow$ **items** (One-to-Many): Each category contains multiple items. Linked via category_id.
* **items** $\rightarrow$ **orders** (One-to-One): An item can be sold and ordered only once. Linked via item_id.
* **users** $\rightarrow$ **orders** (One-to-Many): A user can purchase and sell multiple items over time. Linked via buyer_id = user_id.

**Skills used in this project:** Database design, primary & foreign keys, schema integrity (CHECK constraint), multi-table JOINs, aggregations (GROUP BY, SUM, AVG), and structured data modeling.