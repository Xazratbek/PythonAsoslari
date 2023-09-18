import unittest

def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

def getArea(r,pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPerimeter(r,pi=3.14159):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2*pi*r

def tubSonmi(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
        if n%i==0:
            return False
    return True

def eng_kattasi(x,y,z):
    return max(x,y,z)

def capitalize_first_letters(wordlist: list):
    new_words = []
    for word in wordlist:

        new_words.append(word.title())

    return new_words

def get_just_sonlar(numbers: list):
    return [num for num in numbers if num % 2 == 0]

def is_in_fibonacci_sequence(number):
    if number < 0:
        return False
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

# print(get_full_name('alijon','valiyev'))
# print(eng_kattasi(1,6,2))
# print(test_capitalize_first_letters(["olma","anor","sabzi","hasan"]))
# print(get_just_sonlar([1,2,5,7,8,10,13,15,12,16,18,20]))



##### UNITTEST #####

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon','valiyev')
        self.assertEqual(formatted_name, 'Alijon Valiyev')

    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name,'Hasan Olimovich Husanov')

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3),28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))

# Amaliyot

class EngKattasiTest(unittest.TestCase):

    def eng_kattasi_test(self):
        self.assertEqual(find_largest_number(10, 5, 8), 10)
        self.assertEqual(find_largest_number(15, 20, 17), 20)
        self.assertEqual(find_largest_number(3, 3, 3), 3)
        self.assertEqual(find_largest_number(-5, -10, -3), -3)
        self.assertEqual(find_largest_number(0, 0, 0), 0)

class KattalashtiramizTest(unittest.TestCase):
    def test_capitalize_first_letters(self):
        texts = ["hello", "world", "mohira"]
        expected_result = ["Hello", "World", "Mohira"]
        self.assertEqual(capitalize_first_letters(texts), expected_result)

class TestExtractEvenNumbers(unittest.TestCase):
    def test_extract_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = [2, 4, 6, 8, 10]
        self.assertEqual(get_just_sonlar(numbers), expected_result)

class TestIsInFibonacciSequence(unittest.TestCase):
    def test_is_in_fibonacci_sequence(self):
        self.assertTrue(is_in_fibonacci_sequence(0))
        self.assertTrue(is_in_fibonacci_sequence(1))
        self.assertTrue(is_in_fibonacci_sequence(2))
        self.assertTrue(is_in_fibonacci_sequence(3))
        self.assertTrue(is_in_fibonacci_sequence(5))
        self.assertTrue(is_in_fibonacci_sequence(8))
        self.assertTrue(is_in_fibonacci_sequence(13))
        self.assertFalse(is_in_fibonacci_sequence(4))
        self.assertFalse(is_in_fibonacci_sequence(6))
        self.assertFalse(is_in_fibonacci_sequence(7))
        self.assertFalse(is_in_fibonacci_sequence(10))
        self.assertFalse(is_in_fibonacci_sequence(-1))

unittest.main()