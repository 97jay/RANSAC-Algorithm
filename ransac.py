import random
def solution(input_points, t, d, k):
    """
    :param input_points:
           t: t is the perpendicular distance threshold from a point to a line
           d: d is the number of nearby points required to assert a model fits well, you may not need this parameter
           k: k is the number of iteration times
           Note that, n for line should be 2
           (more information can be found on the page 90 of slides "Image Features and Matching")
    :return: inlier_points_name, outlier_points_name
    inlier_points_name and outlier_points_name is two list, each element of them is str type.
    For example: If 'a','b' is inlier_points and 'c' is outlier_point.
    the output should be two lists of ['a', 'b'], ['c'].
    Note that, these two lists should be non-empty.
    """
    random.seed(20)
    mini=9999999
    list1=[]
    inner=[]
    inner1=[] 
    outer=[]
    max_in=0
    outer1=[]
    for i in range(k):
        s=random.sample(input_points,2)
        if s not in list1:
            list1.append(s)
            if((s[1]['value'][0]-s[0]['value'][0])!=0):
                m1=(s[1]['value'][1]-s[0]['value'][1])/(s[1]['value'][0]-s[0]['value'][0])
            else:
                m1=0
            cval1=s[1]['value'][1]-(m1*s[1]['value'][0])
            avg=0
            for z in range(len(input_points)):
                point=input_points[z]
                if point in s:
                    continue
                if(m1==0):
                    m2=0
                else:
                    m2=-1/m1
                cval2=point['value'][1]-(m2*point['value'][0])
                if(m1-m2==0):
                    x1=0
                else:
                    x1=(cval2-cval1)/(m1-m2)
                y1=(m1*x1)+cval1
                d=((x1-point['value'][0])**2 + (y1-point['value'][1])**2)**0.5
                if(d<=t):
                    avg+=d
                    inner1.append(point['name'])
                else:
                    outer1.append(point['name'])
            if(len(inner1)>0):
               avg/=len(inner1)
            else:
                avg=0
            inner1.append(s[0]['name'])
            inner1.append(s[1]['name'])
            if(len(inner1)>=max_in):
                if((len(inner1)>=(d+2)) and(avg<mini)):
                    mini=avg
                    max_in=len(inner1)
                    outer=outer1
                    inner=inner1
            outer1=[]
            inner1=[] 
    return inner,outer


if __name__ == "__main__":
    input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},
                    {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},
                    {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},
                    {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]
    t = 0.5
    d = 3
    k = 100
    inlier_points_name, outlier_points_name = solution(input_points, t, d, k)  # TODO
    assert len(inlier_points_name) + len(outlier_points_name) == 8  
    f = open('./task1_result.txt', 'w')
    f.write('inlier points: ')
    for inliers in inlier_points_name:
        f.write(inliers + ',')
    f.write('\n')
    f.write('outlier points: ')
    for outliers in outlier_points_name:
        f.write(outliers + ',')
    f.close()


