program single

   implicit none

   integer :: iunit = 13
   real(4) :: f(4)
   integer :: i(4)

   open(iunit, file="single.dat", access="sequential", form="unformatted")
   rewind(iunit)

   read(iunit) f
   write(*, *) f

   read(iunit) i
   write(*, *) i

   read(iunit) f
   write(*, *) f

   close(iunit)

end program
