import sys
seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line !='\n': #skips empty lines and
            line = line.strip()#removes new line character(\n)
        if line.startswith('>'):
            seqname= line
        else:
            #print seqname for fastq files
            b =  ''.join(seq_dict[base] for base in reversed(line[::-1]))# remove the comment if you would like to check the reverse complement
            #print(b) uncommand it if you would like to see the reverse complement

        reads=set(sys.argv[2])
        if set(reads).issubset(line): #looks for the specific matches which is given in the command line
            print ('match found: ' +str(len(line)))
        else:
            return None
        ofile=sys.argv[3]
        with open(ofile, "w") as f1: #creates a file and writes the name of the sequence, the searched string and the line where the match found
            f1.write(seqname + '\n' + reads + 'match found; ' + line)