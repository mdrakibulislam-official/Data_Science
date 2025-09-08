# Original file
old_file = Path(file_path)

# New file with changed extension
new_file = old_file.with_suffix(".csv")

# Rename (this changes the file name)
old_file.rename(new_file)

print(f"File renamed to: {new_file}")
