from collections import deque
from sys import stdin


def main():
    N, P, Q, R = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    A_ruiaseki = []
    prev = 0
    for a in A:
        A_ruiaseki.append(prev)
        prev += a

    P_candidate = []
    Q_candidate = []
    R_candidate = []
    # key => start index, value => end index
    P_dict = {}
    Q_dict = {}
    R_dict = {}

    # しゃくとり法でP, Q, Rの候補となるindexのpairを探索する

    def shakutori(target, candidate_li, candidate_di):
        temp_sum = 0
        dq = deque()
        for i in range(N):
            temp_sum += A[i]
            dq.append(i)

            if temp_sum == target:
                candidate_li.append((dq[0], dq[-1]+1))
                candidate_di[dq[0]] = dq[-1]+1

            while temp_sum > target:
                poped_idx = dq.popleft()
                temp_sum -= A[poped_idx]

                if temp_sum == target:
                    candidate_li.append((dq[0], dq[-1]+1))
                    candidate_di[dq[0]] = dq[-1]+1

    shakutori(P, P_candidate, P_dict)
    shakutori(Q, Q_candidate, Q_dict)
    shakutori(R, R_candidate, R_dict)
    # print(P_candidate)
    # print(Q_candidate)
    # print(R_candidate)

    # for P_pair in P_candidate:
    #     for Q_pair in Q_candidate:
    #         if P_pair[1] == Q_pair[0]:
    #             for R_pair in R_candidate:
    #                 if Q_pair[1] == R_pair[0]:
    #                     print("Yes")
    #                     return
    # print("No")
    for P_par in P_candidate:
        if P_par[1] in Q_dict:
            if Q_dict[P_par[1]] in R_dict:
                print("Yes")
                return
    print("No")

    # 実際に必要なオブジェクトは、P_candidate, Q_dict, R_dict


if __name__ == '__main__':
    main()
