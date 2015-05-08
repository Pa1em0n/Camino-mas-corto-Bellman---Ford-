#datos del Arbol.
vertices = {1:0,2:1,3:2,4:3,5:4,6:5}
aristas = [[1,2],[1,3],[1,4],[3,4],[4,5],[4,6],[5,6]]
pesos = [1,2,4,3,5,2,4]

#Arreglos de la tabla.
inf = float("inf")
distancia = [inf,inf,inf,inf,inf,inf]
previo = [0,0,0,0,0,0]

distancia[0] = 0

for v,i in vertices.items():
    print "\niteracion: "+ str(i)+"\nTabla resultado:"     
    for e in range(0,len(aristas)):
        if ( aristas[e][0] == v):
            adyacente = vertices[aristas[e][1]]
            p = pesos[e]   
        if((distancia[i] + p) < distancia[adyacente]): #peso actual + peso arista < peso adyacente  
            distancia[adyacente] = distancia[i] + p #peso adyacente  =  peso actual + peso.
            previo[adyacente] = v # previo del adyacente = vertice actual.
            print "Arista: "+ str(aristas[e])+"\nVertices: " + str(vertices)+"\nDistancia(costo): " + str(distancia)+"\nprevio: "+str(previo) 
            
def imprime(destino):          
    if(previo[vertices[destino]] != 0):
        imprime(previo[vertices[destino]]) #se imprime recursivamente los vertices previos, al vertice destino.
    print destino

#print "\nTabla resultado:\n Vertices: " + str(vertices) + "\nDistancia(costo): " + str(distancia)+"\nprevio: "+str(previo) 
print "Lista de vertices que componen el camino mas corto, con menos costo"
imprime(6)
                
                
