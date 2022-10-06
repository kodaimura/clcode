import sys
from clean import indent


def main():
	args = sys.argv
	path = args[1]
	count_cleaned_lines = clean_file(path)
	print_result(path, count_cleaned_lines)


def clean_file(path):
	cleaned = ""
	count_cleaned_lines = 0
	with open(path, "r") as f:
		for line in f:
			new_line = indent(line)
			cleaned += new_line

			if line != new_line:
				count_cleaned_lines += 1

	with open(path, "w") as f:
		f.write(cleaned)

	return count_cleaned_lines


def print_result(path, count_cleaned_lines):
	if count_cleaned_lines != 0:
		print(path + " ✔︎", end="\n")
	else:
		print(path + " -", end="\n")


main()