import numpy as np
import requests
from bs4 import BeautifulSoup as bs

#large table with coords
#https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub

#testing coord table
#https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub

def decoder():
    #web-scraping
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    website = requests.get(url)
    soup = bs(website.content, "html.parser")

    table = soup.find("table")
    #print(table)

    table_row = table.find_all("tr")
    #print(table_row)

    data = []
    for row in table_row:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    del data[0] #just to remove header

    for x in data:
        print(x[0])
        x[0] = int(x[0])
        x[2] = int(x[2])
        print(data)

    #initalise container array to add stuff in, basically making grid here
    current_largest_x = 0
    current_largest_y = 0
    for x in data:
        x_coord = x[0]
        y_coord = x[2]
        if x_coord > current_largest_x:
            current_largest_x = x_coord
        if y_coord > current_largest_y:
            current_largest_y = y_coord
    print()
    print(current_largest_x)
    print(current_largest_y)

    current_largest_x += 1
    current_largest_y += 1
    container = np.zeros((current_largest_x, current_largest_y), dtype=str)
    print(container)
    # container[2][1] = 5   #container[row (up n down arrays)][col (elements in array)]
    # print(container)

    # some reason this flips everything
    #ok correction, bascially does nothing
    #adding spaces for empty elements
    #correctiona gain doesnt do nothing, space everything evenly
    i = 0
    for x in container:
        j = 0
        for y in x:
            print("sdfa")
            print(y)
            if y == '':
                container[i][j] = ' '
            j += 1
        i += 1
    print(container)

    #adds the unqiue chars to array
    i = 0
    for x in data:
        row = x[0]
        col = x[2]
        # print(container)
        print(row)
        print(col)
        print()
        container[row][col] = x[1]
        print(container)

    print(container)
    print()

    # np.rot90(container)
    print(np.rot90(container))
    print()

    #more readable manner instead of array
    for array_row in np.rot90(container):
        row_string = "".join([str(y) for y in array_row if y])
        print(row_string)

decoder()