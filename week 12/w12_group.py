
with open("week 12/books_and_chapters.txt") as scripture_list:

    largest_book = 0
    largest_book_name = ""
    chosen_b_section = ""

    user_choice =  input("""
    What volume of scripture do you want to look at? 
    1. Old Testament
    2. New Testament
    3. Book of Mormon
    4. Doctrine and Covenants
    5. Pearl of Great Price
    
    """)
    if user_choice == "1":
        chosen_b_section = "Old Testament"

    elif user_choice == "2":
        chosen_b_section = "New Testament"

    elif user_choice == "3":
        chosen_b_section = "Book of Mormon"  
         
    elif user_choice == "4":
        chosen_b_section = "Doctrine and Covenants"
        
    elif user_choice == "5":
        chosen_b_section = "Pearl of Great Price"


    for line in scripture_list:
        #Genesis:50:Old Testament
        clean_list = line.strip()
        book = clean_list.split(":")

        book_name = book[0]
        book_chapters = int(book[1])
        book_section = book[2]

        if book_section == chosen_b_section:
            print(f"Scripture: {book_section}, Book: {book_name}, Chapters: {book_chapters}")

            if book_chapters > largest_book:
                largest_book = book_chapters
                largest_book_name = book_name
        
    print("*"*20)
    print(f"The largest book is {largest_book_name} with {largest_book} chapters")

