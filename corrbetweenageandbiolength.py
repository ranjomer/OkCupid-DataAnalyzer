import matplotlib.pyplot as plt

#method to calculate the correlation between age and bio length 
#it turns out there's a weak correlation of 0.15

def corrageandbiolen(data):
    fig, plot = plt.subplots()
    corrageabtmelen = data['age'].corr(data['about_me_length'])
    plot.plot(data['age'], data['about_me_length'])
    plot.set_title('correlation :' + str(corrageabtmelen))
    plot.set_xlabel('Age')
    plot.set_ylabel('About Me Length')

    fig.tight_layout()
    plt.show()