# testingout max filter
from scipy import ndimage, misc
import matplotlib.pyplot as plt
fig = plt.figure()
plt.gray()  # show the filtered result in greyscale
ax1 = fig.add_subplot(121) #lhs
ax2 = fig.add_subplot(122) #rhs
ascent = misc.ascent() #random images lol
result = ndimage.maximum_filter(ascent,size=20)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()
