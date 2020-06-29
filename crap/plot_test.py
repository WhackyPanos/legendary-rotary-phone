import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
rect = ax.barh(langs,students)
ax.set_ylabel('Students')
ax.set_xlabel('Language')
ax.set_title('How many students per language')
# plt.show()

plt.savefig('testplot.png',bbox_inches='tight')


