a4 = 0, a9 = 0, a1 = 0 , d[10]:int;
fun is_sorted_seq(x:int, y:int, z:int):bool
{
	return x <= y <= z or x >= y >= z;
}

fun number_of_even_integers(arr[]:int):int
{
	result = 0:int;
	for(i in arr)
		if(i % 2 == 0)
			result = result + 1;
	return result + is_sorted_seq(arr[0], arr[1], arr[2]) + is_sorted_seq(arr[5], arr[4], arr[6]);
}

fun a_void_sample_use_on_where(x:int)
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

fun a_void_sample_use_if_else(x:int)
{
	long_live_the_queen:bool;

	if(x * x == 0)
		print(a9);
	elseif(x * x == 1)
		a1 = a1 + 1;
	elseif(x * x == 4)
		a4 = a4 + 1;
	else
	{
		a9 = a9 + 1;
		long_live_the_queen;
	}
}

main()
{
	x5,y5,x3,x2,x1:int ;
	x5=y5=2+x3=1+x2=2*x1=(2+2)/3;

	a[x5 + x3],i:int;
	for(i=0;i<8;i=i+1)
		a[i] = i + (i % 3 == 2) ;
	long_live_the_king=True:bool;
	result=number_of_even_integers(a):int;
	if(result<10)
		if(result<1)
			print(long_live_the_king);
		else
			print(result);
}
