# Challenge 281, Something About Bases
# https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

base_dict = {
    "0": 1,
    "1": 2,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "8": 9,
    "9": 10,
    "a": 11,
    "b": 12,
    "c": 13,
    "d": 14,
    "e": 15,
    "f": 16
}

dec_values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}

def get_max_digit(number):
    """returns a string containing the max value digit"""
    max_digit = "0"
    for digit in str(number):
        if(digit > "f" or digit < "0"):
            raise ValueError(digit, "isn't within hex ranges")
        elif(digit > max_digit):
            max_digit = digit

    return max_digit

#Number is a str and base is an int (confusing, I know)
def get_decimal_value(number, base):
    """returns the decimal value for a num in a given base"""
    place = len(number)
    value = 0

    for digit in number:
        place -=1
        value += dec_values[digit]*(base**place)
    return value


def something_about_bases(numbers):
    for number in numbers:
        base = base_dict[get_max_digit(number)] #This is the number for printing and multiplying
        dec_value = get_decimal_value(number, base)

        print number
        print "Base: ", base, " - Decimal Value: ", dec_value, "\n"

def something_about_bases_bonus(numbers):
    for number in numbers:
        print "\n", number
        base = base_dict[get_max_digit(number)]

        for i in range(base,17):
            dec_value = get_decimal_value(number, i)
            print "Base: ", i, " - Decimal Value: ", dec_value


test_nums = ["0", "1", "21", "ab3", "ff", "935"]
something_about_bases(test_nums)
something_about_bases_bonus(test_nums[2:])
