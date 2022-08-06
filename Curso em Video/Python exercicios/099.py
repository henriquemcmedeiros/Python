def maior(*num):
    mai = 0
    print(f"A quantidade de números é de {len(num)}, sendo eles {num}")
    for n in num:
        if n > mai:
            mai = n
    print(f"O maior número é {mai}")

maior(7, 8, 12, 0, 1)
maior(7, 8, 1)
maior(7)
maior(7, 8, 0, 1)
maior()