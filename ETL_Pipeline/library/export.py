from etl import ETL
import csv

select_query = 'SELECT * FROM olap_prahlad_tgt;'

table = "D_RETAIL_SLS_T"

def main():
    etl = ETL(table)
    etl.tgt_to_csv()

if __name__ == '__main__':
    main()