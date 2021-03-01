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
10. Number of long words (at least 6 characters)\
11. Average word length\
12. Number of unique stopwords\
13. Fraction of stopwords\
14. Number of sentences\
15. Number of long sentences (at least 10 words)\
16. Average number of characters per sentence\
17. Average number of words per sentence\
18. Automated readability index\
19. Positive sentiment calculated by VADER\
20. Negative sentiment calculated by VADER\
21. Compound sentiment calculated by VADER\
22. LIWC_Funct\
23. LIWC_Pronoun\
24. LIWC_Ppron\
25. LIWC_I\
26. LIWC_We\
27. LIWC_You\
28. LIWC_SheHe\
29. LIWC_They\
30. LIWC_Ipron\
31. LIWC_Article\
32. LIWC_Verbs\
33. LIWC_AuxVb\
34. LIWC_Past\
35. LIWC_Present\
36. LIWC_Future\
37. LIWC_Adverbs\
38. LIWC_Prep\
39. LIWC_Conj\
40. LIWC_Negate\
41. LIWC_Quant\
42. LIWC_Numbers\
43. LIWC_Swear\
44. LIWC_Social\
45. LIWC_Family\
46. LIWC_Friends\
47. LIWC_Humans\
48. LIWC_Affect\
49. LIWC_Posemo\
50. LIWC_Negemo\
51. LIWC_Anx\
52. LIWC_Anger\
53. LIWC_Sad\
54. LIWC_CogMech\
55. LIWC_Insight\
56. LIWC_Cause\
57. LIWC_Discrep\
58. LIWC_Tentat\
59. LIWC_Certain\
60. LIWC_Inhib\
61. LIWC_Incl\
62. LIWC_Excl\
63. LIWC_Percept\
64. LIWC_See\
65. LIWC_Hear\
66. LIWC_Feel\
67. LIWC_Bio\
68. LIWC_Body\
69. LIWC_Health\
70. LIWC_Sexual\
71. LIWC_Ingest\
72. LIWC_Relativ\
73. LIWC_Motion\
74. LIWC_Space\
75. LIWC_Time\
76. LIWC_Work\
77. LIWC_Achiev\
78. LIWC_Leisure\
79. LIWC_Home\
80. LIWC_Money\
81. LIWC_Relig\
82. LIWC_Death\
83. LIWC_Assent\
84. LIWC_Dissent\
85. LIWC_Nonflu\
86. LIWC_Filler\
"
names = [''.join([i for i in s if not i.isdigit()]) for s in names.split('.')]
names = [x for x in names if x != '']
names = {x:names[x].strip() for x in range(len(names))}


def clean(df, name):
    
    # split properties column
    df2 = df['PROPERTIES'].str.split(',', 86, expand=True)
    df = pd.concat([df, df2], axis=1)
    df = df.rename(columns=names)
    
    # select subset of needed columns
    df = df[['SOURCE_SUBREDDIT','TARGET_SUBREDDIT','TIMESTAMP','Compound sentiment calculated by VADER',
               'Number of words','Number of unique works','Average word length','Fraction of stopwords',
               'Automated readability index','LIWC_Swear','LIWC_Anger','LIWC_Past','LIWC_Present','LIWC_Future',
               'LIWC_Posemo','LIWC_Negemo','LIWC_Affect','LIWC_Social','LIWC_Nonflu','LIWC_Assent','LIWC_Dissent']]
    df = df.dropna()
    df.to_csv(PATH + name)

# clean both title and body dataframes
clean(title, '\\title.csv')
clean(body, '\\body.csv')

# # to read the files back
# body = pd.read_csv(PATH + '\\body.csv', index_col=0)
# title = pd.read_csv(PATH + '\\title.csv', index_col=0)