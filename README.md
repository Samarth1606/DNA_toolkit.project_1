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


## Requirements

### Functional Requirements
* **FASTA File Parsing:** Ability to read and process raw DNA sequences from standard `.fasta` files.
* **DNA Validation:** Verifies input sequence validity to filter out non-nucleotide characters.
* **Sequence Analysis:** Calculates nucleotide counts and GC percentage.
* **Genetic Operations:** Performs transcription (DNA to RNA), translation to amino acids, reverse complements, and 6-frame translation.
* **Pattern Matching:** Searches and locates specific codon patterns within sequences.

### Non-Functional Requirements
* **Performance:** Rapid processing of sequence data with minimal execution delay.
* **Robustness:** Built-in error handling for invalid sequence characters or missing files.
* **Modularity:** Separation of core analysis functions (`DNA_Toolkit.py`) from the user interface (`Main.py`).

## How to Run the Tool

1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. Open your terminal or command prompt in the project directory.
4. Execute the main program:

```bash
python Main.py
