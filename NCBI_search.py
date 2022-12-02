from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Entrez
from typing import List
import re
import textwrap



######################################################################################################################
##### Entrez search function that inputs a database and search to output a FASTA file with the desired sequences #####
######################################################################################################################

def entrez_search():
    while True:
    
        input_db = input("Enter the NCBI database you would like to search: (nuccore/protein) ")
        input_term = input("Enter your search term: ")
        output_file_name = input("Enter the desired output file name: ")


        Entrez.email = "email"
        search = Entrez.esearch(db=input_db, term=input_term, retmax=5, sort='relevance')
        search_results = Entrez.read(search)

        id_list = search_results['IdList']
        fetch = Entrez.efetch(db=input_db, id=id_list, rettype="fasta")
        sequences = fetch.read()

        with open('search_results.fasta', 'w') as search_results:
            search_results.write(sequences)


        results_fasta = SeqIO.parse('search_results.fasta', 'fasta')

        for record in results_fasta:
            gene_id = record.description
            keep_sequence = input(gene_id + "\nWould you like to write this sequence to the FASTA file? (y/n) ")
            if keep_sequence == 'n':
                continue
            if keep_sequence == 'y':
                with open(output_file_name, 'a') as output_file:
                    output_file.write('>' + str(gene_id) + '\n' + str('\n'.join(textwrap.wrap(str(record.seq), 70))) + '\n')
            else:
                pass

        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("Thanks for searching.")
            break
        

############################################################################################################################################

entrez_search()
