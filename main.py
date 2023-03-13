# Open the input files for reading
with open("old_file.txt", encoding="utf-8",errors="ignore") as f1, open("new_file.txt", encoding="utf-8",errors="ignore") as f2:
    # Read the contents of the files
    old_file = f1.read()
    new_file = f2.read()

# Split the contents of the files into blocks
old_blocks = [block.strip() for block in old_file.split("\n\n") if block.strip()]
new_blocks = [block.strip() for block in new_file.split("\n\n") if block.strip()]

# Check if any blocks are missing from the new file
missing_blocks = set(old_blocks) - set(new_blocks)
if missing_blocks:
    print(f"The following blocks are missing from the new file: {', '.join(missing_blocks)}")

# Sort the blocks in the new file according to the order in the old file
sorted_blocks = []
for block in old_blocks:
    for new_block in new_blocks:
        header = new_block.split("\n")[0].strip()
        if block.split("\n")[0].strip() == header:
            sorted_blocks.append(new_block)
            new_blocks.remove(new_block)
            break
    else:
        sorted_blocks.append(block)

# Add any remaining blocks from the new file to the end of the sorted list
sorted_blocks += new_blocks

# Write the sorted output file
with open("sorted_file.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(sorted_blocks))