fun fib(a:int):int
{
    if(a < 2)
        return 1;
    return fib(a - 2) + fib(a - 1);
}

fun test_all(x[]:int, result:int):int
{
    for(a in x)
        if(a > 15)
        {
            print(a);
            y = 0:int;
            for(b in x)
                for(c in x)
                    if(b > c)
                        while(b > y = y + 1 <= c and y < b - c)
                            on(y - 5 * (y %2))
                            {
                                where 20:
                                    print(b);
                                where 30:
                                    print(c);
                                where 40:
                                    result = result + 1;
                                where 50:
                                    print(result);
                            };
                    else
                        y = c - b;
        }
        else
        {
            v = a:int;
            while(v = v - 1)
                result = result + (v != 5 and v > 2);
        }
    return result;
}

main()
{
    x[10], i, result = 0:int;
    for(i = 0;i < 10; i = i + 1)
        x[i] = i * i - i / 2 + (i > 5 and (i % 7) * (i % 3) < 10) - (i % 6) * (i % 7) * 8;
    result = test_all(x, result);
    print(result);
    for(i = 0;i < 10; i = i + 1)
        x[i] = fib(i + (i % 4));
    result = test_all(x, i);
    print(result);

}
