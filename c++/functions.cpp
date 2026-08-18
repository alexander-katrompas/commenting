/**
 * Name: Alexander Katrompas
 * Assignment: Demonstration Code
 * Purpose: Demonstrates a properly constructed and
 *          commented functions.cpp file.
 */

#include <stdio.h>

#include "functions.h"

/**
 * Compares two square objects and determines which
 * square is larger.
 *
 * @param sq1 the first square to compare
 * @param sq2 the second square to compare
 * @exception none
 * @return 0 if the squares are equal, 1 if the first
 *         square is larger, or 2 if the second square
 *         is larger
 * @note none
 */
int compareSquares(Square sq1, Square sq2) {
    float len1 = sq1.getLength();
    float len2 = sq2.getLength();
    int result = 0;

    if (len1 > len2) {
        result = 1;
    } else if (len1 < len2) {
        result = 2;
    }

    return result;
}

/**
 * Compares two square objects and reports which square
 * is larger.
 *
 * @param sq1 the first square to compare
 * @param sq2 the second square to compare
 * @exception none
 * @return void
 * @note none
 */
void reportSquares(Square sq1, Square sq2) {
    int compare = compareSquares(sq1, sq2);

    if (compare == 0) {
        printf("squares are equal\n");
    } else if (compare == 1) {
        printf("square1 is bigger\n");
    } else if (compare == 2) {
        printf("square2 is bigger\n");
    }
}