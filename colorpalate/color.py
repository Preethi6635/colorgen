from colorthief import ColorThief
import matplotlib.pyplot as plt
ct=ColorThief("img1.jpg")
dom_color=(ct.get_color(quality=1))
plt.imshow([[dom_color]])

palette=ct.get_palette(color_count=10)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()