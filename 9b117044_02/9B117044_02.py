import json


def get_student_info(data, student_id):
    for student in data:
        if student['student_id'] == student_id:
            return student
    raise ValueError(f'學號 {student_id} 找不到.')


def add_course(data, student_id, course_name, course_score):
    assert course_name != ' ', "課程名稱不可空白."
    assert course_score != ' ', "課程分數不可空白."
    for student in data:
        if student['student_id'] == student_id:
            student['courses'].append({
                'name': course_name,
                'score': course_score
            })
            return
    raise ValueError(f'學號 {student_id} 找不到.')


def calculate_average_score(student_data):
    if not student_data['courses']:
        return 0.0
    total_score = sum(course['score'] for course in student_data['courses'])
    return total_score / len(student_data['courses'])


def main():
    with open('./9b117044_02_00/students.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    while True:
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")
        choice = input("請選擇操作項目：")

        if choice == '1':
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)
                print("=>學生資料: " +
                      json.dumps(student_info, ensure_ascii=False, indent=2))
            except ValueError as e:
                print("=>發生錯誤: " + str(e))
        elif choice == '2':
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score = input("請輸入要新增課程的分數: ")
            if course_name.strip() == '':
                print("=>其它例外: 課程名稱不可空白.")
                continue
            if not course_score.strip().isdigit():
                print("=>其它例外: 課程分數必須為非負數值。")
                continue
            try:
                add_course(data, student_id, course_name, float(course_score))
                print("=>課程已成功新增。")
            except ValueError as e:
                print(f"=>發生錯誤: {str(e)}")
        elif choice == '3':
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)
                avg_score = calculate_average_score(student_info)
                print(f"=>各科平均分數: {avg_score}")

            except ValueError as e:
                print(f"=>發生錯誤: {str(e)}")

        elif choice == '4':
            print("=>程式結束。")
            break

        else:
            print("=>請輸入有效的選項。")


if __name__ == "__main__":
    main()
