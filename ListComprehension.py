
# ========================
# List Comprehension /////
# ========================

List = [1,2,3,4,5,6]

li=[]
for x in range(1,101):
    li.append(x**2)

li2 = [i**2 for i in range(1,11)]
li3 = [i**2 for i in List]

print([z for z in List if z % 2 == 0])



num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 0: 'Zero'}



def n2w(n):
    try:
        print(num2words[n])
    except (KeyError,ValueError,TypeError) as er:
        print(er)


print([z for z in List if z % 2 == 0 or n2w(z)])



