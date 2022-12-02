# Entrez-Search-Tool

My initial project was to improve the Entrez search functions in order to obtain the same search results
that one would gather from the NCBI webtool. After attacking that problem for a bit, I found that you 
could include sort='relevance' in the esearch function and that would print the same results as the
webtool. Once I found that out, it was kind of too late to completely change my project so I decided to
instead make the entrez search tools from biopython easier to use and compile multiple sequences into 
one FASTA file as if you were downloading it from the webtool.

I wrote a script/function that asks the user their desired database (nucleotide and protein are the
only ones that work due to how the search results are stored), search term, and output file name. From
there the program prints each result and asks the user if they would like to write said result to their
FASTA file. Once the user says yes or no to each of the 5 results, it asks if they would like to search
again. If the user responds with yes, they enter their database, search term, and output file again and
the program runs again. If the user responds with no, the program ends and the sequences they said yes to,
if any, are all available within one FASTA file that can be used for further analysis.

There are some limitations to the program that I mostly had to live with to keep it from being too clunky.
Each search is limited to the first 5 search results so it helps to be specific with the search term. This
was to keep the user from having to cycle through extensive amounts of results to find the desired one.
Additionally, the output file has to be specified with each search rather than carrying through from the 
first time. 

I hope that you can see how this tool may be useful. It allows the user to compile multiple sequences on the
command line rather than download them from the webtool, which I think is valuable. 

----- Jameson Cosgrove :)
