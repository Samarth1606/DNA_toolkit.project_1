from DNA_Toolkit import (validate_seq, 
                         count_nucleotides, 
                         GC_content, 
                         transcribe, 
                         reverse_complement, 
                         find_pattern,
                         translate,
                         all_reading_frames,
                         read_fasta)


print("=== DNA SEQUENCE ANALYSIS TOOLKIT ===")
print("1. Enter sequence manually")
print("2. Read from FASTA file")
choice = input("Choose option (1 or 2): ").strip()
sequences = {}
if choice == '1':
  raw_input = input("Enter a DNA sequence: ")
  sequences["Manual Input"] = raw_input
elif choice == '2':
  file_path = input("Enter path to FASTA file (e.g. sample.fasta): ").strip()
  sequences = read_fasta(file_path)
else:
  print("Invalid Option")
  exit()


for header, raw_seq in sequences.items():
    print(f"\n==========================================")
    print(f" PROCESSING: {header}")
    print(f"==========================================")
    DNA_seq = raw_seq.replace(' ','').replace('\n','').replace('\t','').replace('\r','').upper()
    display_seq = raw_seq.strip()
    test = validate_seq(DNA_seq)
    if test:
        print("Validation: PASSED")
        target = input("Enter your target codon: ")
        counts = count_nucleotides(test)
        content = GC_content(test)
        RNA_seq = transcribe(display_seq)
        matches = find_pattern(test, target)
        protein_seq = translate(display_seq)
        print("Nucleotide counts:", counts)
        print("GC Content:", content)
        print("RNA sequence:", RNA_seq)
        print("Reverse Complement:", reverse_complement(display_seq))
        print(f"Pattern '{target.upper()}' found at indices: {matches}")
        print(f"translated protein: {protein_seq}")
        print("\n--- Reading Frames (6-Frame Translation) ---")
        all_frames = all_reading_frames(DNA_seq)

        print("\nForward Strand (+):")
        for i, frame in enumerate(all_frames["forward"]):
            print(f"  Frame +{i + 1} (Start {i}): {frame}")

        print("\nReverse Strand (-):")
        for i, frame in enumerate(all_frames["reverse"]):
            print(f"  Frame -{i + 1} (Start {i}): {frame}")
    else:
        print("Validation: FAILED")





