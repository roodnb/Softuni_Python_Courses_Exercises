import os

files = {}
directory = ".\\ex_4"


for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        file, extension = element.split('.')
        if extension not in files:
            files[extension] = []
        files[extension].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)


sorted_files = dict(sorted(files.items(), key=lambda x: (x[0], sorted(x[1]))))

with open(os.path.join(directory, "report.txt"), 'w') as report_file:
    for k, v in sorted_files.items():
        report_file.write(f'.{k}\n')
        for j in v:
            report_file.write(f'- - - {j}\n')
