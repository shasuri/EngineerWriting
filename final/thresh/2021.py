t = [39.1,38.2,37.5,38.7,36.2,38.6,38.1,35.3,36.3,39.3,35.5,36.5,36.4]
p = [95,93,87,86,75,72,66,63,58,53,49,44,22]

tp = 0
tn = 0
fp = 0
fn = 0

for i in range(13) : 
    if t[i] >= 38 and p[i] >= 80 :
        tp += 1
    if t[i] < 38 and p[i] < 80 :
        tn += 1

    if t[i] < 38 and p[i] >= 80 :
        fp += 1
    if t[i] >= 38 and p[i] < 80 :
        fn += 1

print(tp)
print(tn)
print(fp)
print(fn)

print(tn/(fp+tn))
print(tp/(tp+fn))

rec = tp/(tp+fn)
pre = tp/(tp+fp)
print(1/(1/rec+1/pre)*2)