 # Implement your model here

import os
import pandas as pd

input_dir = "/input/images"
output_dir = "/output"

rows = []
for img in sorted(os.listdir(input_dir)):
    rows.append({"id": img, "mes_score_0_3": 1})

os.makedirs(output_dir, exist_ok=True)
pd.DataFrame(rows).to_csv(
    os.path.join(output_dir, "results.csv"), index=False
)

