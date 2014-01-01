#coding=utf8

#@Author:   Leo Lou
#@Email:    qibinlou@hotmail.com
#@Date:     2014.1.1
#@Version:  1.0

import os
def PhotoSync(jpgpath, cr2path, sourcetype = "JPG", rawtype = "CR2"):
    """
       @jpgath is the path you place your source photos(eg. .JPG) 
       @cr2path is the path you place your raw photos(eg. .CR2)
    """
    s = raw_input("Befor the clean job, you'd better make a copy of your rawtype photos!\nPrepared to continue? Press y or Y\n")
    if s != 'y' and s != 'Y':
        print "You have killed this job! Please try again!\n"
        return
    try:
        os.chdir(jpgpath)
    except Exception, e:
        print e,jpgpath
        return
    else:
        try:
            sourcephotolist = [photo.split('.')[0] for photo in os.listdir(jpgpath) if photo.endswith('.' + sourcetype)]
            os.chdir(cr2path)
        except Exception, e:
            print e,cr2path
            return
        else:
            print sourcephotolist
            rawphotolist = [photo for photo in os.listdir(cr2path) if photo.endswith('.' + rawtype)]
            print rawphotolist
            for photo in rawphotolist:
                if photo.split('.')[0] not in sourcephotolist:
                    print photo
                    try:
                        os.remove(photo)
                    except Exception, e:
                        print e
    print "Congratulations! The raw type photos have been synchronized!\n"
                    
        # print os.listdir(path)

if __name__ == '__main__':
    phototypes = ["JPG", "jpg", "CR2", "tiff", "NEF", "jpeg", "bmp", "png", "gif"]
    while True:
        st = raw_input("Please input the source photo type! The default type is JPG\n")
        if st in phototypes:
            break
    while True:
        rt = raw_input("Please input the raw photo type! The default type is CR2\n")
        if rt in phototypes:
            break
    jpgpath = raw_input("Please the JPG photo path\n")
    rawpath = raw_input("Please the CR2 photo path\n")
    PhotoSync(jpgpath, rawpath, sourcetype = st, rawtype = rt)

    
