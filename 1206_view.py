T = 10
for tc in range(1, T+1):
    N = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 건물의 높이
    view = 0 # 조망권

    for i in range(2, N-2):
        # 왼쪽, 오른쪽 각각 건물 2개보다 크면, 조망권 확보!
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            # 양 옆 건물들 중 최대값
            max_floor = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            # 조망권 계산
            view += arr[i] - max_floor

    print(f'#{tc} {view}')
