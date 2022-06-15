program main
    implicit none
    integer :: i
    i = 0
    print *, i
    open (1, file="inp", form='formatted')
    read (1) i
    close (1)
    open (10, file='test.out', status='replace')
    write (10, *) i
    write (10, *) "CASCI ENERGY FOR  3 STATE"
    write (10, *) "   1           -76.119935758767198"
    write (10, *) "   2           -55.727719796153636"
    write (10, *) "   3           -55.721134757568819"
    write (10, *) "Root =    1"
    write (10, *) "computational time =   0day  0h   0min  0.033sec"
    write (10, *) "c^2              3.065111435116293"
    write (10, *) "weight of 0th wave function is             0.245995716467092"
    write (10, *) "Total second order energy is             -1.732500214377024 a.u."
    write (10, *) ""
    write (10, *) "Total energy is            -57.460220010530662 a.u."
    close (10)
end program main
