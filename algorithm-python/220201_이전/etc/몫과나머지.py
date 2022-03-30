def calculate_change(payment, cost):
    change = payment - cost

    # 거스름돈을 나눈 몫은 지폐의 갯수, 나머지는 나머지금액

    # 50000은 10000의 배수이므로 change % 50000 % 10000 == change % 1000
    # 50000, 10000은 5000의 배수이므로 change % 50000 % 10000 % 5000 == change % 5000

    fifty_count = change // 50000
    ten_count = (change % 50000) // 10000
    # five_count = (change % 50000 % 10000) // 5000
    five_count = (change % 10000) // 5000
    # one_count = (change % 50000 % 10000 % 5000) // 10000
    one_count = (change % 5000) // 10000

    print(f"50000원 지폐: {fifty_count}장")
    print(f"10000원 지폐: {ten_count}장")
    print(f"5000원 지폐: {five_count}장")
    print(f"1000원 지폐: {one_count}장")



# def calculate_change(payment, cost):
#     left = payment - cost
#     a, b, c, d = 0, 0, 0, 0
#     while left > 0:
#         if left >= 50000:
#             a += 1
#             left -= 50000
#
#         elif left >= 10000:
#             b += 1
#             left -= 10000
#
#         elif left >= 5000:
#             c += 1
#             left -= 5000
#
#         elif left >= 1000:
#             d += 1
#             left -= 1000
#
#     print(f"50000원 지폐: {a}장")
#     print(f"10000원 지폐: {b}장")
#     print(f"5000원 지폐: {c}장")
#     print(f"1000원 지폐: {d}장")


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)