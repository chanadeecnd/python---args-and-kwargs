def average(*args):
    sum_score = sum(args)
    average_score = sum_score / len(args)
    return average_score

def check_passed(**kwargs):
    math = kwargs.get('math')
    physics = kwargs.get('physics')
    english = kwargs.get('english')

    if math is not None and math >= 50:
        print("สอนผ่านวิชาคณิต")
    if physics is not None and physics >= 50:
        print("สอบผ่านวิชาฟิสิกส์")
    if english is not None and english >= 50:
        print("สอบผ่านวิชาอังกฤษ")

result_average = average(1,2,3,4,5,6,7,8,9,10)
print(f"Result = ", result_average)

check_passed(math=50, physics=60)