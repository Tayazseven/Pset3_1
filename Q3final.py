import sys
seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
dict={}
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line !='\n': #skips empty lines and
            line = line.strip()
        if line.startswith(">"):
            seqname = line[1:]
            if seqname  not in dict:
                dict[seqname] = []
            continue
        sequence = line
        dict[seqname].append(sequence) ##pu the sequences into dictonarys as keys

        reads = set(sys.argv[2])
        if set(reads).issubset(dict):  # looks for the specific matches which is given in the command line
            print('match found: ' + reads)
        else:
            return None
        ofile = sys.argv[3]
        with open(ofile,
                  "w") as f1:  # creates a file and writes the name of the sequence, the searched string and the line where the match found
            f1.write(seqname + '\n' + reads + 'match found; ')

            ##Time complexitiy of Hashing mapping is 10 times faster than mapping regularly

