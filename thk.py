# Đọc dữ liệu từ file QUEUE.INP
with open("QUEUE.INP", "r") as f:
    lines = f.readlines()

T = int(lines[0].strip())  # Số lượng test case
results = []

for i in range(1, 2*T+1, 2):
    M, N = map(int, lines[i].strip().split())
    max_served = 0
    
    # Duyệt qua các xe khách trong queue
    for j in range(i+1, i+1+N):
        a, b = map(int, lines[j].strip().split())
        
        # Tìm số lượng xe khách lớn nhất có thể phục vụ
        served = 0
        for x in range(a, b+1):
            if all(x not in range(a_, b_+1) for a_, b_ in [(a, b) for a, b in map(int, lines[k].strip().split()) for k in range(i+1, i+1+N) if k != j]): # type: ignore
                served += 1
        
        max_served = max(max_served, served)
    
    results.append(max_served)

# Ghi kết quả vào file QUEUE.OUT
with open("QUEUE.OUT", "w") as f:
    for result in results:
        f.write(str(result) + "\n")