import org.scalatest.FlatSpec

class SelectionSortTest extends FlatSpec{
  // Unit Test for selection sort algorithm
  " A index of Minimum function" should "return the index of minimum" in {
    val r = new scala.util.Random
    val rand_arr: Array[Int] = 1 to 100000 map { _ => r.nextInt() } toArray
    val idx = Timer printsMillo SelectionSort.indexOfMin(0, rand_arr)
    assert(rand_arr(idx) == rand_arr.min)
  }
  " A selection sort algorithm" should "sort random list" in{
    val r = new scala.util.Random
    val rand_arr: Array[Int] = 1 to 100000 map { _ => r.nextInt() } toArray
    val selectionSorted = SelectionSort.selectionSort(rand_arr)(scala.math.Ordering[Int])
    assert(selectionSorted.deep == rand_arr.sorted.deep)
  }
}
