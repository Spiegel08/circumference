a, b, c = 10, 10, 10

def triangle_perimeter(side_a = a, side_b = b, side_c = c):
  return side_a + side_b + side_c

def triangle_area(side_a = a, side_b = b, side_c = c):
  p = (side_a + side_b + side_c) / 2
  return (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
