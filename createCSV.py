import csv

def generate_entries():
    entries = []

    # Create the first 15 entries with "0" as the parent
    for i in range(1, 16):
        entries.append({"id": i, "name": f"Node{i}", "parent": 0})

    # Create 3 entries for each of the first 15 entries
    current_id = 16
    for i in range(1, 16):
        for j in range(3):
            entries.append({"id": current_id, "name": f"Node{current_id}", "parent": i})
            current_id += 1

    # Create 3 entries for each of the previous level (entries from id 16 to 60)
    first_layer_end = current_id
    for i in range(16, first_layer_end):
        for j in range(3):
            entries.append({"id": current_id, "name": f"Node{current_id}", "parent": i})
            current_id += 1

    # Create 3 entries for each of the second layer (entries from previous first_layer_end to current end)
    second_layer_end = current_id
    for i in range(first_layer_end, second_layer_end):
        for j in range(3):
            entries.append({"id": current_id, "name": f"Node{current_id}", "parent": i})
            current_id += 1
    # Create 3 entries for each of the third layer (entries from previous second_layer_end to current end)
    third_layer_end = current_id
    for i in range(second_layer_end, third_layer_end):
        for j in range(3):
            entries.append({"id": current_id, "name": f"Node{current_id}", "parent": i})
            current_id += 1

    return entries

def write_to_csv(entries, filename="output.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "parent"])
        writer.writeheader()
        writer.writerows(entries)

if __name__ == "__main__":
    entries = generate_entries()
    write_to_csv(entries)
    print(f"CSV file with {len(entries)} entries generated successfully.")