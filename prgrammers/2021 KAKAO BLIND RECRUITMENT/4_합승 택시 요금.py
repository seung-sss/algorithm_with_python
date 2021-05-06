def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)

    # 2차원 리스트에 모든 값 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에게 가는 비용 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 각 간선 정보 graph에 넣기
    for val in fares:
        graph[val[0]][val[1]] = val[2]
        graph[val[1]][val[0]] = val[2]

    # 플로이드워셜 실행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 초기 최소값은 s에서 바로 a, b로 가는 비용 더한 것으로 설정
    answer = graph[s][a] + graph[s][b]

    # s에서 특정 지점 가는 비용 + 특정 지점에서 a, b로 가는 비용 더한 값과 비교
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer

# 다익스트라 풀이
# from collections import defaultdict
# import heapq

# def solution(n, s, a, b, fares):
#     dic = defaultdict(list)
#     for st, ed, co in fares:
#         dic[st].append((co, ed))
#         dic[ed].append((co, st))
#         ans = []
#         for i in range(1, n + 1):
#             q = [(0, i)]
#             visited = [True] * (n + 1)
#             dp = [float('inf')] * (n + 1)
#             dp[i] = 0

#             while q:
#                 co, des = heapq.heappop(q)
#                 if visited[des]:
#                     visited[des] = False

#                     for cost, destination in dic[des]:
#                         dp[destination] = min(dp[destination], dp[des] + cost)
#                         heapq.heappush(q, (dp[destination], destination))

#             ans.append(dp[s] + dp[a] + dp[b])

#     return min(ans)

n_1 = 6
s_1 = 4
a_1 = 6
b_1 = 2
fares_1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# 정답 : 82

n_2 = 7
s_2 = 3
a_2 = 4
b_2 = 1
fares_2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# 정답 : 14

n_3 = 6
s_3 = 4
a_3 = 5
b_3 = 6
fares_3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# 정답 : 18