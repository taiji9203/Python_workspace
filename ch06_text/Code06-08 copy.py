import csv


with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singer165.csv", "w", newline='') as outFp:

            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            for inStr in csvReaderA:
                if int(row_list[6]) >= 165 :
                    row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                    row_str = ','.join(map(str, row_list))
                    outFp.write(row_str + '\n')

            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')