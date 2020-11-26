def read_file(fname):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
        print(data)


if __name__ == "__main__":
    read_file("life.html")
