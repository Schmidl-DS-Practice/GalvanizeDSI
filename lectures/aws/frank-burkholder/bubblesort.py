import argparse
import numpy as np

def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input_file", required=True, help="name of input file")
    ap.add_argument("-o", "--output_file", required=True, help="name of output file")
    args = vars(ap.parse_args())

    lst = np.loadtxt(args['input_file'], dtype=int)
    np.savetxt(args['output_file'], bubblesort(lst), fmt="%d")
