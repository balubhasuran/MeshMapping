import pickle

#Python wraper for MetaMap 
from pymetamap import MetaMap# MetaMap for identifying biomedical concepts

# each element is a list of indications for prescribing a plant
phenotypes = pickle.load(open('/home/balus/Metamap/1000 random phenotypes', 'rb'))

#creating a metamap instace from a locally installed metamap 
mm = MetaMap.get_instance("/home/balus/Metamap/public_mm_linux_main_2016v2/public_mm/bin/metamap16")

# function defention to remove the non non ascii values found in phenotypes[i]
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# function call to to remove the non non ascii values found in phenotypes[i]
for i in range(len(phenotypes)):
    for j in range(len(phenotypes[i])):
       phenotypes[i][j]=strip_non_ascii(phenotypes[i][j])


for i in range(len(phenotypes)):
 sents = phenotypes[i]
 print('\n{} are supposedly treated by a plant'.format(phenotypes[i]))
 concepts,error = mm.extract_concepts(sents,[1,len(phenotypes[i])])
 for concept in concepts:
  print(concept)
 
