from shutil import which
import os


exe = dict(fastANI=which('fastANI'),
           minimap2=which('minimap2'),
           samtools=which('samtools'),
           bcftools=which('bcftools'))
           
dirname = os.path.dirname(os.path.abspath(__file__))

db_folder = os.path.join(dirname, 'db')
           
db_list = dict(species_ref = os.path.join(db_folder, 'reference.fna'), snp = os.path.join(db_folder, 'SNP.list'))
