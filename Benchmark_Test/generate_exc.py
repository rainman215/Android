from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
from datetime import *
import os
import sys
import xlwt
import xlrd
import time

pro='test'
# pro=sys.argv[1]
print pro

os.system('adb pull /sdcard/Log/PlayVideo/cpu_log.txt')
os.system('adb pull /sdcard/Log/PlayVideo/mem_log.txt')

os.system('python list_change cpu_log.txt cpu.txt')
os.system('python list_change mem_log.txt mem.txt')

t=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
name=("FileTest","VideoTest","RebootTest","Antutu","Drawelement","Nemark1","Nemark2","3DRating","GLbench","0xbench")
workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet(name[0])

worksheet=workbook.add_sheet(name[1])
borders=xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style='pattern: pattern solid, fore_colour yellow; '
style += 'font: bold on; '
style += 'align: horz center, vert center; '
data_style=xlwt.easyxf(style)
data_style.borders=borders
worksheet.write(0,0,"Test Video",data_style)
worksheet.col(0).width=17777
worksheet.write(0,1,"CPU Usage",data_style)
worksheet.col(1).width=17777
worksheet.write(0,2,"MEM Usage",data_style)
worksheet.col(2).width=17777

worksheet=workbook.add_sheet(name[2])
worksheet.write(0,0,"Reboot interval",data_style)
worksheet.col(0).width=6666
worksheet.write(0,1,"Setting reboot times",data_style)
worksheet.col(1).width=6666
worksheet.write(0,2,"Current reboot times",data_style)
worksheet.col(2).width=6666
for i in range(3,len(name)):
	worksheet=workbook.add_sheet(name[i])	
	worksheet.write(0,0,"Resolution",data_style)
	worksheet.write(1,0,"1920x1080",data_style)
	worksheet.col(0).width=4444
	worksheet.write(0,1,"AP",data_style)
	worksheet.write(1,1,name[i],data_style)
	worksheet.col(1).width=4444
	worksheet.write(0,2,"Test Item",data_style)
	worksheet.col(2).width=4444
	if name[i]=='GLbench':
		worksheet.write_merge(0,0,3,4,'Result',data_style)
		worksheet.col
	else:	
		worksheet.write(0,3,"Result",data_style)
        worksheet.col(3).width=4444
	#worksheet.write_merge(0,0,3,4,'Result',data_style)
workbook.save('./%s_%sBenchmark_result.xls'%(pro,t))



def wrexcel(row,column,val,sheNum,data_style,cell_width):
	excel=r'./%s_%sBenchmark_result.xls'%(pro,t)
	rb=open_workbook(excel,formatting_info=True)
	wb=copy(rb)
	sheet=wb.get_sheet(sheNum)
	borders=xlwt.Borders()
	borders.left = xlwt.Borders.THIN
	borders.right = xlwt.Borders.THIN
	borders.top = xlwt.Borders.THIN
	borders.bottom = xlwt.Borders.THIN
	data_style.borders=borders
	sheet.write(row,column,val,data_style)
	sheet.col(column).width=cell_width
	os.remove(excel)
	wb.save(excel)

def file_test(file,Num,width):
        f=open(file)
        all_text=f.read()
        style='pattern: pattern solid, fore_colour yellow; '
        style += 'font: bold on; '
        style += 'align: horz left, vert center; '
	alignment = xlwt.Alignment()
	alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
        d_style=xlwt.easyxf(style)
        d_style.alignment = alignment
	wrexcel(0,0,all_text,Num,d_style,width)
        f.close()


def video(file,Num,width):
	count=-1
        f=open(file,"r")
        for line in f:
       		count+=1
                print count
        	line=line.strip('\r\n')
                print line
	        val=count%2
#                print val
        	r=count/2
		print r
        	style='pattern: pattern solid, fore_colour yellow; '
        	style += 'font: bold on; '
        	style += 'align: horz left, vert center; '
        	d_style=xlwt.easyxf(style)
        	n_style=xlwt.easyxf()
        	if val==0:
			wrexcel(r+1,0,line,Num,n_style,width)
        	else:
                	wrexcel(r+1,1,line,Num,d_style,width)
       	f.close


def video_mem(file,Num,width):
        count=-1
        f=open(file,"r")
        for line in f:
                count+=1
                print count
                line=line.strip('\r\n')
                print line
                val=count%2
#                print val
                r=count/2
                print r
                style='pattern: pattern solid, fore_colour yellow; '
                style += 'font: bold on; '
                style += 'align: horz left, vert center; '
                d_style=xlwt.easyxf(style)
                n_style=xlwt.easyxf()
                if val==0:
                        wrexcel(r+1,0,line,Num,n_style,width)
                else:
                        wrexcel(r+1,2,line,Num,d_style,width)
        f.close


def RebootTest(file,Num,width):
        f=open(file,"r")
        for line in f:
                line=line.split(';')
	f.close
	n_style=xlwt.easyxf()
        wrexcel(1,0,line[0],Num,n_style,width)
        wrexcel(1,1,line[1],Num,n_style,width)
        wrexcel(1,2,line[2],Num,n_style,width)



def data(file,Num,width):
	count=-1
	f=open(file,"r")
	for line in f:
		count+=1
#		print count
		line=line.strip('\r\n')
#		print line
		val=count%2
#		print val
		r=count/2
		style='pattern: pattern solid, fore_colour yellow; '
                style += 'font: bold on; '
                style += 'align: horz left, vert center; '
                d_style=xlwt.easyxf(style)
                n_style=xlwt.easyxf()
        	if val==0:
			wrexcel(r+1,2,line,Num,n_style,width)
		else:
			wrexcel(r+1,3,line,Num,d_style,width)
	f.close

def data2(file,Num,width):
        count=-1
        f=open(file,"r")
        for line in f:
                count+=1
#               print count
                line=line.strip('\r\n')
#               print line
		style='pattern: pattern solid, fore_colour yellow; '
                style += 'font: bold on; '
                style += 'align: horz left, vert center; '
                d_style=xlwt.easyxf(style)
		n_style=xlwt.easyxf()
                val=count%3
#                print val
                if val==0:
			r=count/3
                        wrexcel(r+1,2,line,Num,n_style,width)
                elif val==1:
			wrexcel(r+1,3,line,Num,d_style,width)
		else:
			wrexcel(r+1,4,line,Num,d_style,3333)
	        f.close

print "***********Generate Excel**************" 
#file_test("filetest.log",0,9999)
video("cpu.txt",1,17777)
video_mem("mem.txt",1,17777)
RebootTest("setting",2,6666)
data("antutu.txt",3,6666)
data("drawele.txt",4,6666)
data("Nemark1.txt",5,6666)
data("Nemark2.txt",6,6666)
data("3DRating.txt",7,6666)
data2("GLbench.txt",8,7777)
data("0x.txt",9,6666)
print "***********ALL Test Done!**************"
print "Please refer to %s_%sBenchmark_result.xls"%(pro,t)
