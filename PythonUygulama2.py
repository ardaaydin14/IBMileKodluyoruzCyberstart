import math

# 2D uzaydaki noktaları temsil eden demetlerden oluşan bir liste oluşturuyoruz
points = [(1, 2), (4, 6), (7, 8), (2, 5)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafeleri saklayacağımız bir liste oluşturuyoruz
distances = []

# Her nokta çifti arasındaki mesafeleri hesaplıyoruz
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Mesafeler listesindeki minimum mesafeyi bulup yazdırıyoruz
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
