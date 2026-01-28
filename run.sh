#!/bin/bash
echo "Running Endo-UC inference..."

python src/inference.py \
  --input_dir /input \
  --output_dir /output

echo "Finished."
