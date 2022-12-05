import sys, os.path
from clean import clean


def main():
	args = sys.argv
	path = args[1]
	count_cleaned_lines = clean_file(path)
	print_result(path, count_cleaned_lines)


def clean_file(path):
	cleaned = ""
	count_cleaned_lines = 0
	with open(path, "r") as f:
		cleaned, cleaned_lines = clean(f, get_file_extension(path))

	with open(path, "w") as f:
		f.write(cleaned)

	return cleaned_lines


def print_result(path, count_cleaned_lines):
	if count_cleaned_lines != 0:
		print(path + " ✔︎", end="\n")
	else:
		print(path + " -", end="\n")


def get_file_extension(path):
	_, ext = os.path.splitext(path)
	return ext


main()