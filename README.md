# Merge Sort File Sorter

This project implements a file sorting utility using the merge sort algorithm. It reads lines from an input text file, 
sorts them, and writes the sorted lines to an output text file. The sorted content is also printed to the console.

## Features

- Reads lines from a specified input file.
- Sorts the lines using the merge sort algorithm.
- Writes the sorted lines to an output file.
- Displays the sorted content in the console.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/merge-sort-file-sorter.git
   cd merge-sort-file-sorter
   ```

2. **Prepare your input file**: Create a text file named `Input_file_merge_sort.txt` in the project directory, and add the lines you want to sort.

3. **Run the script**:
   ```bash
   python merge_sort_file_sorter.py
   ```

4. **Check the output**: After running the script, you will find the sorted lines in `Output_file_merge_sort.txt`, and the sorted content will be printed in the console.

## Functions

- `merge_sort(lines)`: Sorts a list of lines using the merge sort algorithm.
- `read_file(file_path)`: Reads lines from a file and returns a list of stripped lines.
- `write_file(file_path, lines)`: Writes the sorted lines to an output file.
- `main(input_file, output_file)`: The main function that orchestrates reading, sorting, and writing.

## Example

Given an `Input_file_merge_sort.txt` with the following content:
```
banana
apple
orange
grape
```

After running the script, the `Output_file_merge_sort.txt` will contain:
```
apple
banana
grape
orange
```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. 

## Acknowledgements

- Inspired by standard sorting algorithms and their applications in file handling.
