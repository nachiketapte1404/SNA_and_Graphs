# Step 1: Open the .mtx file
input_file = 'road-usroads.mtx'
output_file = 'edges.csv'

# Step 2: Read the .mtx file and extract edges
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Skip the header lines (starting with '%' or until encountering numerical data)
    for line in f_in:
        if line.startswith('%'):
            continue  # Skip comment lines
        # Step 3: Parse the edge data and write to CSV
        nodes = line.strip().split()  # Split by whitespace
        if len(nodes) == 2:  # Each valid line should have 2 nodes (source, target)
            source, target = nodes
            f_out.write(f"{source},{target}\n")  # Write source,target to CSV