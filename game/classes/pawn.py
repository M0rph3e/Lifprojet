#La classe Pawn represente les personnages controllables par le jouer ou par l'AI
import pygame
import time
from .colors import *
from classes.ground import Ground
from classes.wall import Wall
from threading import Thread
DISTANCE_DEPL_MAX=7

class Pawn:
    def __init__(self, x, y, hp, att, defense, team):
        self.x = x
        self.y = y
        self.defense=defense
        self.att=att
        self.hp = hp #j'ai changé # j'ai changé aussi
        self.move_range = 5
        self.attack_range = 1
        self.team = team
        self.canMove=DISTANCE_DEPL_MAX
        self.canAttack=True
        self.fuite=None
    

    
    def move(self, x2, y2,screen,grid_in):

        if self.team==UNIT:
            path = astar(grid_in,self.get_position(),(x2,y2), False)
        elif self.team==ENEMY and self.fuite==True:
            path = astar(grid_in,self.get_position(),(x2,y2), False)
        else:
            path = astar(grid_in,self.get_position(),(x2,y2), True)
        print(path)
        if (self.team==UNIT and len(path) <= self.canMove + 1) or self.team==ENEMY:
            firstCase = True
            if path != None:
                for i in path:
                    if self.canMove<=0:
                        break
                    self.remove_pawn(screen, 20, 20)
                    
                    self.x, self.y = i

                    self.draw_pawn(screen, 20, 20)
                    
                    #print("i :",i)
                    if not firstCase:
                        self.canMove -= 1
                        print("Case restantes", self.canMove)
                    

                    firstCase=False

                    time.sleep(0.25)
                    pygame.display.flip()
            else:
                print("Trop loin")
        else:
            print('Vous pouvez vous déplacer de ', self.canMove, ' cases seulement')


    def draw_pawn(self, screen, height, width):	
        self.rect = pygame.draw.rect(screen, self.team, (self.x * height, self.y * width, width, height))
    
    def remove_pawn(self, screen, height, width):
        pygame.draw.rect(screen, BLACK, (self.x * height, self.y * width, width, height))	
        pygame.draw.rect(screen, GROUND, (self.x * height, self.y * width, width, height),1)

    def get_position(self):
        return (self.x,self.y)

    def attack(self, pion):
        if self.canAttack :
            if(self.get_adjacent(pion) and (self.team != pion.team)):	
                print("Oponent HP", pion.hp)
                pion.hp -= self._difference_attaque(self.att,pion.defense)
                print("After attack", pion.hp)
                self.canAttack=False
                if pion.hp<=0:
                    return True      
            else:
                print("Il est loin pour attaquer, pelo")
        else :
            print("Vous avez déjà attaquer")

    def get_adjacent(self,pion): #verifie qu'un pion est adjacent à un autre
        diff_x = abs(self.x - pion.x)
        diff_y = abs(self.y - pion.y)
        if(diff_x == 0 and diff_y == 1) or (diff_x == 1 and diff_y == 0):
            return True
        else:
            return False

    def get_distance(self,x2,y2): 
        diff_x = abs(self.x - x2)
        diff_y = abs(self.y - y2)
        return diff_x + diff_y

    def getClosestAdjacent(self,endPos,grid):

        options = []
        leftPos = (endPos[0]-1,endPos[1])
        rightPos = (endPos[0]+1,endPos[1])
        bottomPos = (endPos[0],endPos[1]-1)
        topPos = (endPos[0],endPos[1]+1)

        left = self.get_distance(leftPos[0],leftPos[1])
        right = self.get_distance(rightPos[0],rightPos[1])
        bottom = self.get_distance(bottomPos[0],bottomPos[1])
        top = self.get_distance(topPos[0],topPos[1])

        options.append((left,leftPos))
        options.append((right,rightPos))
        options.append((bottom,bottomPos))
        options.append((top,topPos))

        options.sort(key=lambda x: x[0])

        #print(options)
        pos_fin = None
        for pos in options:
             if (isinstance(grid[pos[1][0]][pos[1][1]], Ground)): 
                 pos_fin =  pos[1]
                 return pos_fin
        if pos_fin is None:
            return self.getClosestAdjacent(options[0][1],grid)

    def getFarthestCorner(self,grid):
        topLeft=(1,1)
        topRight=(1,18)
        bottomLeft=(18,1)
        bottomRight=(18,18)

        options = []
        

        tL = self.get_distance(topLeft[0],topLeft[1])
        tR = self.get_distance(topRight[0],topRight[1])
        bL = self.get_distance(bottomLeft[0],bottomLeft[1])
        bR = self.get_distance(bottomRight[0],bottomRight[1])

        options.append((tL,topLeft))
        options.append((tR,topRight))
        options.append((bL,bottomLeft))
        options.append((bR,bottomRight))

        options.sort(key=lambda x: x[0])
        options.reverse()

        for pos in options:
             if (not isinstance(grid[pos[1][0]][pos[1][1]], Wall)): 
                 pos_fin =  pos[1]
                 return pos_fin
        



    #Cette méthode permet de faire la différence entre l'attaque de l'attaquant et la défense de celui qui est attaqué,
    # elle permet de traité le cas ou défense>attaque qui renverra 0 au lieu d'un nb négatif (rajoutant des pv)
    def _difference_attaque(self, attaque, defense):
        diff=(attaque-defense)
        #print("Difference",diff)
        if diff > 0:
            return diff
        else:
            return 0

    def get_traversable(self):
        return False

#Cette partie est consacrée à l'algo de pathfinding 

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position



        



def astar(maze, start, end, adjacent):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    
    if adjacent == True or isinstance(maze[end[0]][end[1]], Pawn):
        pos = Pawn(start[0], start[1], 0, 0, 0, ENEMY)
        endAdj = pos.getClosestAdjacent(end,maze)
        end_node = Node(None, endAdj)
    else:
        end_node = Node(None, end)


    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        if len(open_list) >= 400: #ne se deplace pas si il mets trop longtemps à chercher
            return []

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)



        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #Check if the neighbor is already in closed list (j'ai rajouté lol)
            if Node(current_node,node_position) in closed_list:
                continue
            # Make sure walkable terrain
            #if (isinstance(maze[node_position[0]][node_position[1]], Wall) or isinstance(maze[node_position[0]][node_position[1]], Pawn) or isinstance(maze[node_position[0]][node_position[1]], PawnAI)):
            if node_position[0] != end_node.position[0] or node_position[1] != end_node.position[1]:
                if (not isinstance(maze[node_position[0]][node_position[1]], Ground)): 
                    continue
            # Create new node
            new_node = Node(current_node, node_position)
            # Append
            children.append(new_node)
        # Loop through children
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            
            # Add the child to the open list
            open_list.append(child)








        

    
    
        
