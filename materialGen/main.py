 
camelName = ['EnrichedFraction', 'LiquidEnrichedFraction', 'HotPureFraction', 'HotLowFraction']
unlocalizedName = ['enriched_fraction_', 'liquid_enriched_fraction_', 'hot_pure_fraction_', 'hot_low_fraction_']
localizedName = ['Enriched Fraction', 'Liquid Enriched Fraction', 'Hot Pure Fraction', 'Hot Low Fraction']
idToStart = 24800
fractionNumber = 12
        
f = open('input.txt','r')
string = f.read()
open('output.txt', 'w').close()

lang = open('lang.txt', 'w').close()
lang = open('lang.txt', 'a')

material = open('material.txt', 'w').close()
material = open('material.txt', 'a')

id = idToStart

for j in range(1, fractionNumber + 1):

    string2 = str(string)

    for i in range(len(camelName)):
 
        str1 = string2.replace('id' + str(i + 1), str(id + i))
        str2 = str1.replace('Name' + str(i + 1), camelName[i] + str(j))
        str3 = str2.replace('name' + str(i + 1), unlocalizedName[i] + str(j))
        string2 = str(str3)
        
        lang.write('material.' + unlocalizedName[i] + str(j) + '=' + localizedName[i] + ' ' + str(j) + '\n')
        material.write('public static Material ' + camelName[i] + str(j) + ';' + '\n')
        
    output = open('output.txt', 'a')
    output.write('\n' + '\n' + str3)
    id += len(camelName)
        
       