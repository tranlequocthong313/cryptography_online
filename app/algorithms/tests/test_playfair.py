from algorithms import playfair


def test_encryption():
    cases = [
        {
            "text": "INSTRUMENTS",
            "key": "MONARCHY",
            "expected": "GATLMZCLRQXA"
        },
        {
            "text": "ABC",
            "key": "MONARCHY",
            "expected": "BIBU"
        },
        {
            "text": "ADC",
            "key": "MONARCHY",
            "expected": "RBBU"
        },
        {
            "text": "TRUONGDAIHOCMO",
            "key": "MONARCHY",
            "expected": "ZDVMYQBRFBMHON"
        },
        {
            "text": "ANTOANTHONGTIN",
            "key": "MONARCHY",
            "expected": "RAPRRAPDNAKQGA"
        },
        {
            "text": "JUSTDOIT",
            "key": "MONARCHY",
            "expected": "EXTLHRKS"
        },
        {
            "text": "TRUONGDAIHOCMO",
            "key": "JUSTDOIT",
            "expected": "DQIAWNUESFAEVF"
        },
        {
            "text": "BALLOON",
            "key": "KKKK",
            "expected": "CBNVMPPO"
        },
    ]

    for case in cases:
        result = playfair.encrypt(case['text'], case['key'])
        assert result == case['expected']


def test_decryption():
    cases = [
        {
            "text": "BIBU",
            "key": "MONARCHY",
            "expected": "ABCX"
        },
        {
            "text": "RBBU",
            "key": "MONARCHY",
            "expected": "ADCX"
        },
        {
            "text": "ZDVMYQBRFBMHON",
            "key": "MONARCHY",
            "expected": "TRUONGDAIHOCMO"
        },
        {
            "text": "RAPRRAPDNAKQGA",
            "key": "MONARCHY",
            "expected": "ANTOANTHONGTIN"
        },
        {
            "text": "GATLMZCLRQXA",
            "key": "MONARCHY",
            "expected": "INSTRUMENTSX"
        },
        {
            "text": "ZOBATCZISN",
            "key": "KEY",
            "expected": "THAYPHUONG"
        },
        {
            "text": "IKBR",
            "key": "KEY",
            "expected": "CUYT"
        },
        {
            "text": "EXTLHRKS",
            "key": "MONARCHY",
            "expected": "IUSTDOIT"
        },
        {
            "text": "DQIAWNUESFAEVF",
            "key": "JUSTDOIT",
            "expected": "TRUONGDAIHOCMO",
        },
        {
            "text": "CBNVMPPO",
            "key": "KKKK",
            "expected": "BALXLOON",
        },
    ]

    for case in cases:
        result = playfair.decrypt(case['text'], case['key'])
        assert result == case['expected']


def test_generate_matrix():
    cases = [
        {
            "key": "MONARCHY",
            "expected": [["M", "O", "N", "A", "R"], 
                         ["C", "H", "Y", "B", "D"],
                         ["E", "F", "G", "I", "K"],
                         ["L", "P", "Q", "S", "T"],
                         ["U", "V", "W", "X", "Z"]]
        },
        {
            "key": "MONARCHY",
            "expected": [["M", "O", "N", "A", "R"], 
                         ["C", "H", "Y", "B", "D"],
                         ["E", "F", "G", "I", "K"],
                         ["L", "P", "Q", "S", "T"],
                         ["U", "V", "W", "X", "Z"]]
        },
        {
            "key": "JUSTDOIT",
            "expected": [["I", "U", "S", "T", "D"], 
                         ["O", "A", "B", "C", "E"],
                         ["F", "G", "H", "K", "L"],
                         ["M", "N", "P", "Q", "R"],
                         ["V", "W", "X", "Y", "Z"]]
        },
    ]

    for case in cases:
        result = playfair.generate_matrix(case['key'])
        assert result == case['expected']


def test_make_pairs():
    cases = [
        {
            "text": "ABC",
            "expected": "ABCX"
        },
        {
            "text": "ADC",
            "expected": "ADCX"
        },
        {
            "text": "TRUONGDAIHOCMO",
            "expected": "TRUONGDAIHOCMO"
        },
        {
            "text": "ANTOANTHONGTIN",
            "expected": "ANTOANTHONGTIN"
        },
    ]

    for case in cases:
        result = playfair.make_pairs(case['text'])
        assert result == case['expected']


