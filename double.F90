program double

   implicit none

   integer :: iunit = 13
   real(8) :: f(4)
   integer :: i(4)

   f(1) = 1.0d0
   f(2) = 2.0d0
   f(3) = 3.0d0
   f(4) = 4.0d0

   i(1) = 1
   i(2) = 2
   i(3) = 3
   i(4) = 4

   open(iunit, file="double.dat", access="sequential", form="unformatted")
   rewind(iunit)
   write(iunit) f
   write(iunit) i
   write(iunit) f
   close(iunit)

end program
