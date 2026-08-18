/**
 * Name: Alexander Katrompas
 * Assignment: Demonstration Code
 * Purpose: Demonstrates a properly constructed and
 *          commented class declaration file, Square.h.
 */

#ifndef SQUARE_H
#define SQUARE_H

#define DLENGTH 1

/**
 * Represents a square with a configurable side length.
 *
 * The area is calculated on demand rather than stored
 * as an attribute.
 */
class Square {

public:

    // Constructors / Destructor
    Square(float);
    ~Square();

    // Getters / Accessors
    float getArea() const;
    float getLength() const;

    // Setters / Mutators
    void setLength(float);

    // Printing Methods
    // none

private:

    // Methods
    // none

    // Attributes
    float length;
};

#endif // SQUARE_H