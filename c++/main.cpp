/**
* Name: Alexander Katrompas
 * Assignment: Demonstration Code
 * Purpose: Demonstrates a properly constructed and
 *          commented main.cpp file.
 */

#include "main.h"

/**
 * Serves as the application driver and demonstrates
 * the functions and Square modules.
 *
 * @param none
 * @exception none
 * @return application exit code
 * @note none
 */
int main() {
    Square square1(10); // Demonstration values; normally avoid literals.
    Square square2(5);

    reportSquares(square1, square2);

    square2.setLength(20);
    reportSquares(square1, square2);

    square1.setLength(1);
    square2.setLength(-12);
    reportSquares(square1, square2);

    return 0;
}