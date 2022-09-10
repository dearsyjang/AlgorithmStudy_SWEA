T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split()) # 상자 N개, Q줄
    box = [0] * (N+1)

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i # box 숫자 바꿔주기
    box = box[1:len(box)+1]

    print(f'#{tc}', *box)


