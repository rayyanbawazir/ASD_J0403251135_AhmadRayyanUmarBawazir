#================================
# Praktikum 11 - Adjacency Matrix
# Nama: Ahmad Rayyan Umar Bawazir
# NIM: J0403251135
#================================   
# adjacency matrix for the graph:
print("Adjacency Matrix for the graph:")

nodes = [0, 1, 2, 3]
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
]
# Build adjacency matrix
size = len(nodes)
adj_matrix = [[0] * size for _ in range(size)]
for a, b in edges:
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1

print("Adjacency Matrix (4 nodes: 0, 1, 2, 3)")
print("   " + " ".join(str(node) for node in nodes))
for i, row in enumerate(adj_matrix):
    print(f"{i}: " + " ".join(str(value) for value in row))

print("\nRow meanings:")
for i, row in enumerate(adj_matrix):
    connected = [str(j) for j, value in enumerate(row) if value == 1]
    if connected:
        print(f"Node {i} terhubung dengan: {', '.join(connected)}")
    else:
        print(f"Node {i} tidak terhubung dengan node lain")


#================================
# Praktikum 11 - Adjacency List
#================================
print("\nAdjacency List:")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, "->", graph[node])
    

#======================================
# Praktikum 11 - Convert Matrix to List
#======================================
print("\nConvert Adjacency Matrix to Adjacency List:")

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

adj_list = {}

for i in range(len(matrix)):
    adj_list[i] = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

print(adj_list)

#PENJELASAN KETIGA PROGRAM
print("""
Penjelasan Program: 
1. Adjacency Matrix
Program membuat graph menggunakan matrix 4x4. 
Angka 1 menunjukkan adanya hubungan antar node, sedangkan 0 berarti tidak ada hubungan.
2. Adjacency List
Graph direpresentasikan dalam bentuk daftar tetangga. 
Setiap node menyimpan node lain yang terhubung langsung dengannya.
3. Convert Matrix to List
Program mengubah adjacency matrix menjadi adjacency list dengan membaca setiap nilai pada matrix. 
Jika bernilai 1, maka node dianggap terhubung dan dimasukkan ke adjacency list.
""")    

# Nama File: Pertemuan11_AhmadRayyanUmarBawazir_J0403251135.py

# 1. Adjacency List
graph = {
    "Rumah": ["Sekolah", "Pasar"],
    "Sekolah": ["Rumah", "Taman", "Kantor"],
    "Pasar": ["Rumah", "Kantor"],
    "Taman": ["Sekolah", "Kantor"],
    "Kantor": ["Sekolah", "Pasar", "Taman"]
}

# 2. Adjacency Matrix
# Urutan: Rumah(0), Sekolah(1), Pasar(2), Taman(3), Kantor(4)
matrix = [
    [0, 1, 1, 0, 0], # Rumah
    [1, 0, 0, 1, 1], # Sekolah
    [1, 0, 0, 0, 1], # Pasar
    [0, 1, 0, 0, 1], # Taman
    [0, 1, 1, 1, 0]  # Kantor
]

def tampilkan_output():
    print("=== REPRESENTASI GRAPH PETA KOTA ===")
    
    print("\n1. Adjacency List:")
    for node, neighbors in graph.items():
        print(f"{node} terhubung ke: {', '.join(neighbors)}")
        
    print("\n2. Adjacency Matrix:")
    for row in matrix:
        print(row)
        
    print("\n3. Daftar Node:")
    print(list(graph.keys()))
    
    print("\n4. Hubungan Antar Node (Edges):")
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            # Memastikan edge tidak duplikat untuk tampilan undirected
            if {node, neighbor} not in edges:
                edges.append({node, neighbor})
                print(f"{node} <---> {neighbor}")

if __name__ == "__main__":
    tampilkan_output()