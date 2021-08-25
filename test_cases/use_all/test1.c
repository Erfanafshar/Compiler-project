result = 0,m = 0:int;

fun mul_2_res()
{
    result = result * 2;
}

fun plus_1_res()
{
    result = result + 1;
}

fun make_m_eq_to_re()
{
    m = result;
}

fun use_3_funs():int
{
    mul_2_res();
    plus_1_res();
    print(result);
    make_m_eq_to_re();
    print(m);
    return m;
}

main()
{
    v=use_3_funs();
    print(v);
    v=use_3_funs();
    print(v);
    print(m);
    print(result);
    use_3_funs();


}
