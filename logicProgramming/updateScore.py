# Original score approach next multiple of five and difference less than 3 that will convert to new score
def getNewScore(students):
    for i in students.keys():
        if students[i] >=40 and students[i]%5 >=2:
            students[i] = 5*(students[i]//5+1)
    return students

if __name__ == '__main__':
   students = {"Derek": 33, "Sean": 73, "Jeff": 63, "Markey": 39}
   print("original score is",students)
   print("updated score is",getNewScore(students))
