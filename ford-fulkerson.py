from collections import defaultdict
#Ford-Fulkerson max flow
class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = defaultdict(list)
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    print ('path after enter MaxFlow: %s' % path)
    for key in self.flow:
      print ('%s:%s' % (key,self.flow[key]))
    print ('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      for key in self.flow:
        print('%s:%s' % (key,self.flow[key]))
      path = self.FindPath(source, target, [])
      print ('path inside of while loop: %s' % path)
    for key in self.flow:
      print ('%s:%s' % (key,self.flow[key]))
    return sum(self.flow[edge] for edge in self.GetEdges(source))


if __name__ == "__main__":
  g = FlowNetwork()
  map(g.AddVertex, ['MT', 'GO', 'DF', 'MG', 'CE',
                    'RN', 'MS', 'TO', 'PA', 'AM', 'AP',
                    'MA', 'PB_JPA', 'RS', 'PR', 'SC', 'SP', 'RJ',
                    'ES', 'BA', 'SE', 'AL', 'PE', 'PI', 'PB-CGE'])
  g.AddEdge('MT','GO',10)
  g.AddEdge('MS','MT',10)
  g.AddEdge('PR','MS',10)
  g.AddEdge('RS','PR',10)
  g.AddEdge('SC','RS',10)
  g.AddEdge('SP','SC',20)
  g.AddEdge('SP','RJ',10)
  g.AddEdge('SP','MG',10)
  g.AddEdge('SP','CE',10)
  g.AddEdge('GO','TO',10)
  g.AddEdge('GO','DF',20)
  g.AddEdge('DF','AM',1)
  g.AddEdge('DF','MG',10)
  g.AddEdge('TO','PA',10)
  g.AddEdge('AM','PA',1)
  g.AddEdge('MG','CE',10)
  g.AddEdge('MG','BA',10)
  g.AddEdge('RJ','ES',10)
  g.AddEdge('RJ','DF',10)
  g.AddEdge('BA','SE',10)
  g.AddEdge('BA','PE',10)
  g.AddEdge('SE','AL',10)
  g.AddEdge('AL','PE',10)
  g.AddEdge('CE','MA',10)
  g.AddEdge('CE','RN',10)
  g.AddEdge('MA','PA',10)
  g.AddEdge('PA','PI',3)
  g.AddEdge('PI','PE',3)
  g.AddEdge('CE','PE',10)
  g.AddEdge('RN','PB_JPA',10)
  g.AddEdge('PB_JPA','PB-CGE',10)
  g.AddEdge('PB-CGE','PE',10)

  print (g.MaxFlow('SP', 'PE'))