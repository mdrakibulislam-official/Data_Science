from pathlib import Path

file_path = r"C:\Users\hp\OneDrive\RakibShare\Malay\PSSE_PowerFactory\Permata_CSV"  # Original file

# Original file
file_path = Path(file_path)

# Change extension only (does NOT rename the file)
temp_file = file_path.with_suffix(".csv")

df = pd.read_csv(file_path, delimiter=",",skiprows=2)

print(temp_file)  # Output: data.csv

print(df.columns)
