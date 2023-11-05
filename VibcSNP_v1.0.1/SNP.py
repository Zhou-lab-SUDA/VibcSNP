import os
import subprocess
import tempfile
from configure import db_list, exe

minimap2_exe = exe['minimap2']
samtools_exe = exe['samtools']
bcftools_exe = exe['bcftools']
snp = db_list['snp']
reference_genome = db_list['species_ref']


def parse_vcf(vcf_file):
    vcf_dict = {}
    with open(vcf_file, 'rt') as vcf:
        for line in vcf:
            if not line.startswith('#'):
                parts = line.rstrip().split('\t')
                pos, ref_base, alt_base = parts[1], parts[3], parts[4]
                vcf_dict[pos] = [ref_base, alt_base]
    return vcf_dict


def vc_snp(query):
    with tempfile.TemporaryDirectory() as temp_dir:
        mp_sam = os.path.join(temp_dir, "mp.sam")
        mp_bam = os.path.join(temp_dir, "mp.bam")
        sorted_bam = os.path.join(temp_dir, "sorted.bam")
        vcf_file = os.path.join(temp_dir, "vcf.file")

        step1 = f"{minimap2_exe} -a {reference_genome} {query} -o {mp_sam}"
        step2 = f"{samtools_exe} view -bS -o {mp_bam} {mp_sam}"
        step3 = f"{samtools_exe} sort {mp_bam} -o {sorted_bam}"
        step4 = f"{samtools_exe} index {sorted_bam}"
        step5 = f"{bcftools_exe} mpileup -Ou -f {reference_genome} {sorted_bam} | {bcftools_exe} call -mv -Ov -o {vcf_file}"

        for step in [step1, step2, step3, step4, step5]:
            subprocess.run(step, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        vcf_dict = parse_vcf(vcf_file)
        # print(vcf_dict)
    potential_lineage = {}
    with open(snp, 'rt') as lineage_file:
        for line in lineage_file:
            if not line.startswith('#'):
                parts = line.rstrip().replace(' ', '\t').split('\t')
                lineage = parts[0]
                site, homoplasy, snp_pair = parts[2], parts[3], parts[4].split('->')
                if site in vcf_dict.keys():
                    # print(snp_pair, site)
                    if snp_pair == vcf_dict[site]:
                        # print(snp_pair, site)
                            if lineage in potential_lineage.keys():
                                potential_lineage[lineage] += 1
                            else:
                                potential_lineage[lineage] = 1

    phy = 'New lineage'
    if len(potential_lineage.keys()) < 1:
        phy = 'New lineage'
    else:
        max = 0
        for l in potential_lineage.keys():
            count = potential_lineage[l]
            if max <= count:
                max = count
                phy = l

    return phy