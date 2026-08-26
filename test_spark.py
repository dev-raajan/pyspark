import os

python_path = os.path.abspath(".venv/Scripts/python.exe")

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PySparkLearning")
    .master("local[*]")
    .getOrCreate()
)

print("Spark version:", spark.version)

data = [
    ("Rajan", 25),
    ("Amit", 26),
    ("Rahul", 24)
]

df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()