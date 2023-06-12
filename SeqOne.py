from Bio import Entrez, SeqIO
#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
#seq = Seq.Seq(str(seq), IUPAC.unambiguous_dna)

Entrez.email = "vonjirabe40@gmail.com"

hdl = Entrez.efetch(db='nucleotide', id=['NM_002299'], rettype='fasta') # Lactase gene
seq = SeqIO.read(hdl, 'fasta')

w_hdl = open('example.fasta', 'w')
w_seq = seq[11:5795]
SeqIO.write([w_seq], w_hdl, 'fasta')
w_hdl.close()

recs = SeqIO.parse('example.fasta', 'fasta')
for rec in recs:
   seq = rec.seq
   print(rec.description)
   print(seq)
   print(seq[0:20])
   print(seq.alphabet)
