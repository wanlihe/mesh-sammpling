import numpy as np
import matplotlib.pyplot as plt


def main():
    model1_disp_2336 = np.loadtxt('result/modelI/gdisplac.node2336') #z
    model1_disp_2360 = np.loadtxt('result/modelI/gdisplac.node2360') #y
    model1_velo_2336 = np.loadtxt('result/modelI/gvelocit.node2336')  # z
    model1_velo_2360 = np.loadtxt('result/modelI/gvelocit.node2360')  # y

    model2_disp_2336 = np.loadtxt('result/modelIII.post/gdisplac.node2336')  # z
    model2_disp_2360 = np.loadtxt('result/modelIII.post/gdisplac.node2360')  # y
    model2_velo_2336 = np.loadtxt('result/modelIII.post/gvelocit.node2336')  # z
    model2_velo_2360 = np.loadtxt('result/modelIII.post/gvelocit.node2360')  # y

    plt.figure(1)
    plt.plot(model1_disp_2336[:, 0], model1_disp_2336[:, 3], color='k', label='Model I')
    plt.plot(model2_disp_2336[::500, 0], model2_disp_2336[::500, 3],
             color='r', linestyle='None', marker='s', label='Model II')
    plt.xlabel(r'Time [s]', fontsize=16)
    plt.ylabel(r'z-displacement [mm]', fontsize=16)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.legend(loc='lower right', fontsize=16)
    plt.savefig('disp_2336.png')

    plt.figure(2)
    plt.plot(model1_disp_2360[:, 0], model1_disp_2360[:, 2], color='k', label='Model I')
    plt.plot(model2_disp_2360[::500, 0], model2_disp_2360[::500, 2],
             color='r', linestyle='None', marker='s', label='Model II')
    plt.xlabel(r'Time [s]', fontsize=16)
    plt.ylabel(r'y-displacement [mm]', fontsize=16)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.legend(loc='lower right', fontsize=16)
    plt.savefig('disp_2360.png')

    plt.figure(3)
    plt.plot(model1_velo_2336[:, 0], model1_velo_2336[:, 3], color='k', label='Model I')
    plt.plot(model2_velo_2336[::500, 0], model2_velo_2336[::500, 3],
             color='r', linestyle='None', marker='s', label='Model II')
    plt.xlabel(r'Time [s]', fontsize=16)
    plt.ylabel(r'z-velocity [mm/s]', fontsize=16)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.legend(loc='upper right', fontsize=16)
    plt.savefig('velo_2336.png')

    plt.figure(4)
    plt.plot(model1_velo_2360[:, 0], model1_velo_2360[:, 2], color='k', label='Model I')
    plt.plot(model2_velo_2360[::500, 0], model2_velo_2360[::500, 2],
             color='r', linestyle='None', marker='s', label='Model II')
    plt.xlabel(r'Time [s]', fontsize=16)
    plt.ylabel(r'y-velocity [mm]', fontsize=16)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.legend(loc='upper right', fontsize=16)
    plt.savefig('velo_2360.png')


    # print(model1_disp_2336)

if __name__ == '__main__':
    main()