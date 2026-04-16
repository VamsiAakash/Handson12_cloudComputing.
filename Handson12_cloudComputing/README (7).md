Student Details: 
Name: Vamsi Aakash Samudrala
Student id: 801425922

# Hands-on-12-Spark-on-AWS
# Serverless Spark ETL Pipeline on AWS

This project is a hands-on assignment demonstrating a fully automated, event-driven serverless data pipeline on AWS.

The pipeline automatically ingests raw CSV product review data, processes it using a Spark ETL job, runs analytical SQL queries on the data, and saves the aggregated results back to S3.

---

##  Project Overview

The core problem this project solves is the need for manual data processing. In a typical scenario, data lands in S3 and waits for a data engineer to run a job. This project automates that entire workflow.

**The process is as follows:**
1. A raw `reviews_cleaned.csv` file is uploaded to an S3 "landing" bucket.
2. The S3 upload event instantly triggers an **AWS Lambda** function.
3. The Lambda function starts an **AWS Glue ETL job**.
4. The Glue job (running a PySpark script) reads the CSV, cleans it, and runs multiple Spark SQL queries to generate analytics (e.g., average ratings, top customers).
5. The final, aggregated results are written as CSV files to a separate S3 "processed" bucket.

---

## Architecture

**Data Flow:**
`S3 (Upload) -> Lambda (Trigger) -> AWS Glue (Spark Job) -> S3 (Processed Results)`

---

## 🛠️ Technology Stack

* **Data Lake:** Amazon S3
* **ETL (Spark):** AWS Glue
* **Serverless Compute:** AWS Lambda
* **Data Scripting:** PySpark (Python + Spark SQL)
* **Security:** AWS IAM (Identity and Access Management)

---

## 🔧 Setup and Deployment

### 1. Create S3 Buckets

Create two S3 buckets:
* `handsonfinallandingggg` — raw data landing zone
* `handsonfinalprocessedddd` — processed results destination

**Screenshot: S3 Buckets Created**


<img width="1710" height="1107" alt="Output1" src="https://github.com/user-attachments/assets/d377f238-9bca-44fa-a7bc-ee31d4ad5305" />



---

### 2. Upload Raw Data to Landing Bucket

Upload the `reviews_cleaned.csv` file to the `handsonfinallandingggg` bucket.

**Screenshot: CSV file uploaded to landing bucket**

<img width="1710" height="1107" alt="output2" src="https://github.com/user-attachments/assets/f1f1aea2-6822-40ee-9065-a62dad139f1c" />


---

### 3. Create IAM Role for AWS Glue

1. Go to **IAM** → **Roles** → **Create Role**
2. Select **AWS service** → **Glue**
3. Attach `AWSGlueServiceRole` and `AmazonS3FullAccess` policies
4. Name the role `AWSGlueServiceRole-Reviews`

**Screenshot: IAM Role for Lambda**

<img width="1710" height="1107" alt="output3" src="https://github.com/user-attachments/assets/a1246737-2bd5-4e0f-9f24-a8d0c59143df" />




---

### 4. Create the AWS Glue ETL Job

1. Go to **AWS Glue** → **ETL Jobs**
2. Select **Spark script editor**
3. Paste the contents of `glue etl script.py`
4. Set job name to `process_reviews_job`
5. Attach the IAM role
6. Save and Run the job

**Screenshot: Glue Job Succeeded**

<img width="1710" height="1107" alt="output33" src="https://github.com/user-attachments/assets/159f59a7-eb13-4daa-a14c-8a66c4765626" />



### 5. Create the Lambda Trigger Function

1. Go to **AWS Lambda** → **Create function**
2. Select **Author from scratch**
3. Function name: `start_glue_job_trigger`
4. Runtime: **Python 3.12**
5. Create the function and paste the Lambda code

**Screenshot: Lambda Function Code**

<img width="1710" height="1107" alt="lambda" src="https://github.com/user-attachments/assets/91f8969f-72db-48ab-b511-2d5945f6e7f4" />

<img width="1710" height="1107" alt="output4" src="https://github.com/user-attachments/assets/1201d993-9705-47cb-8190-7a6300972875" />

---

### 6. Verify Processed Output in S3

After the Glue job succeeds, navigate to the `handsonfinalprocessedddd` bucket to verify output folders.

**Screenshot: Processed Bucket with Output Folders**

<img width="1710" height="1107" alt="output5" src="https://github.com/user-attachments/assets/466752b1-098e-4c4d-ac75-2dda290d16d2" />


**Screenshot: Athena Results Folder Contents**

<img width="1710" height="1107" alt="output6" src="https://github.com/user-attachments/assets/1d702cb4-13df-4077-8131-0c6639dd7bdc" />


**Screenshot: Processed Data Folder**

  <img width="1710" height="1107" alt="output7" src="https://github.com/user-attachments/assets/ade15b05-11bc-479f-ba9a-1c68d5bffb82" />


---

##  How to Run the Pipeline

Your pipeline is now fully deployed and automated!

1. Upload `reviews_cleaned.csv` to the `handsonfinallandingggg` S3 bucket
2. This triggers the Lambda function, which starts the Glue job
3. Monitor progress in **AWS Glue → Monitoring tab**
4. After 2-3 minutes, results appear in `handsonfinalprocessedddd`

---

## Query Results

After the job completes, navigate to `handsonfinalprocessedddd`. Results are in the `Athena Results/` folder:

* `s3://handsonfinalprocessedddd/Athena Results/daily_review_counts/`
* `s3://handsonfinalprocessedddd/Athena Results/top_5_customers/`
* `s3://handsonfinalprocessedddd/Athena Results/rating_distribution/`
* `s3://handsonfinalprocessedddd/processed-data/` — complete cleaned dataset

---

##  Cleanup

To avoid future charges, delete the following resources:
1. Empty and delete `handsonfinallandingggg` and `handsonfinalprocessedddd` S3 buckets
2. Delete the `start_glue_job_trigger` Lambda function
3. Delete the `process_reviews_job` Glue job
4. Delete the `AWSGlueServiceRole-Reviews` IAM role
