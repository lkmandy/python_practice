def read_file(fname):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
        print(data)


read_file("ClassMarker_Test_Taking_Guide.pdf")
