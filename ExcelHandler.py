import pandas as pd
import os.path

class ExcelProcess(object):
    def __init__(self):
        super(ExcelProcess,self).__init__()
        self.filePath = None
        self.contentSheet = None
        self.keySheet = None
        self.keyValues = {}
        self.keyStrs = []
        self.multiKeyValues = {}
    
    def ReadExcel(self, fPath):
        if(len(fPath) > 0):
            # 只读取表的sheet1和sheet2,因为sheet1记录的是内容，sheet2记录的是key value关键字列表
            # skiprows = 1 忽略前1行，从第二行开始读取内容
            # hearder = 0 指定第一行作为列名(因为已经忽略了第一行，其实是将第二行作为列名)
            # usecols= "A:F" 读取从A列到F列的内容(可能随着需要开放出来通过配置来决定读取到第几列)，也可以写成列表[0,1,2,3,4,5]
            # usecols=lambda x: "Unnamed" not in x,也可以写成lambda,略过没有列名的的列,或者lambda x: x.find("Unnamed") < 0
            # na_values指定NaN的替代字符
            #keep_default_na 与na_values配合使用，设置为False的时候才会用替代字符替换NaN
            #这里本来想只读取前6列中列名不等于Unnamed的列。发现实现不了！！！要么只能是前6列，要么只能是不等于Unnamed的所有列
            cols = list(range(6))
            data = pd.read_excel(io=fPath, sheet_name=[0,1], header=0, skiprows=1, usecols=cols, na_values="", keep_default_na=False)
            self.filePath = fPath
            self.contentSheet = data[0]
            self.keySheet = data[1]

    def ShowContentSheet(self):
        print("测试测试")
        # for index, row in self.contentSheet.iterrows():
        #     if(index <= 5):
        #         print("行内容：", row)
        #     else:
        #         return

    def InitKeyValueData(self):
        for index, row in self.keySheet.iterrows():
            keyStr = row[0]
            valueStr = row[1]
            if(not keyStr in self.keyValues):
                valueDict = {"val" : valueStr, "cotainedKeys" : []}
                self.keyValues[str(keyStr)] = valueDict
                self.keyStrs.append(str(keyStr))
            else:
                # 由于从第二行开始才是文本内容，并且index从0开始，所以实际的行数要+3
                print("在第{0}行有重复的key = {1}".format(index + 3, keyStr))
                self.multiKeyValues[keyStr] = valueStr
    
    def InitKeyContainedLists(self):
        for key in self.keyValues:
            for keyStr in self.keyStrs:
                if(keyStr == key):
                    continue
                else:
                    if(keyStr.find(key) > 0):
                        self.keyValues[key]["cotainedKeys"].append(keyStr)

            self.keyValues[key]["cotainedKeys"].sort(key= lambda x:len(x), reverse = True)

    def SearchContent(self, searchCols, outputCol, outputFilePath):
        for index, row in self.contentSheet.iterrows():
            isFindKey = False
            for i in range(searchCols - 1):
                #如果找到可key则直接break
                if(not isFindKey):
                    for key in self.keyValues:
                        if(row[i].count(key) > 0):
                            # valueStr = self.keyValues[key]["val"]
                            finalKeyStr = self.GetFinalKey(key, row[i])
                            valueStr = self.keyValues[finalKeyStr]["val"]
                            # 把值写入对应的index里面(注意：iterrows迭代的是work copy，而非对象本身，所以不能直接对row的那个cell赋值。)
                            self.contentSheet.iloc[index, outputCol - 1] = valueStr
                            # print("index = {0}, outputCol - 1 = {1}".format(index, outputCol - 1))
                            # row[outputCol - 1] = valueStr
                            isFindKey = True
                            break
                else:
                    break
            # print("在第{0}行写入了关键字的值为：{1}".format(index + 3, row[outputCol - 1]))

        #把列名中带unnamed字符串的列丢弃(dataFrame.columns是一个Index Object，可以用.str访问器访问Index里面的元素并进行操作)
        self.contentSheet.drop(self.contentSheet.columns[self.contentSheet.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

        for colLabel, _ in self.contentSheet.iteritems():
            print(str(colLabel))

        (_, tempFileName) = os.path.split(self.filePath)
        (fName, fExtension) = os.path.splitext(tempFileName)
        outputPath = "{0}/{1}_output{2}".format(outputFilePath, fName, fExtension)
        print("输出文件的路径为：", outputPath)
        with pd.ExcelWriter(outputPath) as writer:
            self.contentSheet.to_excel(writer, na_rep="", index=False)
            print("输出文件成功")

    def GetFinalKey(self, key, originalKey):
        for containedKey in self.keyValues[key]["cotainedKeys"]:
            if(originalKey.find(containedKey) > 0):
                return containedKey
        return key


