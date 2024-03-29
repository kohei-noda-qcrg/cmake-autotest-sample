cmake_minimum_required(VERSION 3.7)
project(CMake-autotest Fortran)
set(CMAKE_VERBOSE_MAKEFILE 1)
# set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)
# set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)
option(MPI "Enable MPI?" OFF)
option(MKL "Enable MKL?" OFF)
option(OPENMP "Enable OpenMP?" ON)
option(Utest "Enable unit test?" OFF)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/bin)
enable_language(Fortran)
if(MPI)
    find_package(MPI REQUIRED)
endif()
if(OPENMP)
    find_package(OpenMP REQUIRED)
endif()
set(CMAKE_SHARED_LIBRARY_LINK_Fortran_FLAGS "")
if(CMAKE_Fortran_COMPILER_ID STREQUAL Intel)
    add_compile_options(-cpp -mkl -pad -mp1 -integer_size 64 -unroll -warn nounused -nogen-interface) # "-warn nounused" means "-warn all -warn nounused"
    link_libraries(-cpp -mkl)
    if(OPENMP)
        add_compile_options(-qopenmp)
    	link_libraries(-qopenmp)
    endif()
elseif(CMAKE_Fortran_COMPILER_ID STREQUAL GNU)
    add_compile_options(-cpp -fdefault-integer-8 -m64 -I"${MKLROOT}/include" -Wall -Wno-unused-variable)
    link_libraries(-L${MKLROOT}/lib/intel64 -lmkl_intel_ilp64 -lmkl_core -lmkl_sequential -lpthread -lm)
    if(OPENMP)
        add_compile_options(-fopenmp)
        link_libraries(-fopenmp)
    endif()
else()
endif()
if(MPI)
	add_compile_options(-DHAVE_MPI)
endif()
if(MKL)
else()
endif()
if(Utest)
endif()
# if (TARGET MPI::MPI_Fortran)
#     message("MPI")
# else()
#     message("NOT MPI")
# endif()
#set(BLA_VENDOR Intel10_64lp)
#find_package(BLAS)
#find_package(LAPACK)
add_subdirectory(src)
