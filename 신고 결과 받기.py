from collections import defaultdict

def solution(id_list, report, k):
    reports = defaultdict(list) # 구성원별 신고한 사람을 리스트로 저장
    counts = defaultdict(int)
    # print(reports, counts)
    
    for repo in set(report):
        reporter, reported = repo.split(' ')
        reports[reporter].append(reported) # 리스트니까 append
        counts[reported] += 1
    # print(reports)
    # print(counts)
    
    answer = [0] * len(id_list)
    for idx, reporter in enumerate(id_list):
        for reported in reports[reporter]:
            if counts[reported] >= k:
                answer[idx] += 1
    
    return answer
