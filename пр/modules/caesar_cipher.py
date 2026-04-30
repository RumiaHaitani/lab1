
import string

RUS_LOW = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ENG_LOW = string.ascii_lowercase

def _shift_char(ch: str, shift: int, alphabet: str) -> str:
    idx = alphabet.find(ch)
    if idx == -1:
        return ch
    new_idx = (idx + shift) % len(alphabet)
    return alphabet[new_idx]

def cipher(text: str) -> str:

    if not text or not text.strip():
        raise ValueError("Текст не должен быть пустым.")

    shift_input = input("Введите сдвиг (целое число): ")
    try:
        shift = int(shift_input)
    except ValueError:
        raise ValueError("Сдвиг должен быть целым числом.")

    mode = input("Режим: 1 - шифровать, 2 - дешифровать: ").strip()
    if mode == '2':
        shift = -shift

    result = []
    for ch in text:
        if ch.isupper():
            lower_ch = ch.lower()
            if lower_ch in RUS_LOW:
                shifted = _shift_char(lower_ch, shift, RUS_LOW).upper()
            elif lower_ch in ENG_LOW:
                shifted = _shift_char(lower_ch, shift, ENG_LOW).upper()
            else:
                shifted = ch
            result.append(shifted)
        elif ch.islower():
            if ch in RUS_LOW:
                shifted = _shift_char(ch, shift, RUS_LOW)
            elif ch in ENG_LOW:
                shifted = _shift_char(ch, shift, ENG_LOW)
            else:
                shifted = ch
            result.append(shifted)
        else:
            result.append(ch)
    return "".join(result)