#fungsi utama
def myConvexHull(points):
    solutionleft = []
    solutionright = []
    solution = []
    sortedPoints = sorted(points, key=lambda row: (row[0], row[1]))
    leftpoints = []
    rightpoints = []
    a = sortedPoints[0]
    b = sortedPoints[-1]

    for i in range(len(sortedPoints)):
        det = determinan(sortedPoints[i], a, b)
        if (det > 0):
            leftpoints.append(sortedPoints[i])
        elif (det < 0):
            rightpoints.append(sortedPoints[i])

    #titik paling kiri sebagai solusi
    solution.append(a)   
    convex_hull(leftpoints, b, a, solutionleft) #divide and conquer bagian kiri dari garis utama
    solutionleft.sort(key=lambda row: (row[0], row[1])) #susun titik-titik pembentuk convexhull atas untuk memudahkan visualisasi
    solution += solutionleft #masukkan titik2 solusi bagian atas ke himpunan solusi utama

    solution.append(b)

    convex_hull(rightpoints, a, b, solutionright)
    solutionright.sort(key=lambda row: (row[0], row[1]), reverse=True)#susun titik-titik pembentuk convexhull bawah untuk memudahkan visualisasi
    solution += solutionright #masukkan titik2 solusi bagian atas ke himpunan solusi utama
    solution.append(a) #append titik awal lagi supaya memudahkan visualisasi

    return solution


def determinan(p3,p1, p2):   
    #mencari determinan untuk menentukan apakah p3 berada di atas garis atau di bawah garis
    x1, y1 = p1
    x2, y2 = p2
    #ax + by + c
    x3, y3 = p3
    return (x2*y3-x3*y2)-(x1*y3-x3*y1)+(x1*y2-x2*y1)



def get_farthest_point(area, p1, p2):
    #mencari titik terjauh dari di area "area" dari garis ab
    farthest_dist = -1
    C = None
    for p3 in area:
        # print(p3)
        f = abs((p2[0]-p1[0])*(p1[1]-p3[1])-(p1[0]-p3[0])*(p2[1]-p1[1]))
        # print(f)
        if f>farthest_dist:
            farthest_dist = f
            C = p3
    # print(C)
    # print()
    return C

#fungsi convexhull rekursif 
def convex_hull(area, a , b, solution):

    #jika tidak ada titik yang merupakan area maka 
    if len(area) == 0:
        return 
    else:
        #cari titik terjauh dari garis ab

        c = get_farthest_point(area, a, b)
        # print(c)
        # print(determinan(c, a, b))
        
        #masukkan titik c ke himpunan solusi

        solution.append(c)

    
        #divide masalah dengan garis ac dan cb
        ac_right = []
        cb_right = []
        for point in area:
            if determinan(point, a, c) < 0:
                ac_right.append(point)
            if determinan(point, c, b) < 0:
                cb_right.append(point)

        #Proses rekursif 
        convex_hull(ac_right, a, c, solution)
        convex_hull(cb_right, c, b, solution)
