from country import *
from region import *
from customer import *
from category import *
from product import *
from subcategory import *
from sales import *
from location import *
def main():
    load_country_to_tgt()
    load_region_to_tgt()
    load_customer_to_tgt()
    load_category_to_tgt()
    load_subcategory_to_tgt()
    load_product_to_tgt()
    load_location_to_tgt()
    load_sales_to_tgt()
if __name__ == '__main__':
    main()