# solutions.py
"""The Page Rank Algorithm.

"""
import numpy as np
from scipy import linalg as la
import networkx as nx
import itertools

# Problems 1-2
class DiGraph:
    """A class for representing directed graphs via their adjacency matrices.

    Attributes:
        (fill this out after completing DiGraph.__init__().)
    """
    # Problem 1
    def __init__(self, A, labels=None):
        """Modify A so that there are no sinks in the corresponding graph,
        then calculate Ahat. Save Ahat and the labels as attributes.

        Parameters:
            A ((n,n) ndarray): the adjacency matrix of a directed graph.
                A[i,j] is the weight of the edge from node j to node i.
            labels (list(str)): labels for the n nodes in the graph.
                If None, defaults to [0, 1, ..., n-1].
        """
        #raise NotImplementedError("Problem 1 Incomplete")
        #check if there's an issue
        if labels and len(labels) != len(A):
            raise ValueError('number of labels is not the same as number of nodes in graph')
        #modify a so it has no sinks
        self.Ahat = np.copy(A)
        #make it so there are no sinks

        # for i in range(len(self.Ahat[0])):
        #     if self.Ahat[:,i].sum()== 0:
        #         self.Ahat[:,i] = 1
        self.Ahat[:,self.Ahat.sum(axis=0)==0] = 1
        self.A = self.Ahat/np.sum(self.Ahat,axis=0)

        #create labels
        if labels == None:
            labels = [i for i in range(len(self.A))]

        #instantiate other stuff
        self.labels = labels
        s = sum(self.A)
        self.n = len(self.A)

    # Problem 2
    def linsolve(self, epsilon=0.85):
        """Compute the PageRank vector using the linear system method.

        Parameters:
            epsilon (float): the damping factor, between 0 and 1.

        Returns:
            dict(str -> float): A dictionary mapping labels to PageRank values.
        """
        #raise NotImplementedError("Problem 2 Incomplete")

        #solve for p
        m = np.eye(self.n) - epsilon*self.A
        p = la.inv(m)@(((1-epsilon)/self.n)*np.ones(self.n))
        return dict(zip(self.labels,p))


    # Problem 2
    def eigensolve(self, epsilon=0.85):
        """Compute the PageRank vector using the eigenvalue method.
        Normalize the resulting eigenvector so its entries sum to 1.

        Parameters:
            epsilon (float): the damping factor, between 0 and 1.

        Return:
            dict(str -> float): A dictionary mapping labels to PageRank values.
        """
        #raise NotImplementedError("Problem 2 Incomplete")

        #create matrix
        n = len(self.A)
        E = np.ones((self.n,self.n))
        B = epsilon* self.A + ((1-epsilon)/self.n)*E

        #get evals and evecs and find desired value
        evals, evec = la.eig(B)
        l = np.argsort(eval)[-1]
        p = evec[:,l]
        p = p/sum(p)
        return dict(zip(self.labels,p))

    # Problem 2
    def itersolve(self, epsilon=0.85, maxiter=100, tol=1e-18):
        """Compute the PageRank vector using the iterative method.

        Parameters:
            epsilon (float): the damping factor, between 0 and 1.
            maxiter (int): the maximum number of iterations to compute.
            tol (float): the convergence tolerance.

        Return:
            dict(str -> float): A dictionary mapping labels to PageRank values.
        """
        #raise NotImplementedError("Problem 2 Incomplete")
        #set up p(0)
        p = np.ones(self.n) / self.n

        #loop iteratively
        for i in range(maxiter):
            pt1 = epsilon*self.A@p + ((1-epsilon)/self.n)#*np.ones(self.n)
            #check
            if la.norm(p - pt1) <tol:
                #return dict(zip(self.labels,pt1))
                break
            p = pt1.copy()
        p /= p.sum()
        #return
        return dict(zip(self.labels,p))

def tester():
    A = np.array([[0,0,0,0],[1,0,1,0],[1,0,0,1],[1,0,1,0]])
    D = DiGraph(A, labels = ['a','b','c','d'])
    d = D.itersolve()
    print(get_ranks(d))
# Problem 3
def get_ranks(d):
    """Construct a sorted list of labels based on the PageRank vector.

    Parameters:
        d (dict(str -> float)): a dictionary mapping labels to PageRank values.

    Returns:
        (list) the keys of d, sorted by PageRank value from greatest to least.
    """
    #raise NotImplementedError("Problem 3 Incomplete")

    #sort keys
    keys = list(d.keys())

    #get the order right
    order = np.argsort(list(d.values()))[::-1]
    return [keys[i] for i in order]


