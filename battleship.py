

SIZE = 10315

class Node():

    __slots__ = '_role', '_no', '_ne', '_se', '_so', '_fron', '_leaf', '_parent'

    def __init__(self):
        self._no = None
        self._ne = None
        self._se = None
        self._so = None
        self._fron = None      # frontiere du region (left, right, top, bottom) #attention: the order is different from the bombes
        self._role = 0         # null:0; interne:1; leaf:-1;
        self._leaf = None      # the coordinates of a ship
        self._parent = None

    def __str__(self):
        if self._role == -1:
            return "["+str(self._leaf[0])+" "+str(self._leaf[1])+"]"
        elif self._role == 0:
            return "<0 0 0 0>"
        else:
            if self._no == None: no = 0
            else: no = 1
            if self._ne == None: ne = 0
            else: ne = 1
            if self._se == None: se = 0
            else: se = 1
            if self._so == None: so = 0
            else: so = 1
            return "<"+str(no)+" "+str(ne)+" "+str(se)+" "+str(so)+">"

    def setFron(self, fron):
        self._fron = fron

    def setNo(self, no):
        self._no = no

    def setNe(self, ne):
        self._ne = ne

    def setSe(self, se):
        self._se = se

    def setSo(self, so):
        self._so = so

    def setRole(self, role):
        self._role = role

    def setLeaf(self, leaf):
        self._leaf = leaf

    def setParent(self, parent):
        self._parent = parent


