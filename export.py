import os
import pandas as pd
from extractor import extract

folder = "datasets"
data = []

for file in os.listdir(folder):
    if file.endswith(".py") or file.endswith(".js"):
        filepath = os.path.join(folder, file)
        metrics = extract(filepath)
        data.append(metrics)
        
df = pd.DataFrame(data)

df.to_csv("code_metrics.csv", index=False)

print("Dataset saved to code_metrics.csv")
print(df.head())