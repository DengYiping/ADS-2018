import org.scalatest.FlatSpec
class MergeSortVariantTest extends FlatSpec{
  "A sorting algorithm" should "be able to sort any random input" in{
    val r = new scala.util.Random
    val rand_arr: List[Int] = 1 to 100000 map { _ => r.nextInt() } toList
    val selectionSorted = MergeSortVariant.mergeSortVariant(rand_arr, 6)(scala.math.Ordering[Int])
    assert(selectionSorted == rand_arr.sorted)
  }
}
