import time
import socket
import os
import json
import threading
addrs = []
conns = []
players = {}
nicknames = []
tof = True
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1435
s.bind((HOST,PORT))
s.listen()
slash = "\\"
print("Please place the Question Pack in the following directory:")
cwd = os.getcwd()
print(cwd)
print("")
input("Press enter when ready to move on...")
PackName = str(input("What is the name of the pack? "))
PackDirMeta = PackName + slash + "pack.khmeta"
Meta = open(PackDirMeta)
MetaDict = json.load(Meta)
QName = MetaDict["Name"]
NoQs = MetaDict["nq"]
print(f"The Host is {HOST}")
print(f"The Port is {PORT}")
print("Waiting for players...")
def accept_players(s,addrs,conns,tof):
    while tof == True:
        try:
            conn,addr = s.accept()
            addrs.append(addr)
            conns.append(conn)
        except Exception as err:
            print(err)
accept_players_thread = threading.Thread(target=accept_players,args=(s,addrs,conns,tof,))
accept_players_thread.start()
input("")
tof = False





QNum = "Q1"
Num = 1
Num2 = 1
questionsDir = PackName + slash + r"assets" + slash + QName + slash + "questions.json"
QuestionsFile = open(questionsDir,"r")
questions = json.load(QuestionsFile)






for i in range(0,int(NoQs)):
    QuesName = questions[QNum]["question"]
    print(QuesName)
    print("The answers are: ")
    for QTime in range(0,3):
        QAnss = questions[QNum]["answers"][QTime]
        if QTime == 0:
            print(f"A: {QAnss}")
        if QTime == 1:
            print(f"B: {QAnss}")
        if QTime == 2:
            print(f"C: {QAnss}")
    user_ans = str(input("Enter your answer..."))
    correct_ans = questions[QNum]["correct_answer"]
    user_ans = user_ans.lower()
    if user_ans == correct_ans:
        print("You were correct!")
    if user_ans != correct_ans:
        print("You were incorrect!")
        correct_ans = correct_ans.upper()
        print(f"The correct answer was: {correct_ans}")
        print("Waiting after incorrect question...")
        time.sleep(3)
    Num2 += 1
    strnum = str(Num)
    strnum2 = str(Num2)
    QNum = QNum.replace(strnum,strnum2)
    Num = int(strnum)
    Num2 = int(strnum2)
    Num += 1
    print("")
