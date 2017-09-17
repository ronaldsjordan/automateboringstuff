tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    rows = len(tableData[0])
    columns = len(tableData)

    # Determine the longest element in each inner string.
    for i in range(columns): # 0 - 2
        for j in range(rows): # 0 - 3
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    # Print the table right-justified
    for i in range(rows): # 0 - 3
        for j in range(columns): # 0 - 2
            print(tableData[j][i].rjust(colWidths[j] + 1),end='')
        print('')

printTable(tableData)