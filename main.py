import requests
from pprint import pprint as pp
import json
from datetime import date
import babel.numbers



###This script will be used to fetch the national debt from the US treasury API

today = date.today()

#BASE URL
base_url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'

#ENDPOINT_EXAMPLE: /v1/accounting/od/rates_of_exchange
endpoint = '/v2/accounting/od/debt_to_penny'


#FIELDS: fields=record_date,debt_held_public_amt,intragov_hold_amt,tot_pub_debt_out_amt,src_line_nbr
fields = 'fields=record_date,tot_pub_debt_out_amt,src_line_nbr'

#SORTING
sorting = '&sort=-record_date'

#FORMAT
format = '&format=json&page[number]=1&page[size]=1'

def get_debtToThePenny():
    get_debt_request = requests.get(f'{base_url}{endpoint}?{fields}{sorting}{format}')
    #pp(get_debt_request.json())
    response = get_debt_request.json()
    return response

def main():
    data = get_debtToThePenny().get('data')
    for i in data:
        record_date = i['record_date']

        """BABEL Docs:https://stackabuse.com/format-number-as-currency-string-in-python/"""
        total_debt = babel.numbers.format_currency(i['tot_pub_debt_out_amt'], "USD", locale='en_US')

        pp(f'The current national debt as of {record_date} is {total_debt}')

if __name__ == '__main__':
    main()

