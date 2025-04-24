# Check if you are better than the class average

def better_than_average(class_points, your_points):
    return True if (sum(class_points))/len(class_points) < your_points else False
