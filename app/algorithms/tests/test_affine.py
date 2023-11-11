from algorithms.affine import encrypt, decrypt, modinv

def test_encryption():
    cases = [
        {
            "text": "CRYPTO",
            "key": [5, 3],
            "expected": "NKTAUV"
        },
        {
            "text": "HELLO",
            "key": [7, 2],
            "expected": "ZEBBW"
        },
        {
            "text": "TRUONGDAIHOCMO",
            "key": [11, 8],
            "expected": "JNUGVWPISHGEKG"
        },
    ]

    for case in cases:
        result = encrypt(case['text'], case['key'])
        assert result == case['expected']


def test_decryption():
    cases = [
        {
            "text": "NKTAUV",
            "key": [5, 3],
            "expected": "CRYPTO"
        },
        {
            "text": "ZEBBW",
            "key": [7, 2],
            "expected": "HELLO",
        },
        {
            "text": "JNUGVWPISHGEKG",
            "key": [11, 8],
            "expected": "TRUONGDAIHOCMO",
        },
    ]

    for case in cases:
        result = decrypt(case['text'], case['key'])
        assert result == case['expected']


def test_modinv():
    cases = [
        {
            "a": 3,
            "m": 26,
            "expected": 9
        },
        {
            "a": 7,
            "m": 26,
            "expected": 15
        },
        {
            "a": 11,
            "m": 26,
            "expected": 19
        },
    ]

    for case in cases:
        result = modinv(case['a'], case['m'])
        assert result == case['expected']
