def indent(line):
	space = 0
	tab = 0
	for s in line:
		if s == " ":
			space += 1
		elif s == "\t":
			tab += 1
		else:
			break

	return space4_to_tab(line, space, tab)


def space4_to_tab(line, sc, tc):
	return "\t"*(tc + sc // 4) + " "*(sc % 4) + line[sc + tc:]