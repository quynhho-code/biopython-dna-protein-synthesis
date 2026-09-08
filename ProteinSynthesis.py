"""
Project: DNA Sequence Cleaner and Parser & Protein Synthesizer
Description: Clean a raw random DNA sequence FASTA text file, calculates GC content, transcribes into an mRNA strand, and translates the mRNA strand into a protein sequence.
Author: Quynh Ho
"""

with open("DNA.fasta.txt", "r") as file:
    header = ""
    DNA_strand = ""

    for line in file:
        line = line.strip()
        if line.startswith(">"):
            header = line[1:]
        else:
            DNA_strand = DNA_strand + line

print("Clean header: ", header)
print("Clean DNA strand: ", DNA_strand)
print()

print("Total nucleotide of the DNA sequence: ", len(DNA_strand))
G_content = DNA_strand.count("G")
C_content = DNA_strand.count("C")
GC_content = int(G_content) + int(C_content)
print("The amount of Guanine nucleotide is: ", int(G_content))
print("The amount of Cytosine nucleotide is: ", int(C_content))
print("The percentage of Guanine nucleotide is: ", int(G_content) / int(len(DNA_strand)) * 100, "%")
print("The percentage of Cytosine nucleotide is: ", int(C_content) / int(len(DNA_strand)) * 100, "%")
print("The total nucleotide of Guanine and Cytosine in this DNA sequence is: ", int(GC_content))
print("The percentage of Guanine and Cytosine nucleotide is: ", int(GC_content) / int(len(DNA_strand)) * 100, "%")
print()

print("Transcription happens")
mRNA_strand = DNA_strand.replace("T", "U")
print("The transcribed mRNA strand: ", str(mRNA_strand))
print()

print("Translation happens.")

from Bio.Seq import Seq
biopython_mRNA = Seq(mRNA_strand)
Protein1 = biopython_mRNA.translate(to_stop=True)
Protein2 = biopython_mRNA.translate()

print("Entire protein sequence including non-coding DNA: ", Protein2)
print("Protein sequence coded in translation only: ", Protein1)
