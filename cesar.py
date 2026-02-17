#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cesar_encriptar(text: str, key: int) -> str:
    key = key % 26
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + key) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            result.append(ch)

    return ''.join(result)

def cesar_descifrar(text: str, key: int) -> str:
    return cesar_encriptar(text, -key)

def main():
    print("=== Cifrado César ===")
    mode = input("Modo (cifrar/descifrar): ").strip().lower()
    key = int(input("Llave numérica: ").strip())
    text = input("Texto: ")

    if mode in ("cifrar", "c", "encrypt", "e"):
        print("Resultado:", cesar_encriptar(text, key))
    elif mode in ("descifrar", "d", "decrypt"):
        print("Resultado:", cesar_descifrar(text, key))
    else:
        print("Modo no válido. Usa cifrar o descifrar.")

if __name__ == "__main__":
    main()