def test_find_indexes():
    cases = [
        {
            "text": "ABCX",
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": [[0, 3], [1, 3], [1, 0], [4, 3]]
        },
        {
            "text": "ADCX",
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": [[0, 3], [1, 4], [1, 0], [4, 3]]
        },
        {
            "text": "TRUONGDAIHOCMO",
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": [[3, 4], [0, 4], [4, 0], [0, 1], [0, 2], [2, 2], [1, 4], [0, 3], [2, 3], [1, 1], [0, 1], [1, 0], [0, 0], [0, 1]]
        },
        {
            "text": "ANTOANTHONGTIN",
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": [[0, 3], [0, 2], [3, 4], [0, 1], [0, 3], [0, 2], [3, 4], [1, 1], [0, 1], [0, 2], [2, 2], [3, 4], [2, 3], [0, 2]]
        },
    ]

    for case in cases:
        result = playfair.find_indexes(case['text'], case['matrix'])
        assert result == case['expected']


def test_shift_indexes():
    cases = [
        {
            "indexes": [[0, 3], [1, 3], [1, 0], [4, 3]],
            "backward": False,
            "expected": [[1, 3], [2, 3], [1, 3], [4, 0]],
        },
        {
            "indexes": [[0, 3], [1, 4], [1, 0], [4, 3]],
            "backward": False,
            "expected": [[0, 4], [1, 3], [1, 3], [4, 0]],
        },
        {
            "indexes": [[3, 4], [0, 4], [4, 0], [0, 1], [0, 2], [2, 2], [1, 4], [0, 3], [2, 3], [1, 1], [0, 1], [1, 0], [0, 0], [0, 1]],
            "backward": False,
            "expected": [[4, 4], [1, 4], [4, 1], [0, 0], [1, 2], [3, 2], [1, 3], [0, 4], [2, 1], [1, 3], [0, 0], [1, 1], [0, 1], [0, 2]]
        },
        {
            "indexes": [[0, 3], [0, 2], [3, 4], [0, 1], [0, 3], [0, 2], [3, 4], [1, 1], [0, 1], [0, 2], [2, 2], [3, 4], [2, 3], [0, 2]],
            "backward": False,
            "expected": [[0, 4], [0, 3], [3, 1], [0, 4], [0, 4], [0, 3], [3, 1], [1, 4], [0, 2], [0, 3], [2, 4], [3, 2], [2, 2], [0, 3]]
        },
        {
            "indexes": [[1, 3], [2, 3], [1, 3], [4, 0]],
            "backward": True,
            "expected": [[0, 3], [1, 3], [1, 0], [4, 3]],
        },
        {
            "indexes": [[0, 4], [1, 3], [1, 3], [4, 0]],
            "backward": True,
            "expected": [[0, 3], [1, 4], [1, 0], [4, 3]],
        },
    ]

    for case in cases:
        playfair.shift_indexes(case['indexes'], case['backward'])
        assert case['indexes'] == case['expected']


def test_get_string():
    cases = [
        {
            "indexes": [[0, 3], [1, 3], [1, 0], [4, 3]],
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": "ABCX"
        },
        {
            "indexes": [[0, 3], [1, 4], [1, 0], [4, 3]],
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": "ADCX"
        },
        {
            "indexes": [[3, 4], [0, 4], [4, 0], [0, 1], [0, 2], [2, 2], [1, 4], [0, 3], [2, 3], [1, 1], [0, 1], [1, 0], [0, 0], [0, 1]],
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": "TRUONGDAIHOCMO"
        },
        {
            "indexes": [[0, 3], [0, 2], [3, 4], [0, 1], [0, 3], [0, 2], [3, 4], [1, 1], [0, 1], [0, 2], [2, 2], [3, 4], [2, 3], [0, 2]],
            "matrix": [
                ["M", "O", "N", "A", "R"], 
                ["C", "H", "Y", "B", "D"],
                ["E", "F", "G", "I", "K"],
                ["L", "P", "Q", "S", "T"],
                ["U", "V", "W", "X", "Z"]
            ],
            "expected": "ANTOANTHONGTIN"
        },
    ]

    for case in cases:
        result = playfair.get_string(case['indexes'], case['matrix'])
        assert result == case['expected']

