import json
data = []
with open('/Users/heeh/Data/legaladvice/2015-01.txt') as f:
    for line in f:
        data.append(json.loads(line))

print(len(data))        
print(data[0]['selftext'])
