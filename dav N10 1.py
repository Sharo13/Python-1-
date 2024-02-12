# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე,
# შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

import requests

def get_products(url):
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        print("Error: Unable to fetch data.")
        return None

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
    
def product_prices(products):
    if not products:
        return
    
    prices = [product['price'] for product in products] 
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    
    print(f"Maximum Price: {max_price}")
    print(f"Minimum Price: {min_price}")
    print(f"Average Price: {avg_price}")

if __name__ == "__main__":
    api_url = "https://fakestoreapi.com/products"
    products = get_products(api_url)
    product_prices(products)


# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ

def sort_categories(products):
    if not products:
        return []
    
    categories = set()
    for product in products:
        category = product.get('category')
        if category:
            categories.add(category)
    
    sorted_categories = sorted(categories)
    return sorted_categories

if __name__ == "__main__":
    api_url = "https://fakestoreapi.com/products"
    
    products = get_products(api_url)
    
    if products:
        sorted_categories = sort_categories(products)
        print("List of Categories:", sorted_categories)


# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით

def id_title(products):
    if not products:
        return []
    
    id_title_list = [{'id': product['id'], 'title': product['title']} for product in products]
    sorted_list = sorted(id_title_list, key=lambda x: x['title'])
    
    return sorted_list

if __name__ == "__main__":
    api_url = "https://fakestoreapi.com/products"
    products = get_products(api_url)
    
    if products:
        sorted_list = id_title(products)
        print("Sorted List of IDs and Titles:")
        for item in sorted_list:
#             print(f"ID: {item['id']}, Title: {item['title']}")

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით

def ratings_list(products):
    if not products:
        return []
    ratings = [product['rating']['rate'] for product in products if 'rating' in product]
    sorted_ratings = sorted(ratings)
    
    return sorted_ratings

if __name__ == "__main__":
    api_url = "https://fakestoreapi.com/products"
    
    products = get_products(api_url)
    
    if products:
        sorted_list = ratings_list(products)
        print("Sorted List of Ratings:", sorted_list)
