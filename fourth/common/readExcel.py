import xlrd
import os

class readExcel(object):
    dir='testData'
    exr_dir = os.path.dirname(os.getcwd()) + "/" + dir
    exr_dir = os.getcwd() + "/" +dir
    # print('+++',dir)
    # print('===',exr_dir)
    exr_dir = exr_dir + "/" + 'data.xls';
    workbook = xlrd.open_workbook(exr_dir)
    sheet1 = workbook.sheet_by_index(0)
    urlSheet = workbook.sheet_by_name('urlSheet')
    paramSheet = workbook.sheet_by_name('paramSheet')
    assertSheet = workbook.sheet_by_name('assertSheet')
    rownum = urlSheet.nrows

    def getInterfaceList(self):
        urlList = []
        for i in range(1,self.rownum):
            rowvalue = self.paramSheet.row_values(i)
            print(rowvalue)
            urlList.append(rowvalue)
        return urlList
    def getParamList(self):
        paramList = []
        for i in range(1,self.rownum):
            rowvalue = self.paramSheet.row_values(i)
            print(rowvalue)
            paramList.append(rowvalue)
        return paramList
    def getAssertList(self):
        assertList = []
        for i in range(1,self.rownum):
            rowvalue = self.paramSheet.row_values(i)
            print(rowvalue)
            assertList.append(rowvalue)
        return assertList
    def assembleData(self):
        urlList=self.getInterfaceList()
        paramList=self.getParamList()
        assertList=self.getAssertList()
        dataList=[]
        for a,b,c,d in urlList:
            singleList=[]
            id = int(a)
            url=b
            method =d
            param =paramList[id-1][1]
            asserts =assertList[id-1][1]
            singleList.append(id)
            singleList.append(url)
            # 请求方式
            singleList.append(method)
            # 参数
            singleList.append(param)
            singleList.append(asserts)
            dataList.append(singleList)
            print('======',singleList)
        # return  dataList