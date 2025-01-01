def coursesname():
    with open("courses.txt","r", encoding="utf8") as courses:
        veri = courses.readlines()
        for satır in veri:
            satır=satır.replace("\n","")
            satır=satır.split(";")
            print(satır[1])

def min1coursename():
    min1coursesname=list()
    with open("courses.txt","r", encoding="utf8") as courses1:
        minx = courses1.readlines()
        for satır1 in minx:
            satır1=satır1.replace("\n","")
            satır1=satır1.split(";")
            if int(satır1[3])>0 :
                min1coursesname.append(satır1[1])
    print(min1coursesname)

def addanewcourse():
    coursescode=input("Enter the code of the course you want to add")
    coursesname=input("Enter the name of the course you want to add")
    instructor=input("Enter the name of the instructor you want to add")
    append_x = "{};{};{}".format(coursescode.upper(), coursesname.upper(), instructor.upper())
    with open("courses.txt","a", encoding="utf8") as n:
        n.write("\n")
        n.write(append_x)

def bycoursecode():
    code_x = input("Enter the code of the course you are looking for...")
    with open("courses.txt","r", encoding="utf8") as courses2:
        search =courses2.readlines()
        for satır2 in search:
            satır2=satır2.replace("\n","")
            satır2= satır2.split(";")
            if satır2[0]==code_x.upper():
                print(satır2[1])

def startwith():
    startxx = input("Enter the name of the course you are looking for")
    with open("courses.txt","r", encoding="utf8") as courses3:
        startt=courses3.readlines()
        for satır3 in startt:
            satır3=satır3.replace("\n","")
            satır3=satır3.split(";")
            a = satır3[1]
            if startxx in a:
                print(a)


def seçimlerilistele():
    dict={}
    dict2={}
    with open("courses.txt", "r", encoding="utf8") as f:
        b=f.readlines()
        for y in b:
            y=y.replace("\n","")
            y=y.split(";")
            dict[y[0]]=y[1]

    with open("student.txt","r",encoding="utf8") as regrr:
        a=regrr.readlines()
        for x in a:
            x=x.replace("\n","")
            x=x.split(";")
            dict2[x[1]]=x[2]
    for  students in dict2:
        courses=dict2[students].split(",")
        print(students)
        print("#ALDIĞIDERSLER#")
        for course in courses:
            if course in dict:
                print(dict[course])
            else:
                print(course)


def mostcrowded():
    with open("courses.txt","r", encoding="utf8") as file:
        lines=file.readlines()
        mevcutsayısı=[]
        for course in lines:
            course=course.strip()
            courseDetails=course.split(";")
            mevcutsayısı.append(int(courseDetails[3]))
        mevcutsayısı.sort(reverse=True)
        mevcutsayısı=mevcutsayısı[:3]
        for course in lines:
            course=course.strip()
            courseDetails=course.split(";")
            if int(courseDetails[3]) in mevcutsayısı:
                print(courseDetails[0],courseDetails[1],courseDetails[2])



def enaktiföğrenci():
    hangisikaçders={}
    with open("student.txt","r", encoding="utf8") as courses1:
        minx = courses1.readlines()
        for satır7 in  minx:
            satır7=satır7.replace("\n","")
            satır7=satır7.split(";")
            aldığıderssayısı=satır7[2].split(",")
            hangisikaçders[satır7[1]]=len(aldığıderssayısı)
        c=sorted(hangisikaçders.values())
        sonhal={}
        for i in c:
            for k in hangisikaçders.keys():
                if hangisikaçders[k]==i:
                    sonhal[k]=hangisikaçders[k]
        maxaktif=list(sonhal.items())[-1]
        ortaaktif=list(sonhal.items())[-2]
        aktif=list(sonhal.items())[-3]
        print(maxaktif,ortaaktif,aktif)


def menü():
    while True:
        print("\n"*4)
        print("""UNIVERSITY REGISTRAR'S OFFICE APPLICATION
            ------------------
        1)LİST ALL THE COURSES
        2)LİST ALL the COURSE THAT HAVE AT LEAST ONE STUDENT REGİSTERED
        3)ADD A NEW COURSE 
        4)SEARCH A COURSE BY COURSE CODE
        5)SEARCH A COURSE BY NAME
        6)LİST ALL THE STUDENT THEİR REGİSTERED COURSES
        7)LİST TOP 3 MOST CROWDED COURSE
        8)LİST TOP 3 STUDENT WİTH THE MOST COURSE REGİSTRATİONS
        0)EXİT...
        """)
        c = input("SELECT THE ACTION YOU WANT TO DO..! (0-8)")
        if int(c) == 1:
            print("COURSE NAME LİSTED...")
            coursesname()
        elif int(c)==2:
            print("COURSES THAT AT LEAST ONE STUDENT IS REGISTERED ARE LISTED")
            min1coursename()
        elif int(c)==3:
            print("ADD A NEW COURSE")
            addanewcourse()
        elif int(c)==4:
            print("SEARCH A COURSE BY CODE")
            bycoursecode()
        elif int(c)==5:
            print("SEARCH A COURSE BY COURSE NAME")
            startwith()
        elif int(c)==6:
            print("LİST ALL THE STUDENT THEİR REGİSTERED COURSES")
            seçimlerilistele()
        elif int(c)==7:
            print("LİST TOP 3 MOST CROWDED COURSE")
            mostcrowded()
        elif int(c)==8:
            print("LİST TOP 3 STUDENT WİTH THE MOST COURSE REGİSTRATİONS")
            enaktiföğrenci()
        elif int(c)==0:
            print("ÇIKIŞ YAPILIYOR")
            break

        else:
            print("İNVALİD CHOİCE")


menü()

















            












































































































