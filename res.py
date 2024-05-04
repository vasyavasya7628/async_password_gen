from enum import Enum


class Res(Enum):
    DIGITS = '0123456789'
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    SYMBOLS = "!@#$%^&*()"
    PASS_GENERATE = '🔏Сгенерировать'
