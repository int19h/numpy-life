import life
import matplotlib.pyplot as plt
import matplotlib.animation as plt_anim

b = life.board(200, 100)
life.emplace(b, (3, 5), life.glider)
life.emplace(b, (30, 30), life.pulsar)

fig, ax = plt.subplots()
im = ax.imshow(b, animated=True, interpolation='nearest')

plt_anim.FuncAnimation(fig, lambda b: im.set_array(b), frames=life.life(b), interval=0)
plt.show()
