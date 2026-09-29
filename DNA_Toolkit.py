Nucleotide = {"A", "T", "C", "G",}

def validate_seq(DNA_seq):
   clean_seq = DNA_seq.replace(" ", "").replace("\n", "").replace("\r", "").upper()
   temp_seq = DNA_seq.upper()
   for nuc in temp_seq:
      if nuc not in Nucleotide:
         return False
      return temp_seq

def count_nucleotides(count_seq):
   count_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
   for nuc in count_seq:
      if nuc in Nucleotide:
         count_dict[nuc] += 1
   return count_dict

def GC_content(DNA_seq):
   DNA_seq = DNA_seq.upper()
   gc_count = DNA_seq.count("G") + DNA_seq.count("C")
   if len(DNA_seq) > 0:
    return (gc_count / len(DNA_seq)) * 100 
   else: 
      return 0

def transcribe(DNA_seq):
   DNA_seq = DNA_seq.upper()
   return DNA_seq.replace("T", "U").replace("t","u")

mapping = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
    'a': 't', 't': 'a', 'c': 'g', 'g': 'c',
    ' ': ' ' 
}

def reverse_complement(DNA_seq):
   DNA_seq = DNA_seq.upper()
   DNA_seq = "".join(mapping[nuc] for nuc in DNA_seq)[::-1]
   return DNA_seq

def find_pattern(DNA_seq, pattern):
   DNA_seq = DNA_seq.upper()
   pattern = pattern.upper()
   position = []
   seq_len = len(DNA_seq)
   pat_len = len(pattern)
   for i in range(seq_len-pat_len + 1):
      if DNA_seq[i:i + pat_len]== pattern:
         position.append((i, i + pat_len))
   return position

CODON_TABLE = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "_", "TAG": "_", "TGA": "_",
}

AMINO_ACID_NAMES = {
    "A": "Alanine",       "R": "Arginine",      "N": "Asparagine",
    "D": "Aspartic acid", "C": "Cysteine",     "Q": "Glutamine",
    "E": "Glutamic acid", "G": "Glycine",      "H": "Histidine",
    "I": "Isoleucine",    "L": "Leucine",      "K": "Lysine",
    "M": "Methionine",    "F": "Phenylalanine","P": "Proline",
    "S": "Serine",        "T": "Threonine",    "W": "Tryptophan",
    "Y": "Tyrosine",      "V": "Valine",       "_": "STOP"
}

def translate(DNA_seq, init_pos = 0):
   DNA_seq = DNA_seq.upper()
   protein= []
   for i in range(init_pos, len(DNA_seq)-2, 3):
      codon = DNA_seq[i:i+3]
      if codon in CODON_TABLE:
         aa_name = CODON_TABLE[codon]
         amino_acid = AMINO_ACID_NAMES[aa_name]
      else:
         amino_acid = "unknown"

      protein.append(amino_acid)
   return protein

def all_reading_frames(DNA_seq):
   forward_frames = []
   for pos in range(0,3):
      frame = translate(DNA_seq, init_pos=pos)
      forward_frames.append(frame)
   rev_seq = reverse_complement(DNA_seq)
   reverse_frames = []
   for pos in range(0,3):
      frame = translate(rev_seq, init_pos = pos)
      reverse_frames.append(frame)
   return{"forward": forward_frames, "reverse": reverse_frames}

def read_fasta(file_path):
   sequence = {}
   currennt_header = ''
   file = open(file_path,'r')
   for line in file:
      clean_line = line.strip()
      if clean_line == '':
       continue
      if clean_line[0] == '>':
         currennt_header = clean_line[1:]
         sequence[currennt_header] = ''
      else:
         sequence[currennt_header] += clean_line.upper()
   file.close()
   return sequence

   
