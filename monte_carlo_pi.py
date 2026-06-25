import numpy as np
import matplotlib.pyplot as plt

# function of creat estimate point and calculate inside the circle
def estimate_pi(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    inside = (x - 0.5)**2 + (y - 0.5)**2 <= (0.5)**2
    count_inside = np.sum(inside)
    pi_est = 4 * count_inside / n
    return pi_est, x, y, inside


# calculate Estimated π
n = 5000
pi_est, x, y, inside = estimate_pi(n)

print("Estimated π:", pi_est)

#compare with real π
real_pi = np.pi
error = abs(pi_est - real_pi)

print("Real π:", real_pi)
print("Error:", error)


# Effect of number of points
print("\nEffect of number of points:")
n_values = [100, 1000, 5000, 10000, 50000]
errors = []

for n_test in n_values:
    pi_test, _, _, _ = estimate_pi(n_test)
    err = abs(pi_test - real_pi)
    errors.append(err)
    print(f"{n_test} points → π ≈ {pi_test:.6f} | Error = {err:.6f}")


# point Inside / outside Circle
plt.figure()
plt.scatter(x[inside], y[inside], label="Inside Circle")
plt.scatter(x[~inside], y[~inside], label="Outside Circle")

circle = plt.Circle((0.5, 0.5), 0.5, fill=False)
plt.gca().add_patch(circle)

plt.title(f"Monte Carlo Simulation (π ≈ {pi_est:.5f})")
plt.gca().set_aspect('equal')
plt.legend()
plt.grid()


# Effect of Number of Points on π Estimation
plt.figure()
plt.plot(n_values, errors, marker='o')
plt.xlabel("Number of Points")
plt.ylabel("Error")
plt.title("Effect of Number of Points on π Estimation Accuracy")
plt.grid()

plt.show()