import pandas as pd

file_path = "css_marks.xlsx"

# Load raw file (no header)
df_raw = pd.read_excel(file_path, header=None)

# Find header row (where "Roll" appears)
header_row = None
for i, row in df_raw.iterrows():
    if row.astype(str).str.contains("Roll", case=False).any():
        header_row = i
        break

if header_row is None:
    raise Exception("Header row not found!")

# Reload with correct header
df = pd.read_excel(file_path, header=header_row)

# Clean column names
df.columns = df.columns.str.replace("\n", " ", regex=True)
df.columns = df.columns.str.replace(r"\s+", " ", regex=True).str.strip()

print("Columns:", df.columns.tolist())

# Detect columns
roll_col = [col for col in df.columns if "Roll" in col][0]
marks_col = [col for col in df.columns if "Practical" in col][0]

# Convert marks to numeric
df[marks_col] = pd.to_numeric(df[marks_col], errors='coerce')

# Input
target_marks = int(input("Enter marks: "))

# Filter
filtered = df[df[marks_col] == target_marks]

# Output
roll_numbers = filtered[roll_col].dropna().astype(int).tolist()

print(f"Roll Numbers with {target_marks} marks:")
print(roll_numbers)