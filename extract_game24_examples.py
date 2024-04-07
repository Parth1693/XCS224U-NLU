import json

# Open the JSON file and read its contents
with open("puzzles.json", "r") as file:
    json_data = file.read()

# Load JSON data
data = json.loads(json_data)

# Extract "numberTiles" as a list of lists
number_tiles_list = [puzzle["numberTiles"] for puzzle in data["puzzles"]]

print(number_tiles_list)

# Save number_tiles_list to a file
with open("game24_examples.txt", "w") as file:
    for tile_list in number_tiles_list:
        # Convert the list to a string with space-separated values
        line = ",".join(map(str, tile_list))
        # Write the line to the file
        file.write(line + "\n")