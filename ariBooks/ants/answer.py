'''
長さLcmの竿の上をn匹のありが毎秒1cmのスピードで歩いています。
ありが竿の端に到達すると、竿の下に落ちていきます。
また、竿の上は狭くてすれ違えないので、二匹のありが出会うと、それぞれ反対の方向を向いて戻っていきます。
各ありについて、現在の竿の左端から距離xはわかりますが、どちらの方向を向いているかはわかりません。
全てのありが竿から落ちるまでにかかる最小の時間と最大の時間をそれぞれ求めなさい。

入力
L = 10
n = 3
x = (2, 6, 7)

出力
min: 4
max: 8



★発想
ありの区別をなくすと、二匹のありが出会った時、
逆方向へ行くものを、そのまますれ違って進んで行ったと思ってしまっても何も問題がないことに気付く。
＝＞全てのありは独立に動けるようになるので、あとはありのスタート位置と落ちるまでの距離を探索するだけ
'''

L = int(input())
n = int(input())
x = list(map(int, input().split()))

min_step, max_step = 0, 0

max_step = max((L - x[0]), x[len(x)-1])

# min_step = min(x[0], (L-x[len(x)-1]))
for elem in x:
    temp_min_step = min(elem, L-elem)
    min_step = max(min_step, temp_min_step)

print("max: {}".format(max_step))
print("min: {}".format(min_step))
