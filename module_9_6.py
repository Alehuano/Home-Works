# print('abc'[0:1])
# print('abc'[1:2])
# print('abc'[2:3])
# print('abc'[0:2])
# print('abc'[1:3])
# print('abc'[0:3])
def all_variants(text):
    for i in range(len(text)):
        # print ('i=',i)
        for j in range(len(text) - i):
            # print('j=',j)
            yield text[j: j + i + 1]


a = all_variants("abc")
for i in a:
    print(i)
