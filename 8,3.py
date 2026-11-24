def rektangel_area(bredd, hojd):
    area = bredd * hojd
    return area

bredd = int(input("Vad är bredden på rektangeln?"))
hojd = int(input("Vad är höjden på triangeln?"))

area = rektangel_area(bredd, hojd)

print(area)