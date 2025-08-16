This Python program calculates the perimeter of a triangle given the coordinates of its three vertices.
It uses basic geometry and the distance formula to determine the length of each side, then sums them to find the total perimeter.

Object-Oriented Design:
  - 'Point' class for storing x and y coordinates
  - 'Triangle' class for storing 'Point' objects
Distance Formula: calculates the distance between two points
Rounding: the perimeter is rounded to 6 decimal places
Example Run included: demonstrates calculation of a predefined triangle.
  - (The example uses a right triangle which allows one to use basic principles of the Pythagorean Theorem to easily test this program's accuracy.)
Distance between two points (x1, y1) and (x2, y2):
      Distance = [(x2 - x1)^2 + (y2 - y1)^2]
Therefore, the perimeter of a triangle with points A, B, and C is:
      Perimeter = AB + BC + CA
