# You are given three integers  and  representing the dimensions of a cuboid along with an integer.
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to n.
if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
              if i + j + k != n]
    print(result)
