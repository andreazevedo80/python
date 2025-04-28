i = 1
continuar = True
while i<11:
    print(f"2 x {i} = {2 * i}")
    i += 1
    continuar = input("Deseja continuar? (s/n): ")
    continuar = True if continuar == "s" else False
    if not continuar:
        break


