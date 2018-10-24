import matplotlib.pyplot as plt
import numpy as np

#module to show what's the status of people using OkCupid 

def turnintopercentage(dt, totalnum):
      nouveaudt = []
      for value in dt:
            nouveaudt.append((value/totalnum)*100)
      return nouveaudt

def describestatus(data):
    number_of_mf = data.sex.value_counts()
    statusdata = data.groupby(['sex', 'status']).sex.count().to_dict() #I didn't know how to work with series
    femaledata  = [value for (sex, status), value in statusdata.items() if sex == 'f']
    maledata  = [value for (sex, status), value in statusdata.items() if sex == 'm']
    index = np.arange(5)
    bar_width = 0.35
    femaledata = turnintopercentage(femaledata,number_of_mf['f'])
    maledata =  turnintopercentage(maledata,number_of_mf['m'])

    fig, plot = plt.subplots()
    plot.bar(index,femaledata, bar_width, color = 'r', label='female')
    plot.bar(index + bar_width, maledata, bar_width, color = 'b', label='male')
    plot.set_xlabel('status')
    plot.set_ylabel('percentage')
    plot.set_xticks(index + bar_width / 2)
    plot.set_xticklabels([status for (sex, status), value in statusdata.items() if sex == 'm'])
    plot.legend()

    fig.tight_layout()
    plt.show()