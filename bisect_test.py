import bisect


def main():
    # 配列を使わない場合
    A = [1, 12, 23, 38, 54, 66, 76, 98]
    # Aの順序を保ったまま'46'を挿入したい
    A.append(46)
    A.sort()
    print(A)

    B = [1, 12, 23, 38, 54, 66, 76, 98]
    index = bisect.bisect_right(B, 46) # bisectのメソッドによって、46を挿入すべき位置を取得する
    B.insert(index, 46)

    # 上の処理は以下のように一つメソッドにまとめられている
    bisect.insort_right(B, 46)

    print(B)

if __name__ == '__main__':
	main()