#April 12 - A sample of a dictionary guest list

#define the dictionary
age = {}
#add names to dictionary with distinct ages
age['Anna'] = 20
age['Portia'] = 19
age['Ambrose'] = 65
age['Allain'] = 45


#use the function_name.has_key(key-name)
#it rerturns TRUE if the dictionary has the key-name in it 
#And FALSE if it doesnt
#Dsisplay: confirm a person's name exist in the dictionary
# Dispaly: show how old they are
if age.has_key('Anna'):
    print 'Anna is listed in the dictionary. She is'+ ' ' +str(age['Anna']) + ' years old'
else:
    print 'Anna could not be found.'
if age.has_key('Portia'):
    print 'Portia is listed in the dictionary. She is'+ ' ' + str(age['Portia']) + 'years old'
else:
    print 'Portia could not be found.'
if age.has_key('Ambrose'):
    print 'Ambrose is listed in the dictionary. She is'+' '+str(age['Ambrose'])+' years old'



