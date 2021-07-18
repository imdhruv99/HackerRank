def LibraryFine(returnDate, dueDate):
    
    Dr, Mr, Yr = returnDate
    Dd, Md, Yd = dueDate
    fine = 0

    if Yr > Yd:
        fine = 10000
    elif Yr == Yd:
        if Mr > Md:
            fine = (Mr - Md) * 500
        elif Mr == Md and Dr > Dd:
            fine = (Dr -Dd) * 15

    return fine

if __name__ == "__main__":
    
    returnDate = list(map(int, input().split()))
    dueDate = list(map(int, input().split()))

    result = LibraryFine(returnDate, dueDate)
    print(result)