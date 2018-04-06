import org.scalatest.FlatSpec

class HeapSortTest extends FlatSpec{
  "A Heap Sort algorithm " should "sort everything" in {
    val r = new scala.util.Random
    val rand_arr = 1 to 10000 map { _ => r.nextInt()} toArray
    val rand_arr_cpy = rand_arr.clone()
    HeapSort.heapSort(rand_arr)
    println(rand_arr)
    assert(rand_arr.deep == rand_arr_cpy.sorted.deep)
  }
  "A Heap Sort Variant" should "sort everything" in {
    val r = new scala.util.Random
    val rand_arr = 1 to 10 map { _ => r.nextInt(100)} toArray
    val rand_arr_cpy = rand_arr.clone()
    HeapSortVariant.heapSortVariant(rand_arr)
    println(rand_arr)
    assert(rand_arr.deep == rand_arr_cpy.sorted.deep)
  }
  "Move to Bottom Method" should "move one element" in {
    val arr = Array(1, 2, 3, 4)
    val expected = Array(2, 3, 4, 1)
    val recovered = arr.clone()
    HeapSortVariant.moveBottom(arr, 4)
    assert(arr.deep == expected.deep)
    HeapSortVariant.recoverBottom(arr, 4)
    assert(arr.deep == recovered.deep)
  }
}
