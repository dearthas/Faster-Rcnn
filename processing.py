import matplotlib.image as mpimg
import numpy as np
import csv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(dir_path+"/old"):
    if filename.endswith(".jpg"):
        nom=filename
        img = mpimg.imread(dir_path+"/old/"+nom)
        image = np.zeros((500, 500, 3), dtype=np.uint8)
        aleatoire1=int(np.random.rand()*300)
        aleatoire2=int(np.random.rand()*300)
        for i in range(28):
            for j in range(28):
                image[i+50+aleatoire2][j+50+aleatoire1]=img[i][j]
        mpimg.imsave(dir_path+"\\new\\"+nom,image)
        label=nom[6:7]
        with open(dir_path+"\\new\\"+nom[0:-3]+'bboxes.labels.tsv', 'w') as out_file:
            tsv_writer = csv.writer(out_file)
            tsv_writer.writerow(label)
        with open(dir_path+"\\new\\"+nom[0:-3]+'bboxes.tsv', 'w') as out_file:
            tsv_writer = csv.writer(out_file,delimiter='\t')
            tsv_writer.writerow([aleatoire1+50,aleatoire2+50,50+aleatoire1+28,50+aleatoire2+28])
