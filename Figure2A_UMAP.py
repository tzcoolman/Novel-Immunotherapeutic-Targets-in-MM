import numpy as np
#from sklearn.datasets import load_digits
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import os,sys
import datatable as dt
import umap
from sklearn.cluster import DBSCAN
#import sklearn
import sklearn.cluster as cluster
#f1=open(sys.argv[1])
def load_axx(filename): #load PSI
	return pd.read_csv(filename,index_col=0,sep="\t")

def label_point(x, y, val, ax,):
	a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
	for i, point in a.iterrows():
		ax.text(point['x'], point['y']+.03,str(point['val']),fontsize=9,color='red')

thefile="Figure2A_input.txt"
# Import metadata
metadata = pd.read_csv(thefile,sep="\t")
matrix = dt.fread(cmd='cut -f4- '+thefile,header=True, sep='\t', columns=dt.float64)
dt.fread(cmd='cut -f2- MMRF_events.psi.inverse.clean',header=False, sep='\t', columns=dt.float64)

colorx=['dodgerblue','silver','pink','red','purple','orangered','black','black'] #TRANSLOCATION
matrix=matrix.to_numpy()
count=7
#style='markerx',markers=xmarkerx
xmarkerx={"MMRF ND":'o','MMRF RR':"s",'IU ND':"d",'IU RR':'X'}
while count<8:
	brain_umap = umap.UMAP(random_state=count, n_neighbors=60,n_components=2, min_dist=.5)
	embedding = pd.DataFrame(brain_umap.fit_transform(matrix),columns = ['UMAP1','UMAP2'])
	embedding['ID']=metadata['ID']
	embedding['cohort']=metadata['cohort']
	sns_plot = sns.scatterplot(x='UMAP1', y='UMAP2',data=embedding,style='cohort',markers=xmarkerx,hue=metadata.Translocation.to_list(),alpha=.70,linewidth=0,s=18)
	sns_plot.legend(loc='upper right')#, bbox_to_anchor=(1, .5))
	sns_plot.figure.savefig('XXX_'+str(count)+'.svg',format="svg",bbox_inches='tight')
	plt.clf()
	count+=1
