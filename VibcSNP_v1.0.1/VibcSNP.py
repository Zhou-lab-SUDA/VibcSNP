import argparse, os, gzip
import datetime
from configure import example
from Species import species

from SNP import vc_snp


def vc():
    parser = argparse.ArgumentParser(
        description='VibcSNP 1.0.1 https://github.com/Zhou-lab-SUDA/VibcSNP/',
        add_help=True,
        usage='VibcSNP.py -q query genome.'
    )

    parser.add_argument(
        '-q', '--query',
        type=str,
        required=True,
        help='''-q or --query: Input genome.
        Try examples with -q/--query vc_example or non_vc_example.'''
    )
    '''parser.add_argument(
        '-p', '--prefix',
        required=False,
        default='Abr',
        type=str,
        help=-p or --prefix: Prefix for output file. Default as Vibc.
    )'''

    args = parser.parse_args()

    '''if args.prefix:
        work_dir = args.prefix.rsplit('/', 1)[0] if len(args.prefix.rsplit('/', 1)) > 1 else os.path.join(os.getcwd(),
                                                                                                          args.prefix)
    else:
        work_dir = os.path.join(os.getcwd(), 'Vibc')'''
    if args.query == 'vc_example':
        query = os.path.join(example, '3.4.8.fna')
    elif args.query == 'non_vc_example':
        query = os.path.join(example, 'Not_Vc.fna')
    else:
        query = args.query
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---Species Identification---')
    species_judge = species(query)
    [sp, ani] = species_judge
    if sp:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t Input genome is from species vibrio cholerae')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---SNP detection---')
        phy = vc_snp(query)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tSNP lineage: ' + phy)
    else:
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + '\tInput genome is not from species vibrio cholerae')
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAverage Nucleotide Identity: ' + ani)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---Done---')


if __name__ == '__main__':
    vc()