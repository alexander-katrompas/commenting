/**
 * Name: Alexander Katrompas
 * Assignment: Demonstration Code
 * Purpose: Demonstrates a properly constructed and
 *          commented class definition file, Square.cpp.
 */

#include "square.h"

/**
 * Constructs a square with the specified side length.
 *
 * Non-positive values cause the length to be set to
 * the default value DLENGTH.
 *
 * @param length the length of a side of the square
 * @exception none
 * @return none
 * @note none
 */
Square::Square(float length) {
    setLength(length);
}

/**
 * Destroys the square.
 *
 * @param none
 * @exception none
 * @return none
 * @note none
 */
Square::~Square() {
}

/**
 * Returns the area of the square.
 *
 * The area is calculated on demand rather than stored
 * as an attribute.
 *
 * @param none
 * @exception none
 * @return the area of the square
 * @note none
 */
float Square::getArea() const {
    return length * length;
}

/**
 * Returns the side length of the square.
 *
 * @param none
 * @exception none
 * @return the side length of the square
 * @note none
 */
float Square::getLength() const {
    return length;
}

/**
 * Sets the side length of the square.
 *
 * Non-positive values cause the length to be set to
 * the default value DLENGTH.
 *
 * @param length the new side length of the square
 * @exception none
 * @return void
 * @note none
 */
void Square::setLength(float length) {
    if (length > 0) {
        this->length = length;
    } else {
        this->length = DLENGTH;
    }
}