
/* Leetcode problem 1603: Design Parking System. */

class ParkingSystem(_big: Int, _medium: Int, _small: Int) {
  var big: Int = _big
  var medium: Int = _medium
  var small: Int = _small

  def addCar(carType: Int): Boolean = {
    if (carType == 1) {
      if (big == 0) {
        return false
      }
      big = big - 1
    } else if (carType == 2) {
      if (medium == 0) {
        return false
      }
      medium = medium - 1
    } else { /* carType == 3 */
      if (small == 0) {
        return false
      }
      small = small - 1
    }
    true
  }
}
