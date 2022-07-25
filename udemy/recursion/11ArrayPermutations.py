from sys import stdin
from unittest import result


def main():

    def get_permutations(arr):
        if len(arr) <= 1:
            return [arr]

        result = []
        first = arr[0]

        for perm in get_permutations(arr[1:]):
            for i in range(len(arr)):
                result.append(perm[:i] + [first] + perm[i:])

        return result

    # print(get_permutations([1, 2, 3, 4]))

    def model_answer(arr):
        if len(arr) == 0:
            return [arr]
        else:
            permutations = []
            for i in range(len(arr)):
                if arr[i] not in arr[:i]:
                    remaining = model_answer(arr[:i] + arr[i + 1:])
                    for permutation in remaining:
                        permutation.append(arr[i])
                        permutations.append(permutation)
            return permutations

    print(model_answer([1, 2, 3]))


if __name__ == '__main__':
    main()