# Problem 4
def rank_websites(filename="web_stanford.txt", epsilon=0.85):
    """Read the specified file and construct a graph where node j points to
    node i if webpage j has a hyperlink to webpage i. Use the DiGraph class
    and its itersolve() method to compute the PageRank values of the webpages,
    then rank them with get_ranks().

    Each line of the file has the format
        a/b/c/d/e/f...
    meaning the webpage with ID 'a' has hyperlinks to the webpages with IDs
    'b', 'c', 'd', and so on.

    Parameters:
        filename (str): the file to read from.
        epsilon (float): the damping factor, between 0 and 1.

    Returns:
        (list(str)): The ranked list of webpage IDs.
    """
    #raise NotImplementedError("Problem 4 Incomplete")

    #set up this annoying data
    with open(filename,'r') as file:
        contents = file.read().split('\n')

    new = []
    for i in range(len(contents)-1):
        new.append(list(contents[i].split('/')))
    #new = sorted(new)
    s = set()
    for i in new:
        for j in i:
            s.add(j)

    nodes = sorted(list(s))

    #determine dictionary
    websites = dict(zip(nodes, np.arange(len(nodes))))

    A = np.zeros((len(nodes), len(nodes)))
    for i in new:
        for j in i[1:]:
            A[websites.get(j), websites.get(i[0])] += 1

    #plug in to previous functions
    G = DiGraph(A, nodes)
    d = G.itersolve(epsilon = epsilon)
    return get_ranks(d)



def p4tester():
    c1=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '332', '106064', '31328', '86049', '123900', '74923', '119538', '90571', '139197', '116900', '15672']
    c2=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '332', '106064', '31328', '86049', '123900', '74923', '119538', '90571', '116900', '139197', '20283']
    c3=['98595', '32791', '178606', '64104', '96254', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '106064', '332', '31328', '86049', '123900', '74923', '119538', '90571']
    c4=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '332', '106064', '31328', '86049', '123900', '74923', '90571', '119538', '139197', '116900', '20283']
    c5=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '332', '106064', '31328', '86049', '123900', '74923', '119538', '90571', '116900', '139197', '114623']
    c6=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '106064', '332', '31328', '86049', '123900', '74923', '90571', '119538', '116900', '139197', '15672']
    c7=['98595', '32791', '28392', '77323', '92715', '26083', '130094', '99464', '12846', '106064', '332', '31328', '86049', '123900', '74923', '90571', '119538', '139197', '116900', '15672']

    print(rank_websites(epsilon=0.94)[:20]==c1[:20])
    print(rank_websites(epsilon=0.89)[:20]==c2[:20])
    print(rank_websites(epsilon=0.40)[:20]==c3[:20])
    print(rank_websites(epsilon=0.66)[:20]==c4[:20])
    print(rank_websites(epsilon=0.61)[:20]==c5[:20])
    print(rank_websites(epsilon=0.76)[:20]==c6[:20])
    print(rank_websites(epsilon=0.86)[:20]==c7[:20])


# Problem 5
def rank_ncaa_teams(filename, epsilon=0.85):
    """Read the specified file and construct a graph where node j points to
    node i with weight w if team j was defeated by team i in w games. Use the
    DiGraph class and its itersolve() method to compute the PageRank values of
    the teams, then rank them with get_ranks().

    Each line of the file has the format
        A,B
    meaning team A defeated team B.

    Parameters:
        filename (str): the name of the data file to read.
        epsilon (float): the damping factor, between 0 and 1.

    Returns:
        (list(str)): The ranked list of team names.
    """
    #raise NotImplementedError("Problem 5 Incomplete")
    #set up this annoying data
    with open(filename,'r') as file:
        contents = file.read().split('\n')
        contents = contents[1:]
    new = []
    for i in range(len(contents)):
        new.append(list(contents[i].split(',')))
    s = set()
    for i in new:
        for j in i:
            s.add(j)

    nodes = list(s)

    #set up dictionary
    websites = dict(zip(nodes, np.arange(len(nodes))))

    A = np.zeros((len(nodes), len(nodes)))
    for i in new:
        for j in i[1:]:
            #account for weights
            A[websites.get(i[0]), websites.get(j)] +=1


    #plug in to previous functions
    G = DiGraph(A, nodes)
    d = G.itersolve(epsilon = epsilon)
    return get_ranks(d)


# Problem 6
def rank_actors(filename="top250movies.txt", epsilon=0.85):
    """Read the specified file and construct a graph where node a points to
    node b with weight w if actor a and actor b were in w movies together but
    actor b was listed first. Use NetworkX to compute the PageRank values of
    the actors, then rank them with get_ranks().

    Each line of the file has the format
        title/actor1/actor2/actor3/...
    meaning actor2 and actor3 should each have an edge pointing to actor1,
    and actor3 should have an edge pointing to actor2.
    """
    #raise NotImplementedError("Problem 6 Incomplete")
    #set up data
    with open(filename,'r',encoding="utf-8") as file:
        contents = file.read().split('\n')
    contents = [i.split('/') for i in contents] #split within the contents list
    contents = contents[:-1] #because of the new line, get rid of one extra space


    #set up graph
    DG = nx.DiGraph()
    for i in range(len(contents)):
        L = list(itertools.combinations(contents[i][1:],2))
        for c in L:

            if DG.has_edge(c[1],c[0]):
                DG[c[1]][c[0]]["weight"] += 1
            else:
                DG.add_edge(c[1], c[0], weight=1)

    #find ranking keys
    return  get_ranks(nx.pagerank(DG, alpha=epsilon))
