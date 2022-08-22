import sys
from indent import indent


def main():
	args = sys.argv
	path = args[1]

	if path in ["/", "."]:
		print("err")

	cleaned = ""
	with open(path, "r") as f:
		for line in f:
			cleaned += indent(line)

	with open(path, "w") as f:
		f.write(cleaned)

main()