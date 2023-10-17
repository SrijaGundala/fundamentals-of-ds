import numpy as np
scores=np.array([
[67,45,67,98],
[78,87,89,99],
[89,87,78,77],
[89,87,65,67],
[88,78,87,89],
[88,67,98,77],
[78,87,89,67],
[67,87,99,87],
[67,54,89,90],
[78,76,56,66],
[67,45,67,98],
[78,87,89,99],
[89,87,78,77],
[89,87,65,67],
[88,78,87,89],
[88,67,98,77],
[78,87,89,67],
[67,87,99,87],
[67,54,89,90],
[78,76,56,66],
[67,45,67,98],
[78,87,89,99],
[89,87,78,77],
[89,87,65,67],
[88,78,87,89],
[88,67,98,77],
[78,87,89,67],
[67,87,99,87],
[67,54,89,90],
[78,76,56,66],
[78,76,56,77],
[99,87,78,77]
])
avg_scores=np.mean(scores,axis=0)
avg_highscores=np.argmax(avg_scores)
print("Maths:{:.2f}".format(avg_scores[0]))
print("Science:{:.2f}".format(avg_scores[1]))
print("English:{:.2f}".format(avg_scores[2]))
print("History:{:.2f}".format(avg_scores[3]))

print("Subject with highest average score=",end="")
if avg_highscores==0:
    print("Maths")
elif avg_highscores==1:
    print("Science")
elif avg_highscores==2:
    print("English")
else:
    print("History")



