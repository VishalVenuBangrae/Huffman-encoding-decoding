# Huffman Coding Project

This project involves the implementation of Huffman coding and decoding for text compression using Python. The main goal is to efficiently encode and decode text using the least amount of bits possible while maintaining a lossless compression scheme.

## Prerequisites

Ensure you have Python 3 installed on your machine. You will also need the `graphics.py` library if visualizations are required.

## Files

- **TreeNode.py**: Defines the `TreeNode` class used to construct the Huffman tree.
- **Huffman.py**: Contains the logic for creating the Huffman tree and encoding/decoding functions.
- **Driver.py**: The main script that reads text input and executes the Huffman coding process.
- **Driver2.py**: An alternative or supplementary driver script, details depend on its specific implementation.
- **hob.txt**: A sample text file to be compressed.
- **huck_finn.txt**: Another sample text file to be compressed.
- **test_cases.py**: Contains test cases to verify the functionality of the Huffman coding implementation.

## Usage

Run the Driver script with a text file as an argument to encode and decode using Huffman codes:

```bash
python3 Driver.py huck_finn.txt
