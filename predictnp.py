"""
Final prediction of the captured number plate from the segmented char images
"""
import os
import charactersegmentation
import joblib

# loading the already saved model
current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/svc/svc.pkl')
model = joblib.load(model_dir)

# predicting the character from the segmented image
classification_result = []
for each_character in charactersegmentation.characters:
    # converts it to a 1D array
    each_character = each_character.reshape(1, -1)
    result = model.predict(each_character)
    classification_result.append(result)

# print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]

# print(plate_string)

# As it's possible that the characters be wrongly arranged,
# the column_list will be used to sort the characters in the right order.
column_list_copy = charactersegmentation.column_list[:]
charactersegmentation.column_list.sort()
correct_number_plate = ''
for each in charactersegmentation.column_list:
    correct_number_plate += plate_string[column_list_copy.index(each)]

print("The number plate of the specified car is : ", correct_number_plate)
