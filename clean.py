import pandas as pd

# load in data, change path to location of files
PATH = 'F:\Data files\Infovis' 
title = pd.read_csv(PATH + '\\soc-redditHyperlinks-title.tsv', sep='\t')
body = pd.read_csv(PATH + '\\soc-redditHyperlinks-body.tsv', sep='\t')

# column names
names = "1. Number of characters\
2. Number of characters without counting white space\
3. Fraction of alphabetical characters\
4. Fraction of digits\
5. Fraction of uppercase characters\
6. Fraction of white spaces\
7. Fraction of special characters, such as comma, exclamation mark, etc.\
8. Number of words\
9. Number of unique works\
10. Number of long words (at least six characters)\
11. Average word length\
12. Number of unique stopwords\
13. Fraction of stopwords\
14. Number of sentences\
15. Number of long sentences (at least ten words)\
16. Average number of characters per sentence\
17. Average number of words per sentence\
18. Automated readability index"
names = [''.join([i for i in s if not i.isdigit()]) for s in names.split('.')]
names = [x for x in names if x != '']
names = {x:names[x] for x in range(len(names))}

def clean(df, name):
    df2 = df['PROPERTIES'].str.split(',', 18, expand=True)
    df = pd.concat([df, df2], axis=1)
    df = df.rename(columns=names)
    
    # if we need less columns, add the unneccesary ones to this
    df = df.drop(columns=['POST_ID', 'TIMESTAMP', 'PROPERTIES', 18])
    df = df.dropna()
    df.to_csv(PATH + name)
    
clean(title, '\\title.csv')
clean(body, '\\body.csv')

# to read the files back
body = pd.read_csv(PATH + '\\body.csv', index_col=0)
title = pd.read_csv(PATH + '\\title.csv', index_col=0)