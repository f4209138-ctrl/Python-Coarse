grades_book={"Alice":85,
        "Bob":92,
        "Charlie":78,
        "David":90,
        "Eva":95}
total_score=0
for score in grades_book.values():
    total_score+=score
class_average=total_score/len(grades_book)
top_score=max(grades_book.values())
bottom_score=min(grades_book.values())
top_students=[name for name, score in grades_book.items() if score==top_score]
bottom_students=[name for name,score in grades_book.items() if score==bottom_score]
print(f"Class Average: {class_average:2f}")
print(f"Top Score: {top_score} by {','.join(top_students)}")
print(f"Bottom Score: {bottom_score} by {','.join(bottom_students)}")
student_name=input("Enter student name to check score:")
score = grades_book.get(student_name)
if score is not None:
    print(f"{student_name}'s score is {score}")
else:
    print(f"{student_name}'s score is not found in the grade book.")


