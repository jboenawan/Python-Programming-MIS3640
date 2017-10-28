def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source = open(source)
    file2 = open(dest, 'w')
    for line in f_source:
        new_line = line.replace(pattern,replace)
        file2.write(new_line)
    f_source.close()
    file2.close()



pattern = 'Hey Jude'
replace = 'Hi Donald'
source = 'sed_tester.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)



