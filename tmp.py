import glob
from os.path import join

root = '/home/00Dataset/Detection/labels'
dir = 'test', 'train', 'val'

txt_file = join(root, '*', '*.txt')
i = 0
for path in glob.glob(txt_file):

    with open(path, 'r') as f:
        context = f.readlines()
    for index in range(len(context)):
        if context[index][0] == '2':
            context[index] = '1' + context[index][1:]

    with open(path, 'w') as f:
        f.writelines(context)
    print(i)
    i+=1
