# -*- coding: utf-8 -*-

# import matplotlib.font_manager as fm
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
# # font_name = font_manager.FontProperties(fname="/Users/wonjunhui/Library/Fonts/NANUMBARUNGOTHIC_1.TTF").get_name()
# # rc('font', family=font_name)
# path = '/Users/wonjunhui/Library/Fonts/NANUMBARUNGOTHIC_1.TTF'
# fontprop = fm.FontProperties(fname=path, size=18)
# y1_value = (76.0,83.0,65.0,75.0,81.0,68.0,63.0,69.0,74.0,41.0,65.0,59.0,44.0,58.0,40.0,37.0,35.0)
# x_name=('서울','경기','인천','강원','세종','충북','충남','대전','경북','경남','대구','울산','부산','전북','전남','광주','제주')
# n_groups = len(x_name)
# index = np.arange(n_groups)
#
# plt.bar(index, y1_value, tick_label=x_name, align='center')
#
# plt.xlabel('도시', fontproperties=fontprop)
# plt.ylabel('average rainfall (mm)')
# plt.title('Weather Bar Chart')
# plt.xlim( -1, n_groups)
# plt.ylim( 0, 100)
# plt.show()




import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="/Users/wonjunhui/Library/Fonts/NANUMBARUNGOTHIC_1.TTF").get_name()
rc('font', family=font_name)
style.use('ggplot')

industry = ['서울','경기','인천','강원','세종','충북','충남','대전','경북','경남','대구','울산','부산','전북','전남','광주','제주']
fluctuations = [76, 83, 65, 75, 81, 68, 63, 69, 74, 41, 65, 59, 44, 58, 40, 37, 35]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ypos = np.arange(17)
rects = plt.bar(ypos, fluctuations, align='center', width=0.5, color = 'b')
for j in range(0,len(fluctuations)):
    if fluctuations[j] > 60:
        rects[j].set_color('#ff5959')
# rects[0].set_color('b')
plt.xticks(ypos, industry)

for i, rect in enumerate(rects):
    ax.text(rect.get_x() + rect.get_width() / 2.0, 1.01 * rect.get_height(), str(fluctuations[i]), ha='center')
    # ax.text(str(fluctuations[i]))
plt.ylabel('미세먼지농도')
plt.xlabel('도시')
plt.savefig("/Users/wonjunhui/Desktop/test_figure1.png")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Make a fake dataset
# height = [3, 12, 5, 18, 45]
# bars = ('A', 'B', 'C', 'D', 'E')
# y_pos = np.arange(len(bars))
#
# barlist = plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'cyan'])
# # barlist[0].set_color('r')
# for i in range(0,len(height)):
#     if height[i] == 3:
#         barlist[i].set_color('r')
# plt.xticks(y_pos, bars)
# plt.show()

# barlist=plt.bar([1,2,3,4], [1,2,3,4])
# barlist[0].set_color('r')
# print(str(len(barlist)))
# for i in range(0,len(barlist)):
#     print(barlist[i])
    # print(str(i))
# barlist[0].set_color('r')
# plt.show()