import random

def a(num_points):

    points_inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 < 1:
            points_inside_circle += 1
    
    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation

if __name__ == "__main__":
    print("Calculate Pi Approximation")
    num_points = int(input("Type in the number of random points to generate: "))
    pi_approx = a(num_points)
    print(f"Approximation of pi with {num_points} points: {pi_approx}")
    print(f"Actual value of pi: {3.14159265359}")
