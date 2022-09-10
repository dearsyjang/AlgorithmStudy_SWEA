T = int(input())
for tc in range(1,T+1):
    N = int(input())

    bus_stop = [0] * 5001 # 1 <= 버스 정류장 <= 5000

    for i in range(1, N+1):
        # i번째 버스 노선은 A 이상 B 이하 다니는 버스 노선
        A, B = map(int, input().split())
        # 버스 정류장 지나는 횟수 count
        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input()) # 버스 노선
    answer = []
    
    for i in range(1, P+1):
        C = int(input()) # 버스 정류장 번호
        answer.append(bus_stop[C])

    print(f'#{tc}', *answer)
