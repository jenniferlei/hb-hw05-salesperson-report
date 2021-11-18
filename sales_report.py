# """Generate sales report showing total melons each salesperson sold."""

# # set salespeople and melons_sold as empty lists
# salespeople = []
# melons_sold = []

# # open the sales report file and assign to variable f
# f = open('sales-report.txt')

# # for every line in the file
# for line in f:
#     # remove the extra right whitespace and separate each line by "|" and assign the list to variable entries
#     line = line.rstrip()
#     entries = line.split('|')

#     # assign the first item in the entries list to salesperson variable
#     salesperson = entries[0]
#     # assign the third item and convert to integer in the entries list to melons variable
#     melons = int(entries[2])

#     # if salesperson is in the salespeople list,
#     # find in the index position of the salesperson in salespeople list and update melons at the same position
#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)

#         melons_sold[position] += melons
#     # else if salesperson is not in the salespeople list,
#     # add salesperson to end of salespeople list and melons to end of melons sold list
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # for each index of the salespeople list, print salesperson and how many melons they sold
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#### ALTERNATIVE ####
def melons_by_salesperson(path):
    '''Return a dictionary of {salesperson_name: melons_sold}.

    Arguments:
        path (str) - the path to a sales report log file

    Return:
        melons_by_sales (dict)
    '''

    # set melons_sold as empty dictionary
    melons_by_sales = {}

    with open(path) as f:
        for line in f:
            # remove the extra right whitespace and separate each line by "|" and assign the list to variable entries
            entries = line.rstrip().split('|')

            salesperson, _, melons = entries
            melons = int(melons)

            # at salesperson key, get the existing num melons and add num melons to value
            melons_by_sales[salesperson] = melons_by_sales.get(salesperson, 0) + melons


def print_melons_by_salesperson(melons_by_sales_dict):
    '''Print a report of salespeople and total num of melons they sold.

    Arguments:
        melons_by_sales_dict (dict) - {salesperson_name: melons_sold}
    '''
    # for each index of the salespeople list, print salesperson and how many melons they sold
    for salesperson, melons in melons_by_sales_dict_sold.items():
        print(f'{salesperson} sold {melons} melons')


print_melons_by_salesperson(melons_by_salesperson('sales-report.txt'))