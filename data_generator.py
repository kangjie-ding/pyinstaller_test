# working institution:School of Mathematical Sciences,Zhejiang University
# author:Kangjie Ding
# date:2024/5/17 10:19
import numpy as np
import os
import random


def data_generate(plant_num):
    """
    将植株数据存储到csv文件中
    :param plant_num: 植株数量
    """
    heights = [10*random.random() for i in range(plant_num)]
    leaf_nums = [random.randint(1, 50) for i in range(plant_num)]
    statistic_data = np.zeros((plant_num, 102))
    statistic_data[:, 0] = heights
    statistic_data[:, 1] = leaf_nums
    for i in range(plant_num):
        for j in range(leaf_nums[i]):
            area, angle = 10*random.random(), random.randint(1, 90)
            statistic_data[i][j+2] = area
            statistic_data[i][j+52] = angle
    np.savetxt("statistic_data.csv", statistic_data, delimiter=',')


def data_process(file, save_folder):
    with open(file, 'r') as file_in:
        content = file_in.read()
    write_path = os.path.join(os.getcwd(), save_folder, file.split('\\')[-1])
    with open(write_path, 'w') as file_out:
        file_out.write(content)

