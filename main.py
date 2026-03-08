import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from skimage.data import shepp_logan_phantom
from geometry import Circle, Point, Segment

center = Point(200, 200)
circle = Circle(center=center, radius=200)
phantom = shepp_logan_phantom()
phantom[150:170, 200:220] = 1.5
theta = np.linspace(0, np.pi*2, 180)
xdata, ydata = [], []

fig,axs=plt.subplots(1,3, figsize=(20, 6))
ln, = axs[0].plot([], [])
point, = axs[0].plot([], [], 'ro', markersize=8)
sgm, = axs[0].plot([], [], color='green')

plt.tight_layout(pad=2.2)
for ax in axs:
    ax.set_xlim(-100,500)
    ax.set_ylim(-100,500)
    ax.axis('equal')

#до обработки
def init():
    axs[0].set_title('до обработки')
    return ln,

#после обработки
axs[1].set_title('обработано')

#оригинал
axs[2].imshow(phantom, cmap='gray')
axs[2].set_title('оригинал')

def update(frame):
    x_p = circle.center.x + circle.radius * np.cos(frame)
    y_p = circle.center.y + circle.radius * np.sin(frame)
    r_x_p = circle.center.x - circle.radius * np.cos(frame)
    r_y_p = circle.center.y - circle.radius * np.sin(frame)
    xdata.append(x_p)
    ydata.append(y_p)
    sgm.set_data([x_p, r_x_p], [y_p, r_y_p])
    point.set_data([x_p],[y_p])
    ln.set_data(xdata, ydata)
    return ln, point, sgm

print(phantom)
print(phantom.shape)
ani = FuncAnimation(fig, update, frames=theta, interval=50,
                    init_func=init, blit=True, repeat=False)
plt.show()