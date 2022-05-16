def main():
    N = int(input())
    seen = set()  # 既に出た文字列を管理
    max_t = -1  # 0点の提出が最優秀賞になることもあるので注意
    ans = 0  # 暫定の最優秀賞の提出番号
    for i in range(1, N + 1):
        s, _t = input().split()
        t = int(_t)
        if s in seen:  # 既出なので判定しません
            continue
        seen.add(s)  # 最優秀賞でなくても、既出判定には用いられます
        if max_t < t:  # 同点なら早いほうが最優秀賞ですから、不等号は<です
            max_t = t
            ans = i
    print(ans)


if __name__ == '__main__':
    main()
