#!/usr/bin/python3.7
# main.py

# Donc on part sur quel types de liste?
# 1. La solution optimisée, liste des arrêtes, des bords et des centres
# 2. Liste par ligne/colonne ?

class rubik_face:
  '''need comment
  m_position fonctionne en pair (avant/arrière, gauche/droite, bas/haut)
  m_color est une liste de allant de 1 à 3 couleurs
  '''
  def __init__(self):
    m_position = []
    m_color = [] # from 0 to 5
  def mix(nb):
    '''to do
    '''
  def rotation(pos[], direction):
    '''to do
    '''
  
def initRubiks(corner[], edge[], center[]):
	'''to do
	assemble le cube dans sa configuration initiale
	'''
	x=0
	y=0
	z=0
  
	for i in len(corner):
		for j in len(corner):
			if (i%len(corner)) == 0 and i != 0:
				x=x+1
			if (j%len(corner)) == 0 and j != 0:
				z=z+1			
			corner[i].m_position= (x,y,z)
			#gerer la couleur
	x=0
	y=0
	
	for i in len(edge):
		edge[i].m_position = (x,y)
		y=y+1
	#gerer la couleur
	
	for i in len(center):
		#to do
		
	return corner, edge, center
	
