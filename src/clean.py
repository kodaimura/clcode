def clean(fobj, ext):
	content, count = "", 0
	
	if ext == ".clj":
		content, count = clean_clj(fobj)
	elif ext == ".html":
		content, count = clean_html(fobj)
	else:
		content, count = clean_general(fobj) 

	return content, count


def clean_clj(fobj):
	return clean_lines(fobj, tab_to_space2)

def clean_html(fobj):
	return clean_lines(fobj, tab_to_space2)

def clean_general(fobj):
	return clean_lines(fobj, space4_to_tab)


def clean_lines(fobj, func_clean_line):
	content, count = "", 0
	for line in fobj:
		new_line = func_clean_line(line)
		content += new_line

		if line != new_line:
			count += 1

	return content, count


def space4_to_tab(line):
	sc, tc = count_space_tab(line)
	return "\t"*(tc + sc // 4) + " "*(sc % 4) + line[sc + tc:]

def tab_to_space2(line):
	sc, tc = count_space_tab(line)
	return "  "*tc + " "*sc + line[sc + tc:]


def count_space_tab(line):
	space, tab = 0, 0
	for s in line:
		if s == " ":
			space += 1
		elif s == "\t":
			tab += 1
		else:
			break

	return space, tab