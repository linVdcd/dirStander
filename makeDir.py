import argparse
import os

parser = argparse.ArgumentParser(description="make stander dirs")

parser.add_argument('--root',type=str,default='./makeDirTest',help='the mounted disk root')

args = parser.parse_args()
first_level=['datasets','projects','checkpoint']

second_level=['cv','nlp','speech','animation']



#make backup dir

os.system('mkdir '+args.root+'/backup')

#make datasetNote

for fl in first_level:
    for sl in second_level:
        if fl=='datasets':
            dir_huanshi=args.root+'/'+fl+'/'+sl+'_huanshi/datasetNote'
            dir_public=args.root+'/'+fl+'/'+sl+'_public/datasetNote'
            os.system('mkdir -p '+dir_huanshi)
            os.system('mkdir -p '+dir_public)
        else:
            dir = args.root+'/'+fl+'/'+sl
            os.system('mkdir -p '+dir)

#make datasets/model_data

os.system('mkdir '+args.root+'/datasets/model_data')
