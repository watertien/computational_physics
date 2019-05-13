import numpy as np
import matplotlib.pyplot as plt 



particle_n = 500 # Particle quantity
n_max = 101 # Max value of quantum number
state = np.ones((particle_n, 3)) 
kinetic = kinetic0 = np.sum(state**2) 
k = 1.
temp = 1e3 # Initial temperature

equilibrium_n = 1000000
energys = np.zeros(equilibrium_n)

dE = 0
for i in range(equilibrium_n):
    # Ensure after n loops, system has been in equilibrium state
    particle = np.random.randint(0, particle_n)
    direction = np.random.randint(0, 3)
    change = np.random.choice([-1, 1])
    if state[particle,direction] > 1 or change > 0:
        dE = 2 * state[particle, direction] * change + 1
        state[particle,direction] += change
        if np.random.random() < np.exp(-dE / k / temp):
            # Accept proposal
            kinetic += dE
    else:
        dE = 0
    energys[i] = dE

plt.plot(kinetic0 + np.cumsum(energys))
plt.show()

