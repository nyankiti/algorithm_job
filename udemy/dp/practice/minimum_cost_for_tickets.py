import math
from sys import stdin


def main():

    # memorization
    def min_cost_for_tickets(train_days, costs, n):

        lookup = {}

        def rec(pos):
            if pos in lookup:
                return lookup[pos]
            if pos >= len(train_days):
                return 0
            current_day = train_days[pos]

            # 1-day passを利用する場合
            one_day_cost = costs[0] + rec(pos + 1)

            # 7-day passを利用する場合
            seven_day_diff = 0
            for day in train_days[pos:]:
                if day - current_day < 7:
                    seven_day_diff += 1
                else:
                    break
            seven_day_cost = costs[1] + rec(pos + seven_day_diff)

            # 30-day passを利用する場合
            thirty_day_diff = 0
            for day in train_days[pos:]:
                if day - current_day < 30:
                    thirty_day_diff += 1
                else:
                    break
            thirty_day_cost = costs[2] + rec(pos + thirty_day_diff)

            lookup[pos] = min(one_day_cost, seven_day_cost, thirty_day_cost)
            return lookup[pos]

        return rec(0)

    # 32日間の旅行のうち、第一引数に示された日のみ電車を使う
    # costs: [1-day pass, 7-days pass, 30-days pass]
    ans = min_cost_for_tickets([1, 3, 8, 9, 22, 23, 28, 31], [4, 10, 25], 32)
    print(ans)

    # tabulation
    def min_cost_for_tickets_tabu(train_days, costs, n):
        # train_daysの i 日目までにおける最も安い値段を格納
        dp = [math.inf] * len(train_days)
        dp[0] = costs[0]

        for i in range(1, len(train_days)):
            current_day = train_days[i]

            one_day_cost = dp[i - 1] + costs[0]

            seven_day_diff = 0
            for j in range(i, -1, -1):
                if current_day - train_days[j] < 7:
                    seven_day_diff += 1
                else:
                    break

            seven_day_cost = costs[1]
            if i - seven_day_diff >= 0:
                seven_day_cost += dp[i - seven_day_diff]

            thirdy_day_diff = 0
            for j in range(i, -1, -1):
                if current_day - train_days[j] < 30:
                    thirdy_day_diff += 1
                else:
                    break
            thirdy_day_cost = costs[2]

            if i - thirdy_day_diff >= 0:
                thirdy_day_cost += dp[i - thirdy_day_diff]

            if i == len(train_days) - 1:
                print(one_day_cost, seven_day_cost, thirdy_day_cost)

            dp[i] = min(one_day_cost, seven_day_cost, thirdy_day_cost)

        print(dp)
        return dp[-1]

    ans = min_cost_for_tickets_tabu([1, 3, 8, 9, 22, 23, 28, 31], [4, 10, 25],
                                    32)
    print(ans)

    # model answer
    def cost(train_days, costs, n):
        lookup = {}

        def rec(day):
            if day in lookup:
                return lookup[day]
            if day >= n:
                return 0
            # 電車に乗らない日はそのまま1日飛ばすだけ！！！
            # (わざわざ7 or 30日間に電車乗る日が何回あるかをカウントする必要はない！！)
            elif day not in train_days:
                lookup[day] = rec(day + 1)
                return lookup[day]
            else:
                lookup[day] = min(costs[0] + rec(day + 1),
                                  costs[1] + rec(day + 7),
                                  costs[2] + rec(day + 30))
                return lookup[day]

        return rec(0)

    ans = cost([1, 3, 8, 9, 22, 23, 28, 31], [4, 10, 25], 32)
    print(ans)

    # model answer tabulation
    def cost_tabulation(travel_days, costs, n):
        # 大きさがnの配列を作ってdpすることで、わざわざ7 or 30日間に電車乗る日が何回あるかをカウントする必要はなくなる
        # dp[i] => i日目までで最も安い値段
        dp = [0] * n
        for i in range(len(dp)):
            # その日に電車に乗らない場合
            if i not in travel_days:
                dp[i] = (dp[i - 1] if i - 1 >= 0 else 0)
            # その日に電車に乗る場合
            else:
                day_cost = costs[0] + (dp[i - 1] if i - 1 >= 0 else 0)
                week_cost = costs[1] + (dp[i - 7] if i - 7 >= 0 else 0)
                month_cost = costs[2] + (dp[i - 30] if i - 30 >= 0 else 0)
                dp[i] = min(day_cost, week_cost, month_cost)
        return dp[n - 1]


if __name__ == '__main__':
    main()