import os

MINIO_ENDPOINT = os.getenv("DL_ENDPOINT", "http://minio:9000")
MINIO_ACCESS_KEY = os.getenv("DL_ACCESS_KEY", "admin")
MINIO_SECRET_KEY = os.getenv("DL_SECRET_KEY", "senha123")
BUCKET_NAME = "datalake"

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "gold_db")
DB_USER = os.getenv("DB_USER", "jao")
DB_PASS = os.getenv("DB_PASS", "senha123")
DB_PORT = "5432"

DB_CONNECTION_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"