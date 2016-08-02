def gen_file(size):
    file = open(str(size) + "M.data", "w")
    file.seek(size * 1024 * 1024 - 1)

    file.write('\0')
    print('str(size) + "M.data"')

    file.close()


# size_mb = input('Input the file size you want (/MB)')
#
# if not isinstance(size_mb, int):
#     print('Error Input:  ')
# else:
#     gen_file(size_mb)
