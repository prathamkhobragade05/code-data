import pandas as pd
import random

def get_roll_numbers(mark):
    match mark:
        case 21:
            return [1, 4, 8, 24, 32, 37, 45, 53, 60, 61]
        case 22:
            return [7, 9, 12, 15, 19, 22, 23, 29, 31, 36, 40, 41, 43, 44, 49, 51, 52, 54, 55, 57, 59, 65, 66]
        case 23:
            return [2, 5, 14, 16, 17, 18, 21, 39, 46, 47, 56, 58, 63, 64]
        case 24:
            return [20, 25, 38]
        case _:
            return "Invalid"
        
def marksDistribution(mark):
    match mark:
        case 21:
            return { 20: 6, 21: 13, 22: 2, 23: 2 }
        case 22:
            return { 20: 2, 21: 4, 22: 9, 23: 8 }
        case 23:
            return { 21: 1, 22: 1, 23: 21 }
        # case 24:
        #     return { 20: 2, 21: 4, 22: 9, 23: 8 }
        case _:
            return "Invalid"

# Generate marks
def generate_marks():
    marks = []
    for mark, count in mark_distribution.items():
        marks.extend([mark] * count)
    random.shuffle(marks)
    return marks

def reCalculateMarks():
    calcuatedMarks=0
    for m in marks:
        calcuatedMarks=calcuatedMarks+m
    print(f"---23*{givenMarks}->>{23*givenMarks}-------------sum of marks:",calcuatedMarks)
    print(calcuatedMarks//23)

if __name__ == "__main__":
    file_path = "css_data.xlsx"

    givenMarks=int(input("Enter Marks (21-24): "))
    roll_numbers= get_roll_numbers(givenMarks)
    mark_distribution = marksDistribution(givenMarks)

#---Load Excel file
    df = pd.read_excel(file_path)
#---Practical columns (skip Roll No)
    practical_cols = df.columns[1:]

#---Loop through each roll number
    for roll_number in roll_numbers:

        if roll_number not in df['Roll No'].values:
            print(f"Roll No {roll_number} not found, skipping...")
            continue

#-------Get row index
        row_index = df[df['Roll No'] == roll_number].index[0]

#-------Generate new random marks
        marks = generate_marks()

#-------Update row of given roll no
        for i, col in enumerate(practical_cols):
            if i < len(marks):
                df.at[row_index, col] = marks[i]
        
    reCalculateMarks()
    
    # Save changes
    df.to_excel(file_path, index=False)

    print(f"✅ All updates completed! for {givenMarks}: ",roll_numbers)
