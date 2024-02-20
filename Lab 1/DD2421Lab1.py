import monkdata as m
import dtree as d
import numpy as np
import drawtree_qt5 as tree

#Assignment 1, entropy for training sets

#Assignment 2: Entropy increases when the distribution is uniform, since there is less information to go on.
#With a non-uniform distribution we have more information and less uncertainty. Normal dist..



monk1_entropy = d.entropy(m.monk1)
monk2_entropy = d.entropy(m.monk2)
monk3_entropy = d.entropy(m.monk3)

print(f'Entropy for monk1: {monk1_entropy}')
print(f'Entropy for monk2: {monk2_entropy}')
print(f'Entropy for monk3: {monk3_entropy}')

# Calculate average gain for every attribute in each dataset
for dataset, dataset_name in zip([m.monk1, m.monk2, m.monk3], ['monk1', 'monk2', 'monk3']):
    print(f'\nDataset: {dataset_name}')
    gains_dataset = [] #Save the gain for each iteration
    for attribute in m.attributes:
        gain = d.averageGain(dataset, attribute)
        gains_dataset.append(gain) #'Append the gain into the list'
        print(f'Average Gain for attribute {attribute.name}: {gain}')
    if dataset_name == 'monk1':
        monk1_gains = gains_dataset
    elif dataset_name == 'monk2':
        monk2_gains = gains_dataset
    elif dataset_name == 'monk3':
        monk3_gains = gains_dataset
#Too determine which attribute should be used for spliiting the examples at the root node, we look at the max value
max_monk1 = print(max(monk1_gains))
max_monk1= max(monk1_gains)
max_monk2 = print(max(monk2_gains))
max_monk3 = print(max(monk3_gains)) #this attribute should be used
#A higher information gain results in a greater reduction in entropy after the split
attribute = m.attributes



for i in range(1,5):
    monk1data_split = d.select(m.monk1, attribute[4], i)
    print('For A5 = ' + str(i))
    for j in range(6):
        gain = d.averageGain(monk1data_split, m.attributes[j])
        print(gain)


#tree.drawTree(d.buildTree(m.monk1,m.attributes))



#print(gain)

#splits = []
#for i in range(1,5):

#    splits.append(d.select(m.monk1,attribute[4],i))

#for i in range(1,5):
#    for attribute in m.attributes:
#        gain = d.averageGain(d.select(m.monk1,attribute[4],i), attribute)
##        print('A5 = ' + str(i))
#        print('Gain for' + attribute + 'is' + str(gain))
#    gains_dataset.append(gain)  # 'Append the gain into the list'
#    print(f'Average Gain for attribute {attribute.name}: {gain}')
