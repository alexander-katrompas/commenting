/* *************************************************
*  Name: Alexander Katrompas
*  Assignment: Demonstration Code
*  Purpose: A demonstration of a properly
*           constructed and commented main.cpp
************************************************* */

#include "main.h"

int main() {


    Square square1(5);
    Square square2(10);

    std::cout << "The area of the square is: " << square1.getArea() << std::endl;
    std::cout << "The area of the square is: " << square2.getArea() << std::endl;
    std::cout << "Compare squares: " << compareSquares(square1,square2) << std::endl;
    std::cout << "Compare squares: " << compareSquares(square2,square1) << std::endl;


    return 0;
}