class Quadtree():

    __slots__ = '_root'

    def __init__(self):
        self._root = Node()

    # method to return a list of the children of a node
    def children(self, node):
        if node._role == 0 or node._role == -1:
            return []
        else:
            childre = []
            if node._no != None: childre.append(node._no)
            if node._ne != None: childre.append(node._ne)
            if node._se != None: childre.append(node._se)
            if node._so != None: childre.append(node._so)
            return childre

    # method to determine the location of a ship in a certain frontiere
    # topleft:1; topright:2; bottomright:3; bottomleft:4;
    def location(self, fron, ship):
        midX = (fron[1]-fron[0])/2 + fron[0]
        midY = (fron[3]-fron[2])/2 + fron[2]
        if ship[0] < midX and ship[1] < midY:
            return 1
        elif ship[0] > midX and ship[1] < midY:
            return 2
        elif ship[0] > midX and ship[1] > midY:
            return 3
        elif ship[0] < midX and ship[1] > midY:
            return 4
        else:
            return "in the border line"

    # method to determine the situation of 2 ships
    # return value indicates:
    # 10: 2 ships at the same topleft region; 20: 2 ships in the same topright region; 30: same bottomright; 40: same bottomleft
    # 1: one ship at the topleft corner and one at the bottomright corner; 2: one at topleft and one at topright;
    # 3: one at topleft and one at bottomleft; 4: one at topright and one at bottomleft
    # 5: one at the bottomleft and one at bottomright; 6: one at topright and one at bottomright
    def situation(self, A, B):
        if A == B == 1:
            return 10
        elif A == B == 2:
            return 20
        elif A == B == 3:
            return 30
        elif A == B == 4:
            return 40
        elif (A==1 and B==3):
            return 1
        elif (A==1 and B==2):
            return 2
        elif (A==1 and B==4):
            return 3
        elif (A==2 and B==4):
            return 4
        elif (A==4 and B==3):
            return 5
        elif (A==2 and B==3):
            return 6
        elif (B==1 and A==3):
            return -1
        elif (B==1 and A==2):
            return -2
        elif (B==1 and A==4):
            return -3
        elif (B==2 and A==4):
            return -4
        elif (B==4 and A==3):
            return -5
        elif (B==2 and A==3):
            return -6

    # methods to add 2 ships(leafs) into the data structure according to the situations
    # addS1 indicates add 2 ships if these 2 ships are in situation 1 (see the situation() method)
    # and so on
    def addS1(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        no = Node()
        no.setFron([node._fron[0], midX, node._fron[2], midY])
        no.setLeaf(A)
        no.setParent(node)
        no.setRole(-1)
        se = Node()
        se.setFron([midX, node._fron[1], midY, node._fron[3]])
        se.setLeaf(B)
        se.setParent(node)
        se.setRole(-1)
        node.setNo(no)
        node.setSe(se)

    def addS2(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        no = Node()
        no.setFron([node._fron[0], midX, node._fron[2], midY])
        no.setLeaf(A)
        no.setParent(node)
        no.setRole(-1)
        ne = Node()
        ne.setFron([midX, node._fron[1], node._fron[2], midY])
        ne.setLeaf(B)
        ne.setParent(node)
        ne.setRole(-1)
        node.setNo(no)
        node.setNe(ne)

    def addS3(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        no = Node()
        no.setFron([node._fron[0], midX, node._fron[2], midY])
        no.setLeaf(A)
        no.setParent(node)
        no.setRole(-1)
        so = Node()
        so.setFron([node._fron[0], midX, midY, node._fron[3]])
        so.setLeaf(B)
        so.setParent(node)
        so.setRole(-1)
        node.setNo(no)
        node.setSo(so)

    def addS4(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        ne = Node()
        ne.setFron([midX, node._fron[1], node._fron[2], midY])
        ne.setLeaf(A)
        ne.setParent(node)
        ne.setRole(-1)
        so = Node()
        so.setFron([node._fron[0], midX, midY, node._fron[3]])
        so.setLeaf(B)
        so.setParent(node)
        so.setRole(-1)
        node.setNe(ne)
        node.setSo(so)

    def addS5(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        se = Node()
        se.setFron([midX, node._fron[1], midY, node._fron[3]])
        se.setLeaf(B)      # attention, B first here
        se.setParent(node)
        se.setRole(-1)
        so = Node()
        so.setFron([node._fron[0], midX, midY, node._fron[3]])
        so.setLeaf(A)
        so.setParent(node)
        so.setRole(-1)
        node.setSe(se)
        node.setSo(so)

    def addS6(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        ne = Node()
        ne.setFron([midX, node._fron[1], node._fron[2], midY])
        ne.setLeaf(A)
        ne.setParent(node)
        ne.setRole(-1)
        se = Node()
        se.setFron([midX, node._fron[1], midY, node._fron[3]])
        se.setLeaf(B)
        se.setParent(node)
        se.setRole(-1)
        node.setNe(ne)
        node.setSe(se)

    def addS10(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        no = Node()
        no.setFron([node._fron[0], midX, node._fron[2], midY])
        no.setLeaf(A)
        no.setParent(node)
        no.setRole(-1)
        node.setNo(no)
        self.addNodeLeaf(node._no, B[0], B[1])

    def addS20(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        ne = Node()
        ne.setFron([midX, node._fron[1], node._fron[2], midY])
        ne.setLeaf(A)
        ne.setParent(node)
        ne.setRole(-1)
        node.setNe(ne)
        self.addNodeLeaf(node._ne, B[0], B[1])

    def addS30(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        se = Node()
        se.setFron([midX, node._fron[1], midY, node._fron[3]])
        se.setLeaf(A)
        se.setParent(node)
        se.setRole(-1)
        node.setSe(se)
        self.addNodeLeaf(node._se, B[0], B[1])

    def addS40(self, node, A, B):
        node.setRole(1)
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        so = Node()
        so.setFron([node._fron[0], midX, midY, node._fron[3]])
        so.setLeaf(A)
        so.setParent(node)
        so.setRole(-1)
        node.setSo(so)
        self.addNodeLeaf(node._so, B[0], B[1])

    # method to add a leaf into a leaf
    def addNodeLeaf(self, node, x, y):               # when the node is a leaf
        A = self.location(node._fron, node._leaf)    # we turns the leaf into an interne
        B = self.location(node._fron, (x, y))        # then add 2 leafs into this interne
        s = self.situation(A, B)
        if s == 1:
            self.addS1(node, node._leaf, (x, y))
        elif s == -1:
            self.addS1(node, (x, y), node._leaf)
        elif s == 2:
            self.addS2(node, node._leaf, (x, y))
        elif s == -2:
            self.addS2(node, (x, y), node._leaf)
        elif s == 3:
            self.addS3(node, node._leaf, (x, y))
        elif s == -3:
            self.addS3(node, (x, y), node._leaf)
        elif s == 4:
            self.addS4(node, node._leaf, (x, y))
        elif s == -4:
            self.addS4(node, (x, y), node._leaf)
        elif s == 5:
            self.addS5(node, node._leaf, (x, y))
        elif s == -5:
            self.addS5(node, (x, y), node._leaf)
        elif s == 6:
            self.addS6(node, node._leaf, (x, y))
        elif s == -6:
            self.addS6(node, (x, y), node._leaf)
        elif s == 10:
            self.addS10(node, node._leaf, (x, y))
        elif s == 20:
            self.addS20(node, node._leaf, (x, y))
        elif s == 30:
            self.addS30(node, node._leaf, (x, y))
        elif s == 40:
            self.addS40(node, node._leaf, (x, y))

    # method to add a ship(B) into an interne which the position is null
    # situation there is no collision of 2 ships
    def addAtNone(self, node, position, B):
        midX = (node._fron[1]-node._fron[0])/2 + node._fron[0]
        midY = (node._fron[3]-node._fron[2])/2 + node._fron[2]
        add = Node()
        add.setLeaf(B)
        add.setParent(node)
        add.setRole(-1)
        if position == 1:
            add.setFron([node._fron[0], midX, node._fron[2], midY])
            node.setNo(add)
        elif position == 2:
            add.setFron([midX, node._fron[1], node._fron[2], midY])
            node.setNe(add)
        elif position == 3:
            add.setFron([midX, node._fron[1], midY, node._fron[3]])
            node.setSe(add)
        elif position == 4:
            add.setFron([node._fron[0], midX, midY, node._fron[3]])
            node.setSo(add)

    # method to add a leaf(x, y) into a node
    def helper(self, node, x, y):
        if (node._role == 0):                             # when the root is none
            node.setRole(-1)
            node.setLeaf((x, y))
            node.setFron((0, SIZE, 0, SIZE))
            return node
        elif node._role == -1:                           # when the node is a leaf
            self.addNodeLeaf(node, x, y)
        else:                                           # when the node is an interne
            B = self.location(node._fron, (x, y))       # we locate the leaf which is going to be add
            if B == 1:                                  # then put it into the quadrant where it's belong to (method recursion)
                if node._no == None:
                    self.addAtNone(node, B, (x, y))
                else:
                    return self.helper(node._no, x, y)
            elif B == 2:
                if node._ne == None:
                    self.addAtNone(node, B, (x, y))
                else:
                    return self.helper(node._ne, x, y)
            elif B == 3:
                if node._se == None:
                    self.addAtNone(node, B, (x, y))
                else:
                    return self.helper(node._se, x, y)
            elif B == 4:
                if node._so == None:
                    self.addAtNone(node, B, (x, y))
                else:
                    return self.helper(node._so, x, y)

    # method to add a leaf(x, y) into the tree
    def insertion(self, x, y):
        return self.helper(self._root, x, y)

    # method to determinate the location of a bombe
    # value returned indicates:
    # 1: the bombe is inside the north-west quadrant; 2: the bombe is inside the north-est quadrant
    # 4: the bombe is inside the south-west quadrant; 3: the bombe is inside the south-est quadrant
    # 12: the bombe is inside the north-west and north-est quadrant;
    # and so on
    def locationOfBombe(self, fron, zone):
        midX = (fron[1] - fron[0]) / 2 + fron[0]
        midY = (fron[3] - fron[2]) / 2 + fron[2]
        if fron[0] <= zone[0] and midX >= zone[2] and fron[2] <= zone[1] and midY >= zone[3]:
            return 1
        elif midX <= zone[0] and fron[1] >= zone[2] and fron[2] <= zone[1] and midY >= zone[3]:
            return 2
        elif midX <= zone[0] and fron[1] >= zone[2] and midY <= zone[1] and fron[3] >= zone[3]:
            return 3
        elif fron[0] <= zone[0] and midX >= zone[2] and midY <= zone[1] and fron[3] >= zone[3]:
            return 4
        elif fron[0] <= zone[0] and fron[1] >= zone[2] and fron[2] <= zone[1] and midY >= zone[3]:
            return 12
        elif midX <= zone[0] and fron[1] >= zone[2] and fron[2] <= zone[1] and fron[3] >= zone[3]:
            return 23
        elif fron[0] <= zone[0] and fron[1] >= zone[2] and midY <= zone[1] and fron[3] >= zone[3]:
            return 34
        elif fron[0] <= zone[0] and midX >= zone[2] and fron[2] <= zone[1] and fron[3] >= zone[3]:
            return 14
        elif fron[0] <= zone[0] and fron[1] >= zone[2] and fron[2] <= zone[1] and fron[3] >= zone[3]:
            return 1234
        else:
            raise Exception("Error in locationOfBombe")

    # method to delete the intern which all children are null
    def deleteInterne(self, interne):
        if interne._no == interne._ne == interne._se == interne._so == None and interne != self._root:
            self.setNone(interne)

    # method to delete a node from a tree
    def setNone(self, node):
        parent = node._parent
        if parent._no != None and parent._no._fron == node._fron:
            parent.setNo(None)
        elif parent._ne != None and parent._ne._fron == node._fron:
            parent.setNe(None)
        elif parent._se != None and parent._se._fron == node._fron:
            parent.setSe(None)
        elif parent._so != None and parent._so._fron == node._fron:
            parent.setSo(None)
        else:
            raise Exception("Error in setNone")
        node.setParent(None)
        self.deleteInterne(parent)

    # method to delete a node from a bombe zone. the node may be a subtree.
    #'zone' est une liste des quatres coordonées qui représente la portée d'une bombe (x1 y1 x2 y2)
    def suppression(self, node, zone):
        if node != None:

            # if the node is inside the bombe zone, we delete the whole node(could be a subtree, or the whole tree)
            if node._fron[0] >= zone[0] and node._fron[1] <= zone[2] and node._fron[2] >= zone[1] and node._fron[3] <= zone[3]:
                if node != self._root:
                    self.setNone(node)
                else:
                    self._root.setNo(None)
                    self._root.setNe(None)
                    self._root.setSe(None)
                    self._root.setSo(None)
                    self._root.setRole(0)

            # if the node is a leaf, check if the ship is inside the bombe zone
            elif node._role == -1:
                if node._leaf[0] >= zone[0] and node._leaf[0] <= zone[2] and node._leaf[1] >= zone[1] and node._leaf[1] <= zone[3]:
                    if node != self._root:
                        self.setNone(node)

            # if the node is an interne and the bombe zone is inside the node frontiere,
            # check the location of the bombe, then seperate the bombe into different quadrant to continue to delete the node
            # recurtion
            elif node._role == 1:
                l = self.locationOfBombe(node._fron, zone)
                if l == 1 and node._no != None:
                    self.suppression(node._no, zone)
                elif l == 2 and node._ne != None:
                    self.suppression(node._ne, zone)
                elif l == 3 and node._se != None:
                    self.suppression(node._se, zone)
                elif l == 4 and node._so != None:
                    self.suppression(node._so, zone)
                elif l == 12:
                    if node._no != None:
                        self.suppression(node._no, [zone[0], zone[1], node._no._fron[1], zone[3]])
                    if node._ne != None:
                        self.suppression(node._ne, [node._ne._fron[0], zone[1], zone[2], zone[3]])
                elif l == 23:
                    if node._ne != None:
                        self.suppression(node._ne, [zone[0], zone[1], zone[2], node._ne._fron[3]])
                    if node._se != None:
                        self.suppression(node._se, [zone[0], node._se._fron[2], zone[2], zone[3]])
                elif l == 34:
                    if node._se != None:
                        self.suppression(node._se, [node._se._fron[0], zone[1], zone[2], zone[3]])
                    if node._so != None:
                        self.suppression(node._so, [zone[0], zone[1], node._so._fron[1], zone[3]])
                elif l == 14:
                    if node._no != None:
                        self.suppression(node._no, [zone[0], zone[1], zone[2], node._no._fron[3]])
                    if node._so != None:
                        self.suppression(node._so, [zone[0], node._so._fron[2], zone[2], zone[3]])
                elif l == 1234:
                    if node._no != None:
                        self.suppression(node._no, [zone[0], zone[1], node._no._fron[1], node._no._fron[3]])
                    if node._ne != None:
                        self.suppression(node._ne, [node._ne._fron[0], zone[1], zone[2], node._ne._fron[3]])
                    if node._se != None:
                        self.suppression(node._se, [node._se._fron[0], node._se._fron[2], zone[2], zone[3]])
                    if node._so != None:
                        self.suppression(node._so, [zone[0], node._so._fron[2], node._so._fron[1], zone[3]])

    # method to print the tree
    def affichage(self):
        if self._root._role == 0 or self._root._role == -1:
            print(self._root)
        elif self._root._role == 1:
            Q = [self._root]
            while Q:
                next_level = []
                for node in Q:
                    print(node, end='')
                    for child in self.children(node):
                        next_level.append(child)
                print()
                Q = next_level

def jouer():
    grille = Quadtree()
    with open('bateaux.txt') as bateaux:
        for line in bateaux:
            coordinates = [int(x) for x in line.split(' ')]
            if len(coordinates) == 2:
                grille.insertion(coordinates[0], coordinates[1])
            else:
                raise Exception('2 coordonnées sont requises')

    with open('bombes.txt') as bombes:
        for line in bombes:
            coordinates = [int(x) for x in line.split('.')]
            if len(coordinates) == 4:
                grille.suppression(grille._root, coordinates)
            else:
                raise Exception('4 coordonnées sont requises')

    grille.affichage()




if __name__ == '__main__':

    jouer()