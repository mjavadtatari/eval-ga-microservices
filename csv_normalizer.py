import csv

# global variables
CSV_FILE_ADDRESS = 'nm_0_response_time.csv'
NUMBER_OF_WANTED_ROW = 100
CSV_OUTPUT_FILE_ADDRESS = CSV_FILE_ADDRESS[:-4] + '_' + str(NUMBER_OF_WANTED_ROW) + '_sample_data.csv'
CSV_MAXIMUM_VALUE = 0
NORMALIZER_SCALE = 1000
IS_POSITIVE_PARAMETER = True

csv_full_content = []
csv_out_content = []

with open(CSV_FILE_ADDRESS, 'r') as f:
    for item in csv.reader(f):
        csv_full_content.append(item)

    # column_name = rows_without_headers[0]
    # rows_without_headers.pop(0)

csv_out_content = csv_full_content[:NUMBER_OF_WANTED_ROW + 1]

for row in range(len(csv_out_content)):
    for col in range(len(csv_out_content[row])):
        try:
            csv_out_content[row][col] = int(csv_out_content[row][col])
        except ValueError as e:
            continue
    if row:
        CSV_MAXIMUM_VALUE = max(CSV_MAXIMUM_VALUE, max(csv_out_content[row][1:]))

for row in range(len(csv_out_content)):
    for col in range(len(csv_out_content[row])):
        try:
            if IS_POSITIVE_PARAMETER:
                csv_out_content[row][col] = round(((csv_out_content[row][col] / CSV_MAXIMUM_VALUE) * NORMALIZER_SCALE),
                                                  2)
            else:
                csv_out_content[row][col] = round(
                    NORMALIZER_SCALE - ((csv_out_content[row][col] / CSV_MAXIMUM_VALUE) * NORMALIZER_SCALE), 2)
        except TypeError as e:
            continue

with open(CSV_OUTPUT_FILE_ADDRESS, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    # for item in csv_out_content:
    csv_writer.writerows(csv_out_content)
