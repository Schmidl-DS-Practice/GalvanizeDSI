import numpy as np

def plot_distances(ax, x_data, y_data, c, x_target, y_target):
    '''
    Plots the data and the distance between the points and the the target.
    '''
    ax.scatter(x_data, y_data)
    ax.scatter([x_target],[y_target],s=[170], marker='x')
    ax.set_xlabel('% Class Attended')
    ax.set_ylabel('Hours of Study')
    ax.set_title('Score on Exam')

    for i, txt in enumerate(c):
        ax.annotate(str(txt), (x_data[i], y_data[i]), fontsize=12)
        
    for x,y in zip(x_data, y_data):
        dist = np.linalg.norm(np.array([x,y])-np.array([x_target, y_target]))
        ax.plot([x_target, x], [y_target, y], label='Dist: {0:.3f} '.format(dist))
        
    ax.legend()
