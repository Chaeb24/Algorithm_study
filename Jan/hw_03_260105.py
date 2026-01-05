N, M = map(int,input().split()) # N은 사람, M은 파티

truth = list(map(int,input().split()))
truth.pop(0) #번호만 남도록

parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])  # 앞 숫자(참가자 수) 제거


#진실을 아는 사람이 있는가
changed = True
while changed:
    changed = False
    for party in parties: #첫번째 파티부터
        has_truth = False # 진실 아는지 여부
        for person in party: # 파티 속 사람들 중
            if person in truth:
                has_truth = True
                break

        if has_truth: #연쇄 작용
            for person in party:
                if person not in truth:
                    truth.append(person)
                    changed = True

# 거짓말 가능한 파티 수
count = 0
for party in parties:
    can_lie = True
    for person in party:
        if person in truth:
            can_lie = False
            break
    if can_lie:
        count += 1

print(count)