# Cross-Border Freight Analysis Dashboard

## Project Files
- [Dashboard (.pbix)](https://drive.google.com/drive/folders/1qjOiJw4o9lkRaSCbwxcGu4peaTrW1_WB?usp=sharing)
- [Datasets](https://drive.google.com/drive/folders/14re3G-zED98MUEl2u0LFU6BGOHBpU-rp?usp=sharing)

## 📦 Project Overview

This project explores patterns in freight transportation across the U.S., Mexico, and Canada by analyzing publicly available DOT (Department of Transportation) datasets. The goal is to uncover insights into trade volumes, transportation modes, commodity trends, and regional inefficiencies to support data-driven logistics and policy decisions.

The final dashboard was created using **Power BI**, with data preparation carried out in **Excel** and **Python**.

---

## 🛠️ Tools & Technologies

- **Excel** – Initial data cleaning and consolidation  
- **Python (Pandas)** – Dataset merging and transformation  
- **Power BI** – Data modeling, visual analytics, and dashboard design

---

## 📈 Business Questions Addressed

1. **How much in terms of volume and value is being transported?**
2. **What are the top modes of freight transportation by volume and value across borders?**
3. **How do freight volumes and values vary by state?**
4. **Which states or regions experience the highest transportation inefficiencies (e.g., low freight value per weight)?**
5. **What commodities contribute most to emissions-heavy transport (e.g., high freight weight via truck or air)?**
6. **Are there seasonal trends in freight movement that can inform resource allocation?**
7. **What is the relationship between trade partners and transport modes?**

---

## 📂 Dataset Descriptions

### 1. `DOT1` — **Geography-Focused Dataset**
Focus:
- Trade volume/value segmented by U.S. states (`USASTATE`), Mexican states (`MEXSTATE`), and Canadian provinces (`CANPROV`)
- Time-based trends (`MONTH`, `YEAR`)
- Mode of transport (`DISAGMOT`)

Use Cases:
- Regional freight performance
- Monthly or annual transportation patterns

---

### 2. `DOT2` — **Commodity + Geography-Focused Dataset**
Focus:
- Trade value by `COMMODITY2` across U.S. states
- Commodity flow to/from Mexico and Canada
- Transport mode breakdown per commodity

Use Cases:
- Identify high-volume or high-value commodities
- Assess emissions impact by commodity and mode

---

### 3. `DOT3` — **National Overview Dataset**
Focus:
- Aggregate trade stats across countries
- Top commodities and partners by `COUNTRY`
- Mode-of-transport trends over time (`DISAGMOT`)

Use Cases:
- Strategic overview of international trade
- Mode share analysis by partner country

---

## 🔄 Workflow Summary

1. **Data Cleaning & Consolidation**  
   - Excel used for basic filtering and formatting
2. **Data Transformation**  
   - Python scripts created to merge raw CSV files into three main datasets: `DOT1`, `DOT2`, and `DOT3`
3. **Power BI Import & Modeling**  
   - Loaded the datasets
   - Cleaned column types and created calculated fields (e.g., freight efficiency, average cost per weight)
4. **Dashboard Development**  
   - Designed visuals to answer the business questions
   - Used annotations, filters, reference lines, and bookmarks for storytelling

---

## 📊 Dashboard Features

- **Top transport modes by weight and value**
- **State-by-state and month-by-month freight trends**
- **Commodity movement by emissions-heavy modes**
- **Trade partner transport analysis (e.g., Sankey, stacked bar)**
- **Dynamic filtering by year, mode, commodity, and geography**

---

## 📌 Notes

- All visuals are consistent with a custom design template (16:9 layout, light background, Segoe UI fonts, and a uniform color palette).
- Key insights are supported by visual-level filters and reference lines (e.g., COVID year marked with vertical lines).

---

## 🚀 Future Enhancements

- Incorporate emissions multipliers to quantify environmental impact
- Integrate forecasting for seasonal planning
- Include custom tooltip pages with deeper drilldowns

