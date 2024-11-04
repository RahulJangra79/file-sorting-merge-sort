def merge_sort(lines):
    if len(lines) > 1:
        mid = len(lines) // 2  # Finding the mid of the array
        left_half = lines[:mid]  # Dividing the elements into 2 halves
        right_half = lines[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lines[k] = left_half[i]
                i += 1
            else:
                lines[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            lines[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lines[k] = right_half[j]
            j += 1
            k += 1

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines
    return [line.strip() for line in lines]  # Strip newline characters

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')  # Write each line followed by a newline

def main(input_file, output_file):
    # Step 1: Read lines from the input file
    lines = read_file(input_file)
    
    # Step 2: Sort the lines using merge sort
    merge_sort(lines)
    
    # Step 3: Write the sorted lines to the output file
    write_file(output_file, lines)
    
    # Step 4: Print the content of the output file in the console
    print("Sorted lines in the output file:")
    with open(output_file, 'r') as file:
        print(file.read())

input_file = 'Input_file_merge_sort.txt'
output_file = 'Output_file_merge_sort.txt'
main(input_file, output_file)
