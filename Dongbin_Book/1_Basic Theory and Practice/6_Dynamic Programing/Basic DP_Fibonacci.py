# DP 사용 가능한 경우
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
# 메모이제이션을 이용한 탑다운 방식 : 한 번 구한 결과를 메모리 공간에 저장해두고 이용하는 것(캐싱)
# 메모이제이션은 때에 따라 dictionary형 이용할 수 있음 (연속적이지 않은 경우 유용)
# 재귀 함수 이용하면 오버헤드 발생 문제 있을 수 있음
# 일반적으로 반복문 이용한 바텀업 방식 DP가 성능이 더 좋음
# 바텀업 방식에 이용되는 결과 저장용 리스트는 'DP 테이블'이라고 부름
# 시험에서 문제 완전 탐색 알고리즘으로 접근했을 때 시간 오래 걸리면 DP 적용 가능한지 확인
# DP 적용 가능 여부는 해결하고자 하는 부분 문제들이 중복되는지를 확인
# 단순 백트래킹 구현 후, 메모이제이션 적용하여 코드 개선하는 방식으로 생각해도 좋음
# recursion depth 관련 오류 발생하면, sys 라이브러리의 setrecursionlimit() 함수 이용하여 재귀 제한 완화 가능
# 가급적 반복문 이용하여 만들자!!

# 백트래킹을 통한 피보나치 수열 구현 (단순 재귀 방식)
def fibo_backtracking(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    return fibo_backtracking(x - 1) + fibo_backtracking(x - 2)


# 메모이제이션 이용한 탑다운 방식 DP
# DP 이용하면 피보나치 수열 시간 복잡도 O(N)
memo_td = [0] * 100

def fibo_topdown(x):
    # 종료 조건(1 or 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제는 그대로 반환
    if memo_td[x] != 0:
        return memo_td[x]

    # 아직 계산하지 않은 문제는 점화식에 따라 결과 반환
    memo_td[x] = fibo_topdown(x - 1) + fibo_topdown(x - 2)
    return memo_td[x]

print(fibo_topdown(99))


# 반복문 이용한 바텀업 방식 DP
## DP 테이블 생성
memo_bu = [0] * 100

# 첫 번째와 두 번째 피보나치 수 지정
memo_bu[1] = 1
memo_bu[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n + 1):
    memo_bu[i] = memo_bu[i - 1] + memo_bu[i - 2]

print(memo_bu[n])