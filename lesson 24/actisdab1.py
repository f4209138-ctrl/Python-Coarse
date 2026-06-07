student_data={"id1":{"name":"Sara","class":"v","subject_intregration":"enlish,math,science"}}
{"id2":{"name":"David","class":"v","subject_intregration":"enlish,math,science"}}
{"id3":{"name":"Sara","class":"v","subject_intregration":"enlish,math,science"}}
{"id4":{"name":"Surya","class":"v","subject_intregration":"enlish,math,science"}}
results={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_key=(details["name"], details["class"],
                details["subject_intregration"])

    if unique_key not in seen_keys:
      seen_keys.append(unique_key)
      results[student_id]=details
for k,v in results.items():
    print(k,":",v)
