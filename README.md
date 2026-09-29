# DNA Toolkit Project
Project based on Bioinformatics showcasing a DNA reading toolkit

***Validation of DNA sequence:*** validates the DNA sequence if given manually or if through different FASTA formats, so that no other character breaks the code
***metrices of nucleotides and GC percentage:*** counts the number of each nucleotide and also calculates percentage of Guanine and Cytosine contents.
***Transcription and Translation:*** transcribes the given DNA to RNA and then the code translates it all into Amino acid groups
***Reverse compliments:*** Finds compliments of the given DNA sequences so that we can know what code binds to the other
***6 Frame Translation:*** Translates sequences across all 3 forward (+) and 3 reverse (-) reading frames.
***Pattern Matching:*** Locates specific codons given and finds their indices
***Multiple Formats Supported:*** Multiple FASTA formats are supported in the code(`.fasta`, `.fa`, `.txt`) or we can manually add DNA sequences
## System Workflow

```mermaid
flowchart TD
    A[Start Program] --> B{Choose Input Mode}
    B -->|1: Manual| C[Prompt for Raw DNA Sequence]
    B -->|2: FASTA File| D[Read & Parse sample.fasta]
    C --> E[Validate Sequence]
    D --> E
    E -->|Valid| F[Run Toolkit Modules]
    E -->|Invalid| G[Display Error & Exit]
    F --> H[Output: Nucleotide Counts, GC Content, Transcription, Translation, Reading Frames]

