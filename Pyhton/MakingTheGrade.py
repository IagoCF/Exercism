"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    return [round(new_score) for new_score in student_scores]

def count_failed_students(student_scores):
    total = 0
    for student in student_scores:
        if student <= 40: total += 1 
    return total

def above_threshold(student_scores, threshold):
    top = []
    for student in student_scores:
        if student >= threshold: top.append(student)
    return top

def letter_grades(highest):
    divs = round((highest - 40) / 4)
    return list(range(41, highest, divs))

def student_ranking(student_scores, student_names):
    return [
        f"{iter+1}. {student_names[iter]}: {student_scores[iter]}"
        for iter in range(len(student_names))
    ]

def perfect_score(student_info):
    for item in student_info:
        if item[1] == 100: return item
    return []