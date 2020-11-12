from collections import defaultdict

seen = defaultdict(int)
year = ['2002', '2002', '2001', '2004', '2005']

for i in year:
    seen[i] += 1

for i,j in seen.items():
    print('In {} year and it is {}%'.format(i, int(j/len(year)*100)))

    