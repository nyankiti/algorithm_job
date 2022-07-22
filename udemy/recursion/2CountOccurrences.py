from sys import stdin


def main():

    def count_occurrences(arr, num, i=0, count=0):
        if i == len(arr):
            return count

        if arr[i] == num:
            count += 1

        return count_occurrences(arr, num, i + 1, count)

    print(count_occurrences([4, 2, 7, 4, 4, 1, 2], 4))


if __name__ == '__main__':
    main()