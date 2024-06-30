selected_int = int(input("Enter the integer here: "))
start_count = 0
sacrifice = selected_int

while sacrifice > 1:
    sacrifice -= 1
    print(sacrifice)
    start_count += sacrifice

final_answer = selected_int + start_count
print(final_answer)