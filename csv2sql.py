# Create: WCY@2022-05-03
#

import csv
import os, sys
import argparse



def openFile(tarFile):
	with open(tarFile) as myCSVFile:
		csvReader = csv.reader(myCSVFile, delimiter=',', quotechar='"')
		resultList = list(csvReader)

	return resultList

def print_Header_And_Few_Line(dataList, limit):
	counter = 0
	for i in dataList:
		if counter > limit:
			break;
		print(i)
		counter += 1

def getColumnIndex():
	colIdxList = []
	idxValue = int(input("請依序輸入你想要的欄位索引值，輸入 -1 結束："))
	
	while idxValue >= 0 :
		colIdxList.append(idxValue)
		idxValue = int(input("請依序輸入你想要的欄位索引值，輸入 -1 結束："))
	
	return colIdxList

def genSQLValues(targetRow, selectedColumnList):

	result = "("
	
	for i in selectedColumnList:
		result += "\"{}\",".format(targetRow[i])

    # The * operator Concatenates multiple copies of the same tuple. 
	# for example:
	#  result = formatStr.format(*rowTuple)
	result = result[:-1] + "),"

	return result

def genSQL_Insert_Cmd(tableName, dataList, colList):
	result = []
	result.append("Insert into {} values (".format(tableName))

	#處理到倒數第二行
	for i in dataList[:-2] :
		result.append(genSQLValues(i, colList))

	#最後一行要用 ); 所以獨立處理
	lastRec = genSQLValues(dataList[-1], colList)
	result.append(lastRec[:-1] + ");\n")		

	return result


if __name__ == '__main__' :

	inputFile = input("請輸入要讀取的檔名：")
	dataList = openFile(inputFile)
	
	limit = int(input("請輸入要顯示前面多少行："))
	print_Header_And_Few_Line(dataList, limit)
	
	colList = getColumnIndex()
	colList.sort
	print("\n你選擇的欄位為：{}".format(colList))

	dataList = dataList[1:]
	#print("\n去掉第一列「欄位名」後：")
	#print_Header_And_Few_Line(dataList, limit)

	tabName = input("你要輸入的資料庫檔名是：")
	sqlList = genSQL_Insert_Cmd(tabName,dataList,colList)

    #印出前三行與末三行
	print("產生資料的前三行與末三行為：")
	print(sqlList[:3])
	print()
	print(sqlList[-4:-1])

	# 將資料寫入一個檔案
	print("資料寫入檔案：{}.sql".format(tabName))
	with open("{}.sql".format(tabName), 'w') as f:
		for item in sqlList:
			f.write("{}\n".format(item))
	
	# 以下是寫入資料庫的範例程式
	#conn = psycopg2.connect(database="your_datbase_name", user="username", password="password", host="ip_address", port="5432")
	#print("Opened database successfully")
	#cur = conn.cursor()
	#with open("{}.sql".format(tabName), 'r') as sqlfile:
	#	cur.execute(sqlfile.read())
	#	conn.commit()
	
	print("程式正常結束")
	sys.exit(0)

	


