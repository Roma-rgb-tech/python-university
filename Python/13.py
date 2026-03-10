def library_analysis():
    library = {}
    
    while True:
        try:
            count = int(input("Введіть кількість книг у бібліотеці: "))
            if count < 0:
                print("Кількість не може бути від’ємною. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Помилка: будь ласка, введіть ціле число.")

    if count == 0:
        print("Бібліотека порожня. Аналіз неможливий.")
        return


    for i in range(count):
        print(f"\nВведенн даних для книги №{i + 1}:")
        title = input("Назва книги: ").strip()
        author = input("Автор: ").strip()
        
        while True:
            try:
                pages = int(input("Кількість сторінок: "))
                if pages <= 0:
                    print("Кількість сторінок має бути більшою за 0.")
                    continue
                break
            except ValueError:
                print("Помилка: введіть числове значення для кількості сторінок.")
        
        library[title] = (author, pages)


    total_pages = sum(info[1] for info in library.values())
    average_pages = total_pages / len(library)

    print(f"\n--- Результати аналізу ---")
    print(f"Середня кількість сторінок: {average_pages:.2f}")


    below_average = [title for title, info in library.items() if info[1] < average_pages]

    if below_average:
        print("Книги, що мають менше сторінок, ніж у середньому:")
        for title in below_average:
            author, pages = library[title]
            print(f"- '{title}' (Автор: {author}, сторінок: {pages})")
    else:
        print("Книг з кількістю сторінок меншою за середню не знайдено.")

if __name__ == "__main__":
    library_analysis()
    
    
    

    
    
    
    