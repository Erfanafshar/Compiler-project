b1 = False:bool;
b2 = (3 < 5 < 7 < 9 > b1 > -1 >= -5):bool;
b3 = 6 < 2 and 33 == 33:bool;
b4:bool;
p1, i = 0:int;


main()
{
    print(b4);

    b4 = (b2 and ((b2 or b3) and 33 > 5 + 17 / 23)) or (True and False);
    if (b1)
        i = i + 1;
    print(i);


    i = 0;
    if (b2)
        i = i + 35;
    else
        i = i + 33;
    print(i);


    i = 0;
    while (i < 25 + 75)
        i = i + 1;
    print(i);


    i = 0;
    on(i)
    {
        where 0:
            i = i + 37;
        where 1:
            i = i + 32;
    };
    print(i);


    i = 0;

    for(p1 = 33;p1 <= 78; p1 = p1 + 1)
        i = i + 2;

    print(i);
}
