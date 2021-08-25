a1 = 0,a4 = 0,a9 = 0:int;
main()
{
    arr[8]:int;
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = -1;
    arr[4] = -2;
    arr[5] = 3;
    arr[6] = 7;
    arr[7] = 0;


    for(x in arr)
    {
        if(x * x == 0)
            print(a9);
        elseif(x * x == 1)
            a1 = a1 + 1;
        elseif(x * x == 4)
            a4 = a4 + 1;
        else
            a9 = a9 + 1;
    }
    print(a1);
    print(a4);
    print(a9);

    for(x in arr)
    {
        on(x * x)
        {
            where 1:
                a1 = a1 + 1;
            73;

            where 4:
                a4 = a4 + 1;

            where 9:
                a9 = a9 + 1;

            where 0:
                print(a9);

        };
    }
    print(a1);
    print(a4);
    print(a9);

    x5,y5,x3,x2,x1:int;
    x5=y5=2+x3=1+x2=2*x1=(2+2)%3;
    a[x5 + x3],i:int;
    for(i=0;i<8;i=i+1)
        a[i] = i + (i % 3 == 2) ;
    long_live_the_king=True:bool;
    result = 0:int;
    for(i in a)
        if(i % 2 == 0)
            result = result + 1;

    if(result<10)
        if(result<1)
            print(long_live_the_king);
        else
            print(result);

    long_live_the_king = arr[0] <= arr[1] <= arr[2] and arr[5] <= arr[6] <= arr[7];
    print(long_live_the_king);
    long_live_the_king = long_live_the_king != 2 and arr[0] <= arr[1] <= arr[2] >= arr[6];
    print(long_live_the_king);
}
