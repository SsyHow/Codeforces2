def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = {0 : 'zero', 1 : 'one', 2: 'two', 3: 'three', 4 : 'four', 5: 'five', 6 :'six', 7: 'seven', 8 :'eight', 9: 'nine', 10: 'ten',
       11 :'eleven', 12: 'twelve', 13: 'thirteen', 14 : 'fourteen', 15 :'fifteen', 16: 'sixteen', 17: 'seventeen', 18 : 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50 : 'fifty', 60 : 'sixty', 70: 'seventy', 80: 'eighty', 90 : 'ninety'}
b = II()
if 0 <= b <= 19:
    print(num[b])
else:
    if b % 10 == 0:
        print(f'{tens[b - b%10]}')
    else:
        print(f'{tens[b - b%10]}-{num[b%10]}')