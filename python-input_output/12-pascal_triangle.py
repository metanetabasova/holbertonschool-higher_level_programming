#!/usr/bin/python3
def pascal_triangle(n):
    '''
    n olculu Paskal ucbucagini temsil eden siyahilarin siyahisini qaytarir.
    '''
    if n <= 0:
        return []

    # Ucbucagin ilkin veziyyeti triangle = [[1]]

    while len(triangle) < n:
        # Sonuncu yaradilmis setri gotururuk
        prev_row = triangle[-1]

        # Yeni setri formallasdiririq : hemise 1 ile baslayir
        new_row = [1]

        # Evvelki setrin daxili elementlerini toplayiriq
        for i in range(len(prew_row) - 1):
            new_row.append(prev_row[i] + prev_row[i+1])

        # Yeni setri 1 ole bitiririk
        new_row.append(1)

        #Tamamlanmis setri ucbucaga elave edirikk
        triangle.append(new_row)

    return triangle
