# Print the score of the runner up among a given number of  participants
if __name__ == '__main__':
    n = int(input())
    arr = list(sorted(set(map(int, input().split())), reverse=True))
    print(arr[1])
