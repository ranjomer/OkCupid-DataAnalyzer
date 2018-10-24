from collections import Counter
#module to calculate the most used words used by each sex
#inspired by Nabokov's favorite word is mauve


def calcfavwords(data):
    number_of_mf = data.sex.value_counts()
    femalewords = data[data.sex == 'f'].about_me
    malewords = data[data.sex == 'm'].about_me.sample(n = number_of_mf['f']) #so the data is not skewed 
    fwc = Counter()
    mwc = Counter()
    for fs in femalewords:
        fwc.update(word for word in fs.split())
    for ml in malewords:
        mwc.update(word for word in ml.split())

    #this is done to weed out the most common words and emphasize special words.
    #it doesn't work exactly for females, idk why
    ffff = fwc - mwc 
    mmmm = mwc - fwc

    print(ffff.most_common(100))
    print()
    print(mmmm.most_common(100))