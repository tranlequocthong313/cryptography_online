import sys

sys.path.append('..')

from algorithms.caesar import encrypt, decrypt


def test_encryption():
    cases = [
        {
            "text": "HEDIEUHANH",
            "key": 25,
            "expected": "GDCHDTGZMG"
        },
        {
            "text": "CONGNGHETHONGTIN",
            "key": 19,
            "expected": "VHGZGZAXMAHGZMBG"
        },
        {
            "text": "TRUONGDAIHOCMO",
            "key": 25,
            "expected": "SQTNMFCZHGNBLN"
        },
        {
            "text": "ANTOANBAOMAT",
            "key": 24,
            "expected": "YLRMYLZYMKYR"
        },
        {
            "text": "antoanbaomat",
            "key": 24,
            "expected": "YLRMYLZYMKYR"
        }
    ]

    for case in cases:
        result = encrypt(case['text'], case['key'])
        assert result == case['expected']


def test_decryption():
    cases = [
        {
            "text": "RGLFMASLEBSLE",
            "key": 24,
            "expected": "TINHOCUNGDUNG"
        },
        {
            "text": "WJPKWJDAPDKJCPDKJCPEJ",
            "key": 22,
            "expected": "ANTOANHETHONGTHONGTIN"
        },
        {
            "text": "WVJHVOCZOCJIB",
            "key": 21,
            "expected": "BAOMATHETHONG"
        },
        {
            "text": "KOUHNLCGUHA",
            "key": 20,
            "expected": "QUANTRIMANG"
        },
        {
            "text": "SEIETKBYUKDQDWSQE",
            "key": 16,
            "expected": "COSODULIEUNANGCAO"
        }
    ]

    for case in cases:
        result = decrypt(case['text'], case['key'])
        assert result == case['expected']
