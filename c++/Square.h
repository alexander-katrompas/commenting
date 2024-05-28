/* *************************************************
*  Name: Alexander Katrompas
*  Assignment: Demonstration Code
*  Purpose: A demonstration of a properly
*           constructed and commented class
*           declaration file, Square.h
************************************************* */

#ifndef SQUARE_H
#define SQUARE_H

#define DLENGTH 1

class Square {
public:
    /**********************
    Constructors/Destructor
    ***********************/
    Square(float);
    ~Square();

    /**********************
    Getters/Accessors
    ***********************/

    float getArea();
    float getLength();

    /**********************
    Setters/Mutators
    ***********************/
    void setLength(float);


private:
    float length;

};


#endif //SQUARE_H
