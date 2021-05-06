#Imports
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()


#g.add_edge('Person','Student')
g.add_edges_from([('PERSON','STUDENT'),('PERSON','PROFESSOR'),('PERSON','DEAN')])
g.add_edges_from([('STUDENT','Set of Students')])
g.add_edges_from([('PROFESSOR','Prof1'),('DEAN','Dean1')])
g.add_edges_from([('LIE','Lie1'),('PLAN','Plan1'),('Plan1','Lie1'),('Set of Students','Plan1'),('Lie1','Tell2'),('Tell2','Prof1')])
g.add_edges_from([('STUDY','Study1')])
g.add_edges_from([('HATE','Hate1'),('Set of Students','Hate1'),('Hate1','STUDY')])

g.add_edges_from([('STORY','Story1'),('TELL','Tell1'),('TELL','Tell2'),('Story1','__Wedding'),('Story1','__Wedding'),('Story1','__Car Broke')])
g.add_edges_from([('Set of Students','Tell1'),('Tell1','Story1'),('Tell1','Dean1')])

g.add_edges_from([('AGREE','Agree1'),('GIVE','Give1'),('EXAM','Exam1'),('EXAM','Exam2')])

g.add_edges_from([('Dean1','Agree1'),('Agree1','Give1'),('Give1','Set of Students'),('Set of Students', 'Exam2')])
g.add_edges_from([('Set of Students','Study1'),('Study1','Exam2')])
g.add_edges_from([('ASK','Ask1'),('SIT','Sit1'),('ROOMS','Set of Separate Rooms')])
g.add_edges_from([('Dean1','Ask1'),('Ask1','Set of Students'),('Set of Students','Sit1'),('Sit1','Set of Separate Rooms')])
g.add_edges_from([('QUES','Ques1'),('QUES','Ques2')])
g.add_edges_from([('Exam2','Ques1'),('Exam2','Ques2')])



print(nx.info(g))
nx.draw(g, with_labels=True)

plt.show()

