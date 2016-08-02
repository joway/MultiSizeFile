from gen_fixed_size_file import gen_file

size_box = [1, 5, 10, 20, 50, 100, 150, 200, 250, 300, 500, 1000, 1500, 2000]

for size in size_box:
    gen_file(size)
