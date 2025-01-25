import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

#definindo a função que representa a EDO
def duffing(t, y):
    f, f_prime = y
    f_double_prime = 2 * (1 - f**2) * f_prime - f
    return [f_prime, f_double_prime]

#configurações iniciais
num_points = 50  
points = np.random.uniform(-4, 4, (num_points, 2))
rastro_duracao = 20  #número de frames a serem exibidos na trajetória

#definindo intervalo de tempo para a animação
t_span = (0, 50)
t_eval = np.linspace(*t_span, 500)  

#resolvendo as trajetórias de cada ponto inicial
trajectories = []
for x0, v0 in points:
    sol = solve_ivp(duffing, t_span, [x0, v0], t_eval=t_eval)
    trajectories.append(sol.y)

#criando a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 10))
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor("black")
ax.set_xlabel("f(t)", color="white")
ax.set_ylabel("f'(t)", color="white")
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.tick_params(colors='white')


title = ax.text(-4.5, 4.5, "", color="white", fontsize=14, weight="bold")

#inicializando os pontos e trajetórias
points_plot = ax.plot([], [], 'o', color='white', markersize=2)[0]
lines = [ax.plot([], [], '-', color='green', linewidth=0.5, alpha=0.5)[0] for _ in range(num_points)]

#função de atualização da animação
def update(frame):
    x_data = []
    y_data = []
    for i, traj in enumerate(trajectories):
        #dados dos pontos atuais
        x, y = traj[0, frame], traj[1, frame]
        x_data.append(x)
        y_data.append(y)
        
        #definindo o intervalo da trajetória limitada
        start = max(0, frame - rastro_duracao)
        lines[i].set_data(traj[0, start:frame], traj[1, start:frame])
        
    #atualizando os pontos
    points_plot.set_data(x_data, y_data)
    return [points_plot] + lines

#criando a animação
ani = FuncAnimation(fig, update, frames=len(t_eval), blit=True)

#salvando o GIF (ou use plt.show() para exibir diretamente)
ani.save("Orbit_Attractor.gif", writer="imagemagick", fps=20, dpi=800)

#plt.show()
