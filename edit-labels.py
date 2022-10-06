for i in range(228):
    with open(r"C:\\Users\\neela\\Documents\\pseudoLabelGeneratorForYOLO\\yolo-labels\\frame%d.txt" % i, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            fp.write(line[1:])