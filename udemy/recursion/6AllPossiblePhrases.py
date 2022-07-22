from sys import stdin


def main():

    def phrases(arr):
        result = []

        def _phrases(arr, pos=0, candidate=""):
            if pos == len(arr):
                result.append(candidate)
                return

            for phrase in arr[pos]:
                _phrases(arr, pos + 1, candidate + " " + phrase)

        _phrases(arr)

        return result

    # res = phrases([["I", "You", "They"], ["love", "hate"], ["food", "games"]])
    # for phrase in res:
    #     print(phrase)

    def model_ans(arr):
        output = []

        # recursiveのrec
        def rec(arr, i, phrase):
            if i == len(arr):
                output.append(" ".join(phrase))
            else:
                for word in arr[i]:
                    phrase.append(word)
                    # depth firstになっているので、phraseの中身が正しく書き変わる
                    rec(arr, i + 1, phrase)
                    phrase.pop()

        rec(arr, 0, [])
        return output

    # res = model_ans([["I", "You", "They"], ["love", "hate"], ["food",
    #                                                           "games"]])
    # for phrase in res:
    #     print(phrase)

    def model_ans_vol2(arr, i=0):
        if i == len(arr):
            return [" "]
        else:
            from_next = model_ans_vol2(arr, i + 1)
            output = []
            for word in arr[i]:
                for phrase in from_next:
                    output.append(word + ("" if len(phrase) == 0 else " ") +
                                  phrase)
            return output

    res = model_ans_vol2([["I", "You", "They"], ["love", "hate"],
                          ["food", "games"]])
    for phrase in res:
        print(phrase)


if __name__ == '__main__':
    main()