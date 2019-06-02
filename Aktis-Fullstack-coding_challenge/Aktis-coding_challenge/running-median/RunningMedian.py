fname = input("Enter file name:")

def running_median(med):
    med.sort()
    if len(med) % 2 != 0:
        div = len(med) // 2
        return float(med[div])
    else:
        div = len(med) // 2
        next_div = div - 1
        mid = (med[div] + med[next_div]) / 2
        return mid
        
f = open(fname)
data = f.read()
total = int(data.split('\n', 1)[0])
 
with open(fname) as fp:  
    line = fp.readline()
    cnt = 1
    median = []
    mid = None
    while line:
        if 1 < cnt <= total+1:
            median.append(int(line.strip()))
            mid = running_median(median)
            file = open("output.txt", "a")
            file.write(str(mid)+'\n')
            file.close
        line = fp.readline()
        cnt += 1