/* *************************************************
*  Name: Alexander Katrompas
*  Assignment: Demonstration Code
*  Purpose: A demonstration of a properly
*           constructed and commented functions.cpp
************************************************* */

#include "functions.h"

int compareSquares(Square sq1, Square sq2){
/* *************************************************
* This function accepts two square objects,
*         compares there area and will return 0, 1 ,2.
* 0: they are equal
* 1: the first square is bigger
* 2: the second square is bigger

* @param sq1 : a Square object
* @param sq2 : a Square object
* @return 0,1,2 : which square is bigger
* @exception none
* ************************************************* */

    float len1 = sq1.getLength();
    float len2 = sq2.getLength();
    int result = 0;

    if(len1 > len2){
        result = 1;
    } else if (len1 < len2){
        result = 2;
    }

    return result;
}

