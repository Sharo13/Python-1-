import threading
# 1) 1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე
def even_nums():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)
    
def odd_nums():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)
    

if __name__ == "__main__":
  
    even_thrd = threading.Thread(target=even_nums)
    odd_thrd = threading.Thread(target=odd_nums)

    even_thrd.start()
    odd_thrd.start()

    even_thrd.join()
    odd_thrd.join()

    print("Threads finished.")

# # ეკრანზე გამოტანის მეორე ვარიანტი

def even_nums():
    for i in range (30, 51, 2):
        print (f"Even Number - {i}\n")

def odd_nums():
    for i in range (31, 50, 2):
        print (f"Odd Number - {i}\n")

if __name__ == "__main__":
  
    even_thrd = threading.Thread(target=even_nums)
    odd_thrd = threading.Thread(target=odd_nums)

    even_thrd.start()
    odd_thrd.start()

    even_thrd.join()
    odd_thrd.join()

    print("Threads finished.")

# /////////////////////////////////////////
# 2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.
import threading
import requests

def download_mp3(url, fname):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(fname, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {fname}")
        else:
            print(f"Failed to download {url}.")
    except Exception :
        print(f"Error")

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=JjhHGpfXcIE",
        "https://www.youtube.com/watch?v=2zvd1JQ0EKY",
        "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
        "https://www.youtube.com/watch?v=oKOtzIo-uYw"
    ]

    threads = []

    for i, url in enumerate(urls):
        fname = f"song{i+1}.mp3"
        thread = threading.Thread(target=download_mp3, args=(url, fname))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All downloads compeleted.")
