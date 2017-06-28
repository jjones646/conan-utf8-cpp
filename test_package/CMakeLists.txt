cmake_minimum_required( VERSION  3.0 )

project( Utf8CppPackageTest
         VERSION       0.0.1
         LANGUAGES     C  CXX
)

# set c++ std version
set( CMAKE_CXX_STANDARD  14 )
# don't fail if c++14 is not available
set( CMAKE_CXX_STANDARD_REQUIRED  OFF )
# disable compiler-specific extensions
set( CMAKE_CXX_EXTENSIONS  OFF )

include( "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake" )
conan_basic_setup( TARGETS )

add_executable( Utf8CppPackageTest
    main.cpp
)
target_link_libraries( Utf8CppPackageTest
    PRIVATE  CONAN_PKG::utf8-cpp
)
