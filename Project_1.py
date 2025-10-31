#Basic student grade analyzer
student_grades={"Rahul":[67,89,98],"Bhavisha":[100,84,99],"Santhosh":[96,54,80],"Santhiya":[92,97,100]}
for student,grades in student_grades.items():
     average=sum(grades)/len(grades)
     print(student,": ",average)
     
