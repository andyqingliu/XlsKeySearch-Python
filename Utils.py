cols2skip = [2,5,8]
writeColumns = {}
cols = ["我是谁", "你又是谁", "我哪知道你是谁", "你爱是谁是谁我不管"]
# valueDict = {val : "valueStr", cotainedKeys : []}
print(type(cols))
for strCol in cols:
    print("strCol = {0},长度是{1}".format(strCol, len(strCol)))

def takeSecond(elem):
    return elem[1]

a = 1
if a:
    print("a is not null")
else:
    print("a is null ...")