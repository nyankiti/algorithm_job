from sys import stdin


class CardStack:
    def __init__(self, val) -> None:
        # 現在見えている値
        self.val = val
        # その下にある値
        self.cards = [val]


def bisect_right(a, x, lo=0, hi=None, *, key=None):

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if x < key(a[mid]):
                hi = mid
            else:
                lo = mid + 1
    return lo


def main():
    N, K = map(int, stdin.readline().split())
    *P, = map(int, stdin.readline().split())

    result = [-1]*N
    # 現在場に見えているカード(重ねられた下のカードは見えていない)
    shown_cards = []

    # 山札をめくっていく
    for i, p in enumerate(P):
        p_stack = CardStack(p)
        p_idx = bisect_right(
            shown_cards, p_stack.val, key=lambda x: x.val)
        # 大きい数字がない場合
        if p_idx == len(shown_cards):
            shown_cards.append(p_stack)
        else:
            # 大きい数字がある場合
            shown_cards[p_idx].cards.append(p)
            shown_cards[p_idx].val = p

        if len(shown_cards[p_idx].cards) == K:
            for j in shown_cards[p_idx].cards:
                result[j-1] = i+1
            shown_cards.pop(p_idx)

    for ans in result:
        print(ans)


if __name__ == '__main__':
    main()
