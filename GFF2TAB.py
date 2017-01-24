with open("C:\Users\skumar20\Desktop\Bioinfo_dev\GFF_parser\samp1.gff", "r") as gff_file:
    data = gff_file.readlines()
gff_file.close()
o_file = open("C:\Users\skumar20\Desktop\Bioinfo_dev\GFF_parser\samp2.gff","w")
for line in data:
    o_file.write(line)
o_file.close()
