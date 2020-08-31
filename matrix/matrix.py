class Matrix:
    def __init__(self, matrix_string):
        self.ms = [list(map(int, row.split()))
                   for row in matrix_string.split('\n')]

    @property
    def rows(self):
        return self.ms[:]

    @property
    def columns(self):
        return list(map(list, zip(* self.ms)))

    # @property enables method rows and columns to be called like attributes
    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
