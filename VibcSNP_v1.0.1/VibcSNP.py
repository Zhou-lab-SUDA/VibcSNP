import argparse, os, gzip
import datetime

from Species import species

from SNP import vc_snp


def vc():
    def check_value(value):
        if value not in ['s', 'r', 'c', 'sr', 'sc', 'rs', 'rc', 'cs', 'cr', 'src', 'scr', 'rsc', 'rcs', 'csr', 'crs']:
            raise argparse.ArgumentTypeError(
                'Mortal! You can only beseech for predictions of s(pecies), r(esistance), and c(gMLST)!')
        return value

    parser = argparse.ArgumentParser(
        description='Abracadabra, an ancient incantation, unveils the mystic power concealed within Acinetobacter baumannii genomes.',
        add_help=True,
        usage='''In the realm of code, behold Abracadabra, the enchanting script, that holds the key to unlocking the enigmatic potential within Acinetobacter baumannii genomes.'''
    )

    parser.add_argument(
        '-q', '--query',
        type=str,
        required=True,
        help='''-q or --query: Input genome.'''
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

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---Species Identification---')
    species_judge = species(args.query)
    [sp, ani] = species_judge
    if sp:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t Input genome is from species vibrio cholerae')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---SNP detection---')
        phy = vc_snp(args.query)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tSNP lineage: ' + phy)
    else:
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + '\tInput genome is not from species vibrio cholerae')
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAverage Nucleotide Identity: ' + ani)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t---Done---')


if __name__ == '__main__':
    vc()