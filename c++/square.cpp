/* *************************************************
*  Name: Alexander Katrompas
*  Assignment: Demonstration Code
*  Purpose: A demonstration of a properly
*           constructed and commented class
*           definition file, Square.cpp
************************************************* */

#include "square.h"

Square::Square(float length) {
/* **************************
* Constructor accepts a length
* and sets the length of the
* square to that length.
*
* @param float : length
* @exception : none
* @return : void
****************************/
    setLength(length);
}

Square::~Square(){
/* **************************
* Destructor (empty)
*
* @param : none
* @exception : none
* @return : void
* @note : none
****************************/
}

float Square::getArea(){
/* **************************
* Returns the area of the square. The area is
* not stored as an attribute, and is calculated
* on demand through this method.
*
* @param float : none
* @exception : none
* @return float : area of the square
* @note : none
****************************/
    return length * length;
}

float Square::getLength() {
/* **************************
* returns the length of the square
*
* @param : none
* @exception : none
* @return float : length of the square
* @note : none
****************************/
    return length;
}

void Square::setLength(float length) {
/* **************************
* sets the length of a side of the square
* including error checking that the length
* is positive, or is set to default value DELNGTH
*
* @param float : length
* @exception : none
* @return : void
* @note : none
****************************/
    if(length > 0){
        this->length = length;
    } else {
        this->length = DLENGTH;
    }
}
