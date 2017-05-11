from PIL import Image, ImageFilter
import os

allFileNum = 0  

def printPath(level, path):  
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    ''' 
    fileList = []
    dirList = [] 
    # 所有文件夹，第一个字段是次目录的级别  
      
    # 所有文件  
      
    # 返回一个列表，其中包含在目录条目的名称(google翻译)  
    files = os.listdir(path)  
    # 先添加目录级别  
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # 排除隐藏文件夹。因为隐藏文件夹过多  
            if(f[0] == '.'):  
                pass  
            else:  
                # 添加非隐藏文件夹  
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            # 添加文件  
            fileList.append(f)  

    temp_im = Image.open('./temp.png')
    r,g,b,a = temp_im.split()
    temp_w, temp_h = temp_im.size

    for fl in fileList:  
        # 打印文件  
        print ('-' * (int(dirList[0])), fl)  
        # 随便计算一下有多少个文件  
        allFileNum = allFileNum + 1  
        # 打开一个jpg图像文件，注意路径要改成你自己的:
        im = Image.open(path + fl)        
        w, h = im.size        
        x = 0
        y = 0
        
        while y <= h:
            while x <= w:
                    im.paste(temp_im, (x, y), mask = a)
                    x = x + temp_w
                    # print(str(x)+","+str(y))
            x = 0
            y = y + temp_h

		# 把缩放后的图像用jpeg格式保存:
        im.save('./thumb/' + fl + '_thumb.jpg', 'jpeg')  
  
if __name__ == '__main__':  
    printPath(1, './img/')  

    print ('总文件数 =', allFileNum)