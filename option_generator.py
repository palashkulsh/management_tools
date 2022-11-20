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
    })


# Merge 3 cells.
# worksheet.merge_range('B4:D4', 'Merged Range', merge_format)

# Merge 3 cells over two rows.
#worksheet.merge_range('B7:D8', 'Merged Range', merge_format)

inputs = {
    "A":['a1','a2','a3'],
    "B":['b1','b2','b3'],
    "C":['c1','c2','c3'],
    "d":["d1","d2"],
    "e":["e1",'e2','e3','e4']
}

total_columns = len(inputs)
total_rows = 1
ordered_keys = list(inputs.keys())
ordered_sizes = list(map(lambda key: len(inputs[key]), ordered_keys))
total_rows = reduce(lambda x,y: x*y,ordered_sizes)

#this solution is limited to 26 options only
for index in range(len(ordered_keys)):
    option = ordered_keys[index]
    if index==len(ordered_sizes)-1:
        curr_level_merge_size=1
    else:
        #find product of size of options after current option
        curr_level_merge_size = reduce(lambda x,y: x*y, ordered_sizes[index+1:])

    print(curr_level_merge_size)
    current_column = chr(ord('A')+index)
    start_row=2
    print(current_column)
    while start_row<total_rows:
        for item in range(ordered_sizes[index]):
            print(inputs[option][item])
            range_to_merge='{}{}:{}{}'.format(current_column,start_row,current_column,start_row+curr_level_merge_size-1)
            print(range_to_merge)
            if(curr_level_merge_size>1):
                worksheet.merge_range(range_to_merge,inputs[option][item] , merge_format)
            else:
                #because in write function rows and columns are zero indexed
                worksheet.write(start_row-1, index,inputs[option][item])

            start_row=start_row+curr_level_merge_size

workbook.close()
