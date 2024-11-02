import pandas as pd

def display_cumulative_product_views(file_path):
    # Reading the CSV file
    # file_path = "Product_View_Analysis.csv"
    data = pd.read_csv(file_path)

    df = pd.DataFrame(data)

    # Defining constants for column names
    PRODUCT_VIEW_COUNT = 'Product View Count'
    PARENT_ORG = 'Parent org'

    # Using Group by 'Parent org' and 'Brand' to calculate the cumulative product view count
    cumulative_view_counts = df.groupby([PARENT_ORG, 'Brand'])[PRODUCT_VIEW_COUNT].sum().reset_index()

    # Calculate total cumulative view count per Parent org
    parent_org_totals = cumulative_view_counts.groupby(PARENT_ORG)[PRODUCT_VIEW_COUNT].sum().reset_index()


    # Sorting the result in descending order of product view count
    sorted_cumulative_view_counts = parent_org_totals.sort_values(by=PRODUCT_VIEW_COUNT, ascending=False)


    # Printing each Parent org with its brands in sorted order
    for _, org_row in sorted_cumulative_view_counts.iterrows():
        parent_org = org_row[PARENT_ORG]
        parent_org_total = org_row[PRODUCT_VIEW_COUNT]

        # Printing the Parent org and its cumulative product view count
        print(f"{parent_org} : {parent_org_total}")

        # Filtering out the brands for this Parent org and sorting them by product view count in descending order
        org_brands = cumulative_view_counts[cumulative_view_counts[PARENT_ORG] == parent_org]
        org_brands_sorted = org_brands.sort_values(by=PRODUCT_VIEW_COUNT, ascending=False)

        # Printing each brand and its cumulative product view count under the Parent org
        for _, brand_row in org_brands_sorted.iterrows():
            brand = brand_row['Brand']
            brand_view_count = brand_row[PRODUCT_VIEW_COUNT]
            print(f"  {brand} : {brand_view_count}")


if __name__ == '__main__':
    # Replace 'Product_View_Analysis.csv' with the path to your CSV file
    display_cumulative_product_views("Product_View_Analysis.csv")