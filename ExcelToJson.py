import os  
import sys  
import codecs  
import xlrd #http://pypi.python.org/pypi/xlrd  
  
global PRINT_LEVEL# 0:no log; 1: warning; 2: prompt; 3: all  
PRINT_LEVEL = 1  
  
def getStrFromObj(obj):  
    if type(obj) == float:  
        return str(int(obj))  
    else:  
        return obj  
          
def getEcelColStr(col):  
    if col <= 26:  
        return chr(ord('A') + col - 1)  
    elif col <= 52:  
        return 'A'+chr(ord('A') + col - 26 - 1)  
    elif col <= 78:  
        return 'A'+chr(ord('A') + col - 26 - 1)  
    else:  
        return str(col)  
  
def praseRowData(outputFile, fieldName, rowData, row):  
    ncols = len(rowData)  
    cellValue = getStrFromObj(rowData[0])  
    outputFile.write('\t\"' + cellValue + '\": {\n')  
    if PRINT_LEVEL >= 3:  
        print ('id: ' + cellValue)  
      
    for col in range(ncols-1):  
        if PRINT_LEVEL >= 3:  
            print ('col: ' + str(col))  
        cellValue = getStrFromObj(rowData[col+1])  
        if PRINT_LEVEL >= 1:  
            if len(cellValue) == 0:  
                colStr = getEcelColStr(col+2)  
                print ('Warning: the value in row %d col %s is null!' % (row+2, colStr))  
        field = fieldName[col+1]  
        if field == "markStr":
            continue;
        if col != 0:  
            outputFile.write(',\n')  
        lineStr = '\"' + field + '\": \"' + cellValue + '\"'  
        if PRINT_LEVEL >= 3:  
            print (lineStr)  
        outputFile.write('\t\t' + lineStr)  
          
    outputFile.write('\n\t}')  
          
  
def mainParse(excelFileName):  

  
    # prase file name  
    #excelFileName = 'aaa.xlsx'
    if PRINT_LEVEL >= 2:  
        print ('Excel File Name: ' + excelFileName)  
    tmpStr = excelFileName.split('.')[0]  
    #jsonFileName = 'output_tables/' + tmpStr[0:1].upper() + tmpStr[1:] + '.json'
    jsonFileName = 'output_tables/' + tmpStr + '.json'  
    if PRINT_LEVEL >= 2:  
        print ('Json File Name: ' + jsonFileName)  
        print ('****************')  
    if os.path.exists(excelFileName) == False:  
        if PRINT_LEVEL >= 1:  
            print ('Warning: the excel file %s dose not exsit!' % (excelFileName))  
        exit(0)  
  
    # open file  
    workbook = xlrd.open_workbook(excelFileName)  
    outputFile = codecs.open(jsonFileName, 'w', 'utf-8')  
      
    # prase  
    if PRINT_LEVEL >= 2:  
        print ('Prase ...')  
    firstLine = True  
    for sheet in workbook.sheets():  
        if sheet.nrows != 0:  
            # prase table data begin  
            if firstLine:  
                firstLine = False  
            else:  
                outputFile.write(u'\n')  
            outputFile.write(u'{\n')  
                  
            # get field  
            fieldName = sheet.row_values(1)  
              
            for row in range(sheet.nrows - 1):
                if row < 1:
                    continue;
                if row != 0 and row != 1:  
                    outputFile.write(',\n')  
                praseRowData(outputFile, fieldName, sheet.row_values(row + 1), row)  
              
            # prase table data end  
            outputFile.write(u'\n}')  
      
    # close file  
    outputFile.close()  
    if PRINT_LEVEL >= 2:  
        print ('****************')  
        print ('Excel to Json Finished!')  
        print ('****************')  

def resetName(name):
    nameList = name.split('.')
    if len(nameList) < 2:
        return
    if nameList[1] == 'xlsx':
        mainParse(name)
def trimfile(dir):
    for fn in os.listdir(dir):
        resetName(fn)


if __name__ == "__main__":
    if not os.path.isdir('output_tables'):
        os.mkdir('output_tables')
    trimfile(os.path.abspath('.'))
