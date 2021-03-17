# # Read only

def read_only():
    ''' a method that only read the file '''
    try:
        file1 = open('data.txt', 'r') # read only
        text = file1.read()
        print(text)
        file1.close() # the reason for closing
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    '''A method that writes to a file'''
    # if file exist, it will be overwritten
    # if file does not exist, it will be created
    file2 = open('more_data.txt', 'w')
    file2.write('tomatoes')
    file2.close()

# python will know to close this file (even if there are errors)
# with open('jumbo.txt') as f:
#     txt = f.read()
#     print(txt)

def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            # food_sale (each element in list)
            split_food_sale = food_sale.split(',')
            
            order_date = split_food_sale[0]
            print(order_date)
            # append order_date to all_dates list
            all_dates.append(order_date)
    print(all_dates)
    
    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def append_text():
    '''Append data to an existing file'''
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')


if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    append_text()