
# 🚀 Simple ETL Data Pipeline using Spotify Data
This project demonstrates the simple ETL Data Pipeline for ETL Logic using Spotfiy dataset on CSV to Parquet as backup and CSV to PostgreSQL table for Data Visualization via Metabase

![Spotify Data Pipeline Design](/images/data_pipeline_design.png)

## 💡 Technologies Used
- **Programming Language**: Python 3.10.2

- **Database**: PostgreSQL 17

- **Data Visualization Tool**: Metabase 55.6

- **Data Store**: [Spotify Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

- **Data Orchestration Tool**: Dagster 1.11.1

- **Python Libraries**:
    - **pandas**: For data manipulation and cleaning.
    - **SQLAlchemy**: For database interaction.
    - **numpy**: For numerical computations.
    - **dotenv**: To handle environment variables (API keys, DB credentials).


## 📦 Setup Instructions
  
  
### 1. Clone the Repository
  
```bash
git  clone https://github.com/Mitsuki16/simple_dagster_job_example
cd simple_dagster_job_example
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
.venv/Scripts/activate # On Windows  
# OR  
source .venv/bin/activate # On macOS/Linux`
```

### 3. Install Dependencies Using `pip`

```bash
pip install dagster==1.11.1 pandas
```
### 4. Run the Job

To execute the job via the command prompt:
```bash
dg run -- port 8000
```
You should see logs showing the generated number list and their computed sum.

### 5: Access Dagster Web UI

Navigate to the following link in your browser to view the Dagster Web UI:

[http://localhost:8000/overview](http://localhost:3000/overview)
<br>
<br>

## 🖥️ To View the Metabase Web UI, Run the Metabase 

**Pre-Requisite Software** - Java 21+ and Metabase 55.6 (JAR)

To execute the Metabasem, navigate to folder where metabase is saved and execute the below command in the command prompt:
```bash
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Navigate to the following link in your browser to view the Dagster Web UI:

[http://localhost:3000/](http://localhost:3000/overview)
<br>
<br>


## ⚙️ Dagster Asset Overview

An ETL Pipeline of two tasks on Extracting the data from source CSV file, transforms(Adding uploaded date, removing unwanted columns and filters missing values) and loading the data to destination as parquet file as backup along with loading the transformed CSV data to a PostgreSQL table for Data Visualization

### ✅ Asset 1 – `etl_csv_to_parquet_data`
- **Category**: ETL Logic for Transformation of CSV to Parquet
- **Description**: ETL - Load CSV data, Transform and Load as Parquet file.

### ✅ Asset 2 – `load_postgres_table`
- **Category**: Load Transformed CSV data to PostgreSQL
- **Description**: Load transformed CSV data into PostgreSQL table named spotify_data


---
## 🎉  ETL Data Pipeline Job Executed Status

![Simple Dagster Job Success Image](/images/dagster_simple_etl_job_files_run.png)

----------

## 👩‍💻 Metabase - Spotify Data Analysis

![Simple Dagster Job Success Image](/images/metabase_spotify_analysis.png)

----------
