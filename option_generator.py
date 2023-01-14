## this program creates a excel of possibilities of given inputs


import xlsxwriter
from functools import reduce

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('merge1.xlsx')
worksheet = workbook.add_worksheet()


# Create a format to use in the merged range.
merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'text_wrap': 1
    })


# Merge 3 cells.
# worksheet.merge_range('B4:D4', 'Merged Range', merge_format)

# Merge 3 cells over two rows.
#worksheet.merge_range('B7:D8', 'Merged Range', merge_format)

inputs = {
    "kafka_version":['2x','3x'],
    "logstash_compatible":['yes','no'],
    "nodejs_library_compatible":['yes','no'],
    "other_Team_compatible":["yes","no"],
}

total_columns = len(inputs)
total_rows = 1
ordered_keys = list(inputs.keys())
ordered_sizes = list(map(lambda key: len(inputs[key]), ordered_keys))
total_rows = reduce(lambda x,y: x*y,ordered_sizes)

#this solution is limited to 26 options only

# traverse all keys in input
for index in range(len(ordered_keys)):
    option = ordered_keys[index]
    #decide how many cells to merge
    #vertically each cell is merge of product of number of options below it
    if index==len(ordered_sizes)-1:
        curr_level_merge_size=1
    else:
        #find product of size of options after current option
        curr_level_merge_size = reduce(lambda x,y: x*y, ordered_sizes[index+1:])

    print(curr_level_merge_size)
    current_column = chr(ord('A')+index)
    #leaving 1 row for header
    worksheet.write(0, index, ordered_keys[index], merge_format)
    #for merged cells take indexing from 1, so starting from second row
    start_row=2
    print(current_column)
    #repeat till total_rows are filled with repetition
    while start_row<=total_rows:
        #repeat on each element of a given option
        for item in range(ordered_sizes[index]):
            print(inputs[option][item])
            #generate ranges to merge
            #end the merge at 1 row less than the sum
            range_to_merge='{}{}:{}{}'.format(current_column,start_row,current_column,start_row+curr_level_merge_size-1)
            print(range_to_merge)
            #merge is only required for other than last option
            if(curr_level_merge_size>1):
                worksheet.merge_range(range_to_merge,inputs[option][item] , merge_format)
            else:
                #for last option cells are not merged, values for last option are just repeated
                print('total_row {} start_row {}'.format(total_rows,start_row))
                #because in write function rows and columns are zero indexed
                #so start row is decremented by 1
                worksheet.write(start_row-1, index,inputs[option][item], merge_format)

            start_row=start_row+curr_level_merge_size

workbook.close()
