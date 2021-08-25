fun fib(a:int):int
{
    if(a < 2)
        return 1;
    return fib(a - 2) + fib(a - 1);
}

fun c(a:int, b:int):int
{
    if(a >= b)
        return a == b;
    x = b - 1,v1 = c(a, x):int;
    a = a - 1;
    return v1 + c(a, x);
}

fun c_minus_fib(a[]:int)
{
    for(b in a)
    {
        x = fib(b) - c(b, b/2);
        print(x);
    }
}

main()
{
    a[5],i,counter = 5:int;
    for(i = 1; counter = counter -1; i = i + (i % 3) + 1)
        a[counter] = i;
    c_minus_fib(a);
}
