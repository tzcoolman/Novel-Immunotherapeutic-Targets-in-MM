import os,sys
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import math

def logcpm(value):
    return math.log(value+1,2)

def load_csv(filename,dem):
    return pd.read_csv(filename,index_col=0,sep=dem)

def load_list(filename):
    axx={}
    f1=open(filename)
    for line in f1.readlines():
        temp=line.replace("\r","").replace("\n","").replace("\"","").split(",")
        axx[temp[0]]=1
    f1.close()
    return axx

axx={'CD38':1,'TNFRSF17':1,'TNFRSF17':1,'SLAMF7':1}
aaa=load_csv("Figure4E_input.txt","\t")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
for target in axx.keys():
    if target in aaa.columns:
        total=aaa.sort_values(by=[target])
        total[target]=list(map(logcpm,list(total[target])))
        expressed=total[(total[target]!=0)]
        noexp=total[(total[target]==0)]
        sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=total,linewidth=0,s=8,palette='coolwarm')
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=noexp,linewidth=0,s=8,color='blue')
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=noexp,alpha=.70,linewidth=0,s=10,palette='binary')
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=aaa,alpha=.70,size=target,linewidth=0,s=10,palette=cmap)
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=aaa,alpha=.70,linewidth=0,s=10,palette='hot')
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue=target,data=aaa,alpha=.70,linewidth=0,s=10,palette='viridis')
        #partb=aaa[aaa['CD48']>1200]
        #sns_plot = sns.scatterplot(x='rnaUMAP1', y='rnaUMAP2',hue='seurat_cluster',data=aaa,alpha=.7,linewidth=0,s=10,palette='tab20')
        #plt.legend([],[], frameon=False) #hide legend
        #label_point(embedding_s['UMAP1'],embedding_s['UMAP2'],embedding_s['Gene_name'],plt.gca())
        #sns_plot.legend(loc='lower right')#, bbox_to_anchor=(1, .5))
        sns_plot.legend(fontsize=8)
        sns_plot.figure.savefig('0661_634'+'_'+target+'light_FDA.png',format="png",bbox_inches='tight',dpi=600)
        #sns_plot.figure.savefig('0661_634'+'_'+target+'light.svg',format="svg",bbox_inches='tight')
        plt.clf()
