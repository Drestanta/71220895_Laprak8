def compare_files(file1, file2):
    with open(file_1) as file1, open(file_2) as file2:
        for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1 != line2:
                print(f"Difference at line {i}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
                print()

file_1 = 'mbox-short.txt'
file_2 = 'mbox.txt'

compare_files(file_1, file_2)