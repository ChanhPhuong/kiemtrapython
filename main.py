# Doc du lieu tu file input va luu vao list

# shape = []
# def docFile():
#     file = open('input.txt', encoding='utf-8')
#     for line in file:
#         print(line.strip())
#     file.close
# docFile()

from baitap3 import Circle
from baitap3 import Rect
from baitap3 import Triangle

shapes = []
def docfile(file):
    
    with open(file, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            if line == '#Circle':
                banKinh = float(f.readline().strip())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Circle( x, y,banKinh))
            
            elif line == '#Rect':
                rong, dai = map(float, f.readline().strip().split())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Rect( x, y,rong, dai))
            
            elif line == '#Triangle':
                a, b, c = map(float, f.readline().strip().split())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Triangle( x, y,a, b, c))
    return shapes


data = docfile("input.txt")
print(data)

def lietke():
    # Liệt kê hình có chu vi lớn nhất và diện tích lớn nhất
    max_chu_vi = max(shapes, key=lambda x: x.chuVi()).chuVi()
    max_dien_tich = max(shapes, key=lambda x: x.dienTich()).dienTich()
    print(f"Hình có chu vi lớn nhất: {max_chu_vi}")
    print(f"Hình có diện tích lớn nhất: {max_dien_tich}")

lietke()