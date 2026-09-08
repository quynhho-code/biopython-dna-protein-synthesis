# biopython-dna-protein-synthesis
# Description:
Manually download a random DNA sequence. Build a Python script to clean and parse the raw data, calculate GC content, and transcribe the sequence to an mRNA strand. Utilize Biopython to translate the strand and synthesize protein
# Core Workflow:
Random DNA sequence
-> Clean and parse the sequence
-> Calculate GC content
-> Transcribe into mRNA strand
-> Translate mRNA into protein sequence 
-> Display results.
## Workflow:
1. Input DNA: The program receives a DNA sequence.
2. Clean sequence: Use a python script to remove hidden or invalid spaces and characters.
3. GC content: Calculate G and C nucleotides, and GC content and their percentage.
4. Transcription: Convert the DNA sequence into an mRNA strand.
5. Translation: Convert the mRNA strand into a protein sequence using Biopython to produce 2 protein sequences: one that stops at the first stop codon and one that continues through the remaining sequence, including region after the first stop codon.
6. Output: Display the analyzed results.
# Prerequisites:
This project requires Python 3 and the Biopython library.
## Installation:
Install Biopython using pip:
pip3 install biopython
# How to run:
1. Place your raw FASTA text file containing DNA sequence ("DNA.fasta.txt") in the same folder of the python script.
2. Run the pipeline script: python ProteinSynthesis.py
# Example:
1. Input: ATCGATCGAT
2. Output:
G content: 2
% G content: 10%
C content: 2
% C content: 10%
Total GC content: 4
% GC content: 20%
mRNA: AUGCAUGCAU
Protein: ...
# What I learned:
Through this project, I've learned:
- Python and Biopython programming
- Cleaning and parsing raw data
- Central Dogma analysis (transcription & translation)
- Basic DNA and gene analysis
# Future Improvements:
- Analyze multiple DNA sequences
- Use real DNA sequences
- Write python script to find Open Reading Frame
# Technologies:
- Python/Biopython
- Git/GitHub
