from algorithms.vigenere import encrypt, decrypt

def test_encryption():
    cases = [
        {
            "text": "KHOACONGNGHETHONGTIN",
            "key": "KEY",
            "expected": "ULMKGMXKLQLCDLMXKRSR"
        },
        {
            "text": "HETHONGTHONGTIN",
            "key": "SECRET",
            "expected": "ZIVYSGYXJFRZLMP"
        },
        {
            "text": "KHOACONGNGHETHONGTIN",
            "key": "SECRET",
            "expected": "CLQRGHFKPXLXLLQEKMAR"
        },
        {
            "text": "ANTOANBAOMATTHONGTIN",
            "key": "MONARCHY",
            "expected": "MBGORPIYAANTKJVLSHVN"
        },
    ]

    for case in cases:
        result = encrypt(case['text'], case['key'])
        assert result == case['expected']


def test_decryption():
    cases = [
        {
            "text": "SIHWMMTOCNSTPB",
            "key": "MAHOA",
            "expected": "GIAIMATHONGTIN"
        },
        {
            "text": "DOONRWVOWHBGDLBBKJ",
            "key": "KHOA",
            "expected": "THANHPHOMANGTENBAC"
        },
        {
            "text": "WRCVBIPVMGBQZ",
            "key": "TRUONGDH",
            "expected": "DAIHOCMOTPHCM"
        },
        {
            "text": "LPAADJBTUTUFMYWVVS",
            "key": "BIMAT",
            "expected": "KHOAKITHUATXAYDUNG"
        },
        {
            "text": "MBAIEJOCFVBNX",
            "key": "MONARCHY",
            "expected": "ANNINHHETHONG"
        },
        {
            "text": "LZKINTMYIBTZBE",
            "key": "TRUONG",
            "expected": "SIQUANTHONGTIN"
        }
    ]

    for case in cases:
        result = decrypt(case['text'], case['key'])
        assert result == case['expected']
