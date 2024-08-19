# Traffic Light Data Analyzer

This Python script processes and analyzes traffic light data.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Data Format](#data-format)
- [Tasks Description](#tasks-description)

## Features

0. Complete tasks 1-5.
1. Find the number of red, yellow & green occurrences.
2. Find how long each colour was active for.
3. Find all times when Green was active (by time).
4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.

*Note: Overlapping cycles may be counted separately. In the code you can find another function to count them differently. Please see the comment in [task.py](./task.py) file, line 99.*

5. Find number of lines with mistakes (multiple colours active at the same time or no colours active).
6. Exit the program.

## Usage

1. Make sure that your data file is properly formatted as described in the [Data Format](#data-format) section.
2. Execute the script using Python:

```sh
python .\task.py
```
3. Choose the data file path when prompted (either use the default or provide a custom path).
4. Select the task number from the list of available options.

## Data Format

The input data file should be a CSV file with the following structure:

```sh
Red,Yellow,Green,TimeActive,Time
1,0,0,7,0:00:07
0,1,0,7,0:00:14
0,0,1,9,0:00:23
0,1,0,1,0:00:24
1,0,0,1,0:00:25
```
