/* *************************************************
*  Name: Alexander Katrompas
*  Assignment: Demonstration Code
*  Purpose: A demonstration of a properly
*           constructed and commented main.cpp
************************************************* */

#include "main.h"

int main() {
/* **********************************
 * This function is the application driver. It uses
 * and tests the functions and Square modules.
 *
 * @param na : na
 * @return (int) : application exit code
 * @exception na : na
 * @note na
 * **********************************/

    Square square1(10); // normally, DO NOT use literals
    Square square2(5);  // these are used only for demonstation

    reportSquares(square1, square2);

    square2.setLength(20);
    reportSquares(square1, square2);

    square1.setLength(1);
    square2.setLength(-12);
    reportSquares(square1, square2);

    return 0;
}
