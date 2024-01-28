# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:21:48 2023

@author: salva
"""

import pandas as pd 

# User inputs for files used
inpt1 = input('please input molar table: ')
inpt2 = input('please input ox% table: ')
inpt3 = input('please input the output file name: ')

# molar reference table (standard)
df_table = pd.read_csv(inpt1)

# ox%  table (PDS/PIQUANT output)
df_ox = pd.read_csv(inpt2) 

# PMC list
lst_PMC = df_ox['PMC']

# select element oxides from the oxide table
lst_sodium_ox = df_ox['Na2O_wt%']
lst_magnesium_ox = df_ox['MgO_wt%']
lst_aluminum_ox = df_ox['Al2O3_wt%']
lst_silicon_ox = df_ox['SiO2_wt%']
lst_phosphorus_ox = df_ox['P2O5_wt%']
lst_sulfur_ox = df_ox['SO3_wt%']
lst_chlorine_ox = df_ox['Cl_wt%']
lst_potassium_ox = df_ox['K2O_wt%']
lst_calcium_ox = df_ox['CaO_wt%']
lst_titanium_ox = df_ox['TiO2_wt%']
lst_chromium_ox = df_ox['Cr2O3_wt%']
lst_manganese_ox = df_ox['MnO_wt%']
lst_iron_ox = df_ox['FeO-T_wt%']
lst_nickel_ox = df_ox['NiO_wt%']
lst_zinc_ox = df_ox['ZnO_wt%']
lst_bromine_ox = df_ox['Br_wt%']


# element properties
element_properties = ["sodium", "magnesium", "aluminum", "silicon", "phosphorus",
                      "sulfur", "chlorine", "potassium", "calcium", "titanium",
                      "chromium", "manganese", "iron", "nickel", "zinc", "bromine"]


# obtain molar values for each element (molar_values)
# chemical formula number (i.e: SiO2 => n_Si = 1) (number_values)
molar_values = {}
number_values = {}

for i, element in enumerate(element_properties):
    molar_values[element + "_molar"] = df_table.iloc[i, 1]
    number_values[element + "_number"] = df_table.iloc[i, 2]


# obtain mole values for each element
sodium_moles = [(float(sodium) / float(molar_values['sodium_molar'])) * float(number_values['sodium_number']) for sodium in lst_sodium_ox]
magnesium_moles = [(float(magnesium) / float(molar_values['magnesium_molar'])) * float(number_values['magnesium_number']) for magnesium in lst_magnesium_ox]
aluminum_moles = [(float(aluminum) / float(molar_values['aluminum_molar'])) * float(number_values['aluminum_number']) for aluminum in lst_aluminum_ox]
silicon_moles = [(float(silicon) / float(molar_values['silicon_molar'])) * float(number_values['silicon_number']) for silicon in lst_silicon_ox]
phosphorus_moles = [(float(phosphorus) / float(molar_values['phosphorus_molar'])) * float(number_values['phosphorus_number']) for phosphorus in lst_phosphorus_ox]
sulfur_moles = [(float(sulfur) / float(molar_values['sulfur_molar'])) * float(number_values['sulfur_number']) for sulfur in lst_sulfur_ox]
chlorine_moles = [(float(chlorine) / float(molar_values['chlorine_molar'])) * float(number_values['chlorine_number']) for chlorine in lst_chlorine_ox]
potassium_moles = [(float(potassium) / float(molar_values['potassium_molar'])) * float(number_values['potassium_number']) for potassium in lst_potassium_ox]
calcium_moles = [(float(calcium) / float(molar_values['calcium_molar'])) * float(number_values['calcium_number']) for calcium in lst_calcium_ox]
titanium_moles = [(float(titanium) / float(molar_values['titanium_molar'])) * float(number_values['titanium_number']) for titanium in lst_titanium_ox]
chromium_moles = [(float(chromium) / float(molar_values['chromium_molar'])) * float(number_values['chromium_number']) for chromium in lst_chromium_ox]
manganese_moles = [(float(manganese) / float(molar_values['manganese_molar'])) * float(number_values['manganese_number']) for manganese in lst_manganese_ox]
iron_moles = [(float(iron) / float(molar_values['iron_molar'])) * float(number_values['iron_number']) for iron in lst_iron_ox]
nickel_moles = [(float(nickel) / float(molar_values['nickel_molar'])) * float(number_values['nickel_number']) for nickel in lst_nickel_ox]
zinc_moles = [(float(zinc) / float(molar_values['zinc_molar'])) * float(number_values['zinc_number']) for zinc in lst_zinc_ox]
bromine_moles = [(float(bromine) / float(molar_values['bromine_molar'])) * float(number_values['bromine_number']) for bromine in lst_bromine_ox]
  
  
# elemental combination for mineral identification
iron_magnesium_moles = [float(iron) + float(magnesium) for iron, magnesium in zip(iron_moles, magnesium_moles)]
iron_magnesium_calcium_moles = [float(iron) + float(magnesium) + float(calcium) for iron, magnesium, calcium in zip(iron_moles, magnesium_moles, calcium_moles)]
potassium_sodium_aluminum_moles = [float(potassium) + float(sodium) + float(aluminum) for potassium, sodium, aluminum in zip(potassium_moles, sodium_moles, aluminum_moles)]
calcium_aluminum_moles = [float(calcium) + float(aluminum) for calcium, aluminum in zip(calcium_moles, aluminum_moles)]


# Elemental ratios
# Fe/Mn
iron_to_manganese = [float(iron)/float(manganese) if float(manganese) != 0 else None
                     for iron, manganese in zip(iron_moles, manganese_moles)]

# olivine (Fe,Mg)_2SiO_4 => (Fe+Mg)/Si = 2
olivine_conditionB = [float(iron_magnesium)/float(silicon) for iron_magnesium, silicon in zip(iron_magnesium_moles, silicon_moles)]

# pyroxene (Fe,Mg,Ca)_2Si_2O_6  => (Fe+Mg+Ca)/Si = 1
pyroxene_conditionB = [float(iron_magnesium_calcium)/float(silicon) for iron_magnesium_calcium, silicon in zip(iron_magnesium_calcium_moles, silicon_moles)]

# K,Na-feldspar (K,Na)AlSi_3O_8 => (K+Na+Al)/Si = 2/3
alkali_feldspar_conditionB = [float(potassium_sodium_aluminum)/float(silicon) for potassium_sodium_aluminum, silicon in zip(potassium_sodium_aluminum_moles, silicon_moles)]

# Anorthrite CaAl_2Si_2O_8 => (Ca + Al)/Si = 3/2
anorthrite_conditionB = [float(calcium_aluminum)/float(silicon) for  calcium_aluminum, silicon in zip(calcium_aluminum_moles, silicon_moles)]

data = {'PMC':lst_PMC,
        'Na (moles)':sodium_moles,
        'Mg (moles)':magnesium_moles,
        'Al (moles)':aluminum_moles,
        'Si (moles)':silicon_moles,
        'P (moles)':phosphorus_moles,
        'S (moles)':sulfur_moles,
        'Cl (moles)':chlorine_moles,
        'K (moles)':potassium_moles,
        'Ca (moles)':calcium_moles,
        'Ti (moles)':titanium_moles,
        'Cr (moles)':chromium_moles,
        'Mn (moles)':manganese_moles,
        'Fe (moles)':iron_moles,
        'Ni (moles)':nickel_moles,
        'Zn (moles)':zinc_moles,
        'Br (moles)':bromine_moles,
        '(Mg+Fe+Ca)/Si':pyroxene_conditionB,
        '(Mg+Fe)/Si':olivine_conditionB,
        '(K+Na+Al)/Si':alkali_feldspar_conditionB,
        '(Ca+Al)/Si':anorthrite_conditionB,
        'Fe/Mn':iron_to_manganese}

df = pd.DataFrame(data)
df.to_csv(inpt3)

