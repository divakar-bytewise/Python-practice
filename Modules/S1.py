def avg_marks(marks):
    return sum(marks)/len(marks)

def grade(avg):
    if avg>=90:
        return 'A'
    elif avg>=70:
        return 'B'
    elif avg>=50:
        return 'C'
    elif avg>=35:
        return 'D'
    else:
        return 'F'

def priniting_stud(name,marks):
    avg=avg_marks(marks)
    grades=grade(avg)
    print(f"stud name : {name}")
    print(f"Marks:{marks}")
    print(f"Average:{avg:.2f}")
    print(f"grade:{grades}")
