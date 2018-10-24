import matplotlib.pyplot as plt

# module to calculate the average bio length of males and females

def calcavgbiolength(data):
    biolengthM = 0
    biolengthF = 0
    fig, plot = plt.subplots()
    number_of_mf = data.sex.value_counts()
    for row in data.groupby('sex').about_me_length:
        if(row[0] == 'f'):
            for bio in row[1]:
                biolengthF += bio
        else:
            for bio in row[1]:
                biolengthM += bio

    averagefbio = biolengthF / number_of_mf['f']
    averagembio = biolengthM / number_of_mf['m']
    plot.bar(height = averagefbio, color = 'r', label='female', x = 0.6, width = 0.1)
    plot.bar(height = averagembio, color = 'b', label='male', x = 0.8, width = 0.1)
    plot.set_xlabel('sex')
    plot.set_ylabel('average bio length')
    plot.legend()
    
    fig.tight_layout()
    plt.